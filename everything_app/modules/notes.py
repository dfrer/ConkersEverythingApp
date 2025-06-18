"""Simple notes module."""

from pathlib import Path


class NotesModule:
    def __init__(self, config, file_path: str = "notes.txt"):
        self.config = config
        self.file_path = Path(file_path)

    def add(self, text: str) -> None:
        with self.file_path.open("a") as f:
            f.write(text + "\n")
        print("Note saved")

