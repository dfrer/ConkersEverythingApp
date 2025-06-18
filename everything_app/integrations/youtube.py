"""Placeholder for YouTube API integration."""

import webbrowser


class YouTubeIntegration:
    def __init__(self, config):
        self.config = config

    def open_homepage(self) -> None:
        url = "https://www.youtube.com"
        print(f"Opening {url}")
        webbrowser.open(url)

