
# EasyMP4Compress

## Overview
EasyMP4Compress is a simple and user-friendly tool for compressing MP4 video files. It provides both a graphical user interface (GUI) and command-line interface (CLI) for easy operation. The program uses FFmpeg for video compression, offering options for standard and minimum compression.

## Installation
To install EasyMP4Compress, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/daishir0/EasyMP4Compress
   ```
2. Change to the project directory:
   ```
   cd EasyMP4Compress
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Ensure FFmpeg is installed on your system. If not, install it according to your operating system's instructions.

## Usage
### GUI Mode
1. Run the program without arguments:
   ```
   python easymp4compress.py
   ```
2. Use the file browser to select an MP4 file.
3. Click "Compress" to start the compression process.

### CLI Mode
For standard compression:
```
python easymp4compress.py /path/to/your/video.mp4
```

For minimum compression:
```
python easymp4compress.py /path/to/your/video.mp4 -minimum
```

## Notes
- Compressed files are saved in a "compressed" folder in the same directory as the original file.
- The GUI displays a progress bar during compression.
- The program uses FFmpeg for compression, so make sure FFmpeg is properly installed on your system.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# EasyMP4Compress

## 概要
EasyMP4Compressは、MP4ビデオファイルを圧縮するためのシンプルで使いやすいツールです。グラフィカルユーザーインターフェース（GUI）とコマンドラインインターフェース（CLI）の両方を提供し、簡単に操作できます。このプログラムはFFmpegを使用してビデオ圧縮を行い、標準圧縮と最小圧縮のオプションを提供します。

## インストール方法
EasyMP4Compressをインストールするには、以下の手順に従ってください：

1. リポジトリをクローンします：
   ```
   git clone https://github.com/daishir0/EasyMP4Compress
   ```
2. プロジェクトディレクトリに移動します：
   ```
   cd EasyMP4Compress
   ```
3. 必要な依存関係をインストールします：
   ```
   pip install -r requirements.txt
   ```
4. FFmpegがシステムにインストールされていることを確認します。インストールされていない場合は、お使いのオペレーティングシステムの指示に従ってインストールしてください。

## 使い方
### GUIモード
1. 引数なしでプログラムを実行します：
   ```
   python easymp4compress.py
   ```
2. ファイルブラウザを使用してMP4ファイルを選択します。
3. "圧縮開始"をクリックして圧縮プロセスを開始します。

### CLIモード
標準圧縮の場合：
```
python easymp4compress.py /path/to/your/video.mp4
```

最小圧縮の場合：
```
python easymp4compress.py /path/to/your/video.mp4 -minimum
```

## 注意点
- 圧縮されたファイルは、元のファイルと同じディレクトリ内の "compressed" フォルダに保存されます。
- GUIでは圧縮中にプログレスバーが表示されます。
- このプログラムは圧縮にFFmpegを使用しているため、システムにFFmpegが適切にインストールされていることを確認してください。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。
