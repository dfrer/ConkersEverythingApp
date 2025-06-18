"""Basic timer module."""

import time


class TimersModule:
    def __init__(self, config):
        self.config = config

    def start_timer(self, seconds: int) -> None:
        print(f"Timer started for {seconds} seconds")
        time.sleep(seconds)
        print("Time's up!")

