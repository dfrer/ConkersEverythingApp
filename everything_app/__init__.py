from .config import Config

class EverythingApp:
    """Base application class that loads modules and integrations."""

    def __init__(self, config_path: str = "config.json"):
        self.config = Config(config_path)
        self.integrations = {}
        self.modules = {}

    def load_integrations(self) -> None:
        """Load builtin integrations."""
        from .integrations import youtube, gmail, twitter

        self.integrations["youtube"] = youtube.YouTubeIntegration(self.config)
        self.integrations["gmail"] = gmail.GmailIntegration(self.config)
        self.integrations["twitter"] = twitter.TwitterIntegration(self.config)

    def load_modules(self) -> None:
        """Load builtin modules."""
        from .modules import notes, timers, orders

        self.modules["notes"] = notes.NotesModule(self.config)
        self.modules["timers"] = timers.TimersModule(self.config)
        self.modules["orders"] = orders.OrdersModule(self.config)

    def start(self) -> None:
        self.load_integrations()
        self.load_modules()
        print("Everything App initialized with modules:")
        for name in self.modules:
            print(f" - {name}")
        print("Integrations:")
        for name in self.integrations:
            print(f" - {name}")

