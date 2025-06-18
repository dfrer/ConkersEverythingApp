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

    def run_api(self, host: str = "127.0.0.1", port: int = 8000) -> None:
        """Start the FastAPI server bound to this ``EverythingApp``."""
        if not self.modules:
            self.start()
        from .api import create_api
        import uvicorn

        api_app = create_api(self)
        uvicorn.run(api_app, host=host, port=port)

