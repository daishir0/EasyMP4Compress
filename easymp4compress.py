import os
import subprocess
import PySimpleGUI as sg
import re
import sys

def compress_mp4(input_file, window=None, minimum=False):
    output_dir = "compressed"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.basename(input_file)
    output_file = os.path.join(output_dir, filename)

    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-c:v", "libx264",
        "-crf", "23" if not minimum else "28",
        "-preset", "medium" if not minimum else "slow",
        "-c:a", "aac",
        "-b:a", "128k",
        "-progress", "pipe:1",
        output_file
    ]

    try:
        process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        
        duration = get_video_duration(input_file)
        
        for line in process.stdout:
            progress = parse_progress(line, duration)
            if progress is not None and window:
                window['-PROGRESS-'].update(progress)
                window['-PROGRESSBAR-'].update(progress)

        process.wait()
        if window:
            window['-PROGRESS-'].update("圧縮が完了しました。")
            window['-PROGRESSBAR-'].update(100)
        print(f"圧縮が完了しました。出力ファイル: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"エラーが発生しました: {e}")
        if window:
            window['-PROGRESS-'].update("エラーが発生しました。")

def get_video_duration(input_file):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", input_file]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def parse_progress(line, duration):
    time_match = re.search(r"out_time_ms=(\d+)", line)
    if time_match:
        time_ms = int(time_match.group(1))
        progress = min(100, int(time_ms / (duration * 10000)))
        return progress
    return None

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        minimum = '-minimum' in sys.argv
        compress_mp4(input_file, minimum=minimum)
    else:
        sg.theme('DefaultNoMoreNagging')

        layout = [
            [sg.Text("MP4ファイルを選択してください:")],
            [sg.Input(key='-FILE-', enable_events=True), sg.FileBrowse(file_types=(("MP4 Files", "*.mp4"),))],
            [sg.Text("ファイルがここに表示されます", key='-FILENAME-', size=(50, 1))],
            [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESSBAR-')],
            [sg.Text("", key='-PROGRESS-')],
            [sg.Button('圧縮開始', key='-COMPRESS-'), sg.Button('終了')]
        ]

        window = sg.Window('MP4圧縮ツール', layout, finalize=True)

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, '終了'):
                break
            elif event == '-FILE-':
                file_path = values['-FILE-']
                window['-FILENAME-'].update(file_path)
            elif event == '-COMPRESS-':
                file_path = values['-FILE-']
                if file_path and file_path.lower().endswith('.mp4'):
                    compress_mp4(file_path, window)
                else:
                    sg.popup_error('有効なMP4ファイルを選択してください。')

        window.close()

if __name__ == "__main__":
    main()
