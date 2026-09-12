#!/usr/bin/env python3
"""
Utility functions for YouTube Downloader
"""

from typing import List
from colorama import Fore

def load_urls_from_file(file_path: str) -> List[str]:
    """Load URLs from a text file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return urls
    except Exception as e:
        print(f"{Fore.RED}Error reading file {file_path}: {str(e)}")
        return []

def print_banner():
    """Print application banner"""
    print(f"{Fore.CYAN}")
    print("=" * 60)
    print("    🎥 YouTube Video/Audio Archival Utility v1.0.0")
    print("    📁 Personal Backup & Creative Commons Media")
    print("    🎵 Formats: MP4, MP3, M4A | Quality: 144p-4K")
    print("=" * 60)
    print(f"{Fore.YELLOW}    ⚖️  Notice: For personal archival of your own content only.")
    print()

def validate_url(url: str) -> bool:
    """Basic URL validation for YouTube URLs"""
    youtube_domains = [
        'youtube.com',
        'youtu.be',
        'www.youtube.com',
        'm.youtube.com'
    ]
    
    return any(domain in url.lower() for domain in youtube_domains)

def format_duration(seconds: int) -> str:
    """Format duration from seconds to HH:MM:SS"""
    if not seconds:
        return "Unknown"
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes:02d}:{seconds:02d}"

def format_views(views: int) -> str:
    """Format view count in human readable format"""
    if not views:
        return "Unknown"
    
    if views >= 1_000_000_000:
        return f"{views / 1_000_000_000:.1f}B"
    elif views >= 1_000_000:
        return f"{views / 1_000_000:.1f}M"
    elif views >= 1_000:
        return f"{views / 1_000:.1f}K"
    else:
        return str(views)