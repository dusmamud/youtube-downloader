#!/usr/bin/env python3
"""
Core YouTube Downloader Class
"""

import os
import sys
from pathlib import Path
from typing import List, Dict, Optional
import yt_dlp
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

class YouTubeDownloader:
    """Main YouTube Downloader class with all functionality"""
    
    def __init__(self, output_dir: str = "downloads"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Available quality options
        self.video_qualities = {
            '144p': 'worst[height<=144]',
            '240p': 'worst[height<=240]',
            '360p': 'best[height<=360]',
            '480p': 'best[height<=480]',
            '720p': 'best[height<=720]',
            '1080p': 'best[height<=1080]',
            '1440p': 'best[height<=1440]',
            '2160p': 'best[height<=2160]',
            'best': 'best',
            'worst': 'worst'
        }
        
        self.audio_qualities = {
            'best': 'bestaudio/best',
            'worst': 'worstaudio/worst',
            '128k': 'bestaudio[abr<=128]',
            '192k': 'bestaudio[abr<=192]',
            '256k': 'bestaudio[abr<=256]',
            '320k': 'bestaudio[abr<=320]'
        }

    def get_ydl_opts(self, format_type: str, quality: str, output_format: str) -> Dict:
        """Generate yt-dlp options based on format and quality"""
        base_opts = {
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
            'ignoreerrors': False,
            'no_warnings': True,
            'extractor_args': {
                'youtube': {
                    'player_client': ['android', 'ios'],
                    'player_skip': ['webpage', 'configs'],
                }
            },
            'http_headers': {
                'User-Agent': 'com.google.android.youtube/19.29.37 (Linux; U; Android 14; Pixel 8 Pro) gzip',
            },
            'js_runtimes': {
                'node': {}
            }
        }
        
        if format_type == 'audio':
            if output_format in ['mp3', 'm4a']:
                base_opts.update({
                    'format': self.audio_qualities.get(quality, 'bestaudio/best'),
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': output_format,
                        'preferredquality': quality.replace('k', '') if 'k' in quality else '192',
                    }]
                })
            else:
                base_opts['format'] = self.audio_qualities.get(quality, 'bestaudio/best')
        
        elif format_type == 'video':
            if output_format == 'mp4':
                base_opts['format'] = f"{self.video_qualities.get(quality, 'best')}[ext=mp4]/best[ext=mp4]/best"
            else:
                base_opts['format'] = self.video_qualities.get(quality, 'best')
        
        return base_opts

    def download_single(self, url: str, format_type: str = 'video', 
                       quality: str = 'best', output_format: str = 'mp4') -> bool:
        """Download a single video/audio"""
        try:
            print(f"{Fore.CYAN}Downloading: {url}")
            print(f"{Fore.YELLOW}Format: {format_type} | Quality: {quality} | Output: {output_format}")
            
            ydl_opts = self.get_ydl_opts(format_type, quality, output_format)
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ret_code = ydl.download([url])
                if ret_code != 0:
                    print(f"{Fore.RED}✗ Download failed with exit code: {ret_code}")
                    return False
            
            print(f"{Fore.GREEN}✓ Successfully downloaded!")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}✗ Error downloading {url}: {str(e)}")
            return False

    def download_playlist(self, playlist_url: str, format_type: str = 'video',
                         quality: str = 'best', output_format: str = 'mp4') -> Dict:
        """Download entire playlist"""
        try:
            print(f"{Fore.CYAN}Downloading playlist: {playlist_url}")
            
            # Create playlist-specific directory
            playlist_dir = self.output_dir / "playlist_downloads"
            playlist_dir.mkdir(exist_ok=True)
            
            ydl_opts = self.get_ydl_opts(format_type, quality, output_format)
            ydl_opts['outtmpl'] = str(playlist_dir / '%(playlist_index)s - %(title)s.%(ext)s')
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Get playlist info first
                playlist_info = ydl.extract_info(playlist_url, download=False)
                if not playlist_info:
                    print(f"{Fore.RED}✗ Error: Could not fetch playlist info")
                    return {"success": False, "error": "Could not fetch playlist info"}
                
                total_videos = len(playlist_info.get('entries', []))
                print(f"{Fore.YELLOW}Found {total_videos} videos in playlist")
                
                # Download playlist
                ret_code = ydl.download([playlist_url])
                if ret_code != 0:
                    print(f"{Fore.RED}✗ Playlist download failed with exit code: {ret_code}")
                    return {"success": False, "error": f"Exit code {ret_code}"}
            
            print(f"{Fore.GREEN}✓ Playlist download completed!")
            return {"success": True, "total": total_videos}
            
        except Exception as e:
            print(f"{Fore.RED}✗ Error downloading playlist: {str(e)}")
            return {"success": False, "error": str(e)}

    def bulk_download(self, urls: List[str], format_type: str = 'video',
                     quality: str = 'best', output_format: str = 'mp4') -> Dict:
        """Download multiple URLs"""
        results = {"successful": 0, "failed": 0, "errors": []}
        
        print(f"{Fore.CYAN}Starting bulk download of {len(urls)} URLs...")
        
        for i, url in enumerate(urls, 1):
            print(f"\n{Fore.MAGENTA}[{i}/{len(urls)}] Processing: {url}")
            
            if self.download_single(url, format_type, quality, output_format):
                results["successful"] += 1
            else:
                results["failed"] += 1
                results["errors"].append(url)
        
        print(f"\n{Fore.GREEN}Bulk download completed!")
        print(f"Successful: {results['successful']}")
        print(f"Failed: {results['failed']}")
        
        return results

    def get_video_info(self, url: str) -> Optional[Dict]:
        """Get video information without downloading"""
        try:
            ydl_opts = self.get_ydl_opts('video', 'best', 'mp4')
            ydl_opts.update({'quiet': True})
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                if not info:
                    return None
                return {
                    'title': info.get('title', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'uploader': info.get('uploader', 'Unknown'),
                    'view_count': info.get('view_count', 0),
                    'upload_date': info.get('upload_date', 'Unknown')
                }
        except Exception as e:
            print(f"{Fore.RED}Error getting video info: {str(e)}")
            return None