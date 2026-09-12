# 🎥 YouTube Video Downloader

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub release](https://img.shields.io/badge/release-v1.0.0-green.svg)](https://github.com/dusmamud/youtube-downloader/releases)
[![Notice: Personal Archival](https://img.shields.io/badge/Notice-Personal%20Archival%20Only-orange.svg)](DISCLAIMER.md)

A comprehensive, professional-grade media backup and archival utility for creators with support for single videos, playlists, bulk downloads, and multiple formats/resolutions.

> [!IMPORTANT]
> **LEGAL NOTICE & FAIR USE ARCHIVAL POLICY:**
> This tool is strictly intended for **personal backup and archival of your own original content** or media licensed under permissive **Creative Commons / Public Domain** licenses. Downloading copyrighted media without express authorization from the rights holder is prohibited. This software does **not** bypass or decrypt DRM (Digital Rights Management) protections. Please review [**DISCLAIMER.md**](DISCLAIMER.md) before use.

## ✨ Features

- 🎬 **Single Video Download** - Download individual YouTube videos
- 📁 **Playlist Download** - Download entire YouTube playlists with organized structure
- 📋 **Bulk Download** - Download multiple videos from a text file
- 🎵 **Multiple Formats** - Support for MP4, MP3, M4A
- 🎯 **Quality Options** - Various video resolutions (144p to 4K) and audio bitrates
- ℹ️ **Video Info** - Get detailed video information without downloading
- 🖥️ **Cross-platform** - Works on Windows, macOS, and Linux
- 🎨 **Interactive Mode** - User-friendly interactive interface
- 🚀 **Fast & Reliable** - Built with yt-dlp for optimal performance

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/dusmamud/youtube-downloader.git
cd youtube-downloader

# Install dependencies
pip install -r requirements.txt

# Download your video backup
python youtube_downloader.py "https://www.youtube.com/watch?v=YOUR_OWN_VIDEO_ID"
```

## 📦 Installation

### Prerequisites
- **Python 3.7+** - [Download here](https://www.python.org/downloads/)
- **FFmpeg** - Required for audio conversion ([Installation guide](docs/INSTALLATION.md))

### Method 1: Git Clone (Recommended)
```bash
git clone https://github.com/dusmamud/youtube-downloader.git
cd youtube-downloader
pip install -r requirements.txt
```

### Method 2: Download ZIP
1. Download ZIP from [GitHub releases](https://github.com/dusmamud/youtube-downloader/releases)
2. Extract and navigate to folder
3. Run: `pip install -r requirements.txt`

For detailed installation instructions, see [Installation Guide](docs/INSTALLATION.md).

## 🎯 Usage

### Basic Commands

```bash
# Download video (MP4, best quality)
python youtube_downloader.py "VIDEO_URL"

# Download audio as MP3
python youtube_downloader.py "VIDEO_URL" -f audio -o mp3

# Download playlist
python youtube_downloader.py "PLAYLIST_URL" -p

# Get video information
python youtube_downloader.py "VIDEO_URL" -i

# Interactive mode
python youtube_downloader.py
```

### Advanced Examples

```bash
# High-quality audio download
python youtube_downloader.py "VIDEO_URL" -f audio -o mp3 -q 320k

# Playlist as MP3 files
python youtube_downloader.py "PLAYLIST_URL" -p -f audio -o mp3

# Bulk download from file
python youtube_downloader.py -b urls.txt -q 1080p

# Custom output directory
python youtube_downloader.py "VIDEO_URL" -d "~/Downloads/YouTube"
```

## 📋 Command Line Options

| Option | Description | Values |
|--------|-------------|--------|
| `-f, --format` | Download format | `video`, `audio` |
| `-q, --quality` | Quality setting | `144p`-`2160p`, `best`, `worst`, `128k`-`320k` |
| `-o, --output` | Output format | `mp4`, `mp3`, `m4a` |
| `-d, --dir` | Output directory | Any valid path |
| `-p, --playlist` | Download playlist | Flag |
| `-b, --bulk` | Bulk download | Path to URLs file |
| `-i, --info` | Show video info | Flag |

## 📁 Project Structure

```
youtube-downloader/
├── 📄 youtube_downloader.py    # Main CLI interface
├── 📁 src/                     # Source code
│   ├── 🐍 __init__.py
│   ├── 🐍 downloader.py        # Core downloader class
│   └── 🐍 utils.py             # Utility functions
├── 📁 docs/                    # Documentation
│   ├── 📖 INSTALLATION.md
│   ├── 📖 USAGE.md
│   └── 📖 TROUBLESHOOTING.md
├── 📁 tests/                   # Unit tests
├── 📄 requirements.txt         # Dependencies
├── 📄 requirements-dev.txt     # Development dependencies
├── 📄 setup.py                 # Package setup
├── 📄 .gitignore              # Git ignore rules
├── 📄 LICENSE                  # MIT License
└── 📄 README.md               # This file
```

## 🎵 Quality Options

### Video Resolutions
- `144p` - Mobile quality
- `360p` - Standard definition
- `720p` - HD quality
- `1080p` - Full HD
- `1440p` - 2K quality
- `2160p` - 4K quality
- `best` - Highest available
- `worst` - Lowest available

### Audio Bitrates
- `128k` - Good quality (smaller files)
- `192k` - High quality (recommended)
- `256k` - Very high quality
- `320k` - Maximum quality
- `best` - Best available
- `worst` - Lowest available

## 📝 Bulk Download Format

Create a text file with URLs (one per line):

```txt
# Your own playlist
https://www.youtube.com/watch?v=YOUR_OWN_VIDEO_ID_1
https://www.youtube.com/watch?v=YOUR_OWN_VIDEO_ID_2

# Creative Commons / Public Domain educational playlist
https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID

# Single video backup
https://www.youtube.com/watch?v=YOUR_OWN_VIDEO_ID_3
```

## 📂 Output Structure

```
downloads/
├── 🎬 Single Video.mp4
├── 🎵 Audio File.mp3
├── 📁 playlist_downloads/
│   ├── 01 - First Video.mp4
│   ├── 02 - Second Video.mp4
│   └── 03 - Third Video.mp4
└── 🎬 Another Video.mp4
```

## 🧪 Testing

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=src
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
# Clone and setup
git clone https://github.com/dusmamud/youtube-downloader.git
cd youtube-downloader

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `yt-dlp not found` | `pip install --upgrade yt-dlp` |
| `FFmpeg not found` | [Install FFmpeg](docs/INSTALLATION.md#ffmpeg-installation) |
| Permission denied | Change output directory or run as admin |
| Video unavailable | Check if video is public/accessible |

For detailed troubleshooting, see [Troubleshooting Guide](docs/TROUBLESHOOTING.md).

## 📚 Documentation

- 📖 [Installation Guide](docs/INSTALLATION.md) - Detailed setup instructions
- 📖 [Usage Guide](docs/USAGE.md) - Comprehensive usage examples
- 📖 [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions
- 🤝 [Contributing](CONTRIBUTING.md) - How to contribute

## 🔧 Dependencies

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - YouTube downloading engine
- **[colorama](https://github.com/tartley/colorama)** - Cross-platform colored output
- **[FFmpeg](https://ffmpeg.org/)** - Audio/video processing (external)

## ⚖️ Legal Notice & Terms of Use

This software is developed strictly for **educational and personal media backup purposes**. Users must adhere to the following terms:
- **Own Content Archival**: Exclusively intended for creators to download and archive their own uploaded media or content explicitly licensed under Creative Commons / Public Domain.
- **Respect Copyright**: Do not download or distribute copyrighted material without explicit permission from the rights holder.
- **No DRM Circumvention**: This software does **NOT** circumvent, decrypt, or tamper with DRM technologies (Widevine, FairPlay).
- **YouTube Terms of Service**: Users are solely responsible for complying with YouTube's Terms of Service and applicable local copyright laws.

For complete terms, liability limitations, and policy details, see [**DISCLAIMER.md**](DISCLAIMER.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Support

- ⭐ Star this repository if you find it helpful
- 🐛 [Report bugs](https://github.com/dusmamud/youtube-downloader/issues)
- 💡 [Request features](https://github.com/dusmamud/youtube-downloader/issues)
- 🤝 [Contribute code](CONTRIBUTING.md)

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/dusmamud/youtube-downloader?style=social)
![GitHub forks](https://img.shields.io/github/forks/dusmamud/youtube-downloader?style=social)
![GitHub issues](https://img.shields.io/github/issues/dusmamud/youtube-downloader)
![GitHub pull requests](https://img.shields.io/github/issues-pr/dusmamud/youtube-downloader)

---

<div align="center">
Made with ❤️ for the YouTube downloading community
</div>