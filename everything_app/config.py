import json
from pathlib import Path

class Config:
    """Simple configuration storage."""

    def __init__(self, path: str = "config.json"):
        self.path = Path(path)
        if self.path.exists():
            self.data = json.loads(self.path.read_text())
        else:
            self.data = {"user": "me"}
            self.save()

    def save(self) -> None:
        self.path.write_text(json.dumps(self.data, indent=4))

    def get(self, key: str, default=None):
        return self.data.get(key, default)

    def set(self, key: str, value) -> None:
        self.data[key] = value
        self.save()

