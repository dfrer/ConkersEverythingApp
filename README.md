# Personal Everything App

This repository contains the initial foundation for a personal "Everything App". The app aims to unify many day-to-day tasks such as note taking, timers and basic integrations with services like YouTube, Gmail and Twitter.

## Features

- **Deep customization** via a JSON configuration file.
- **Notes module** for quick text notes.
- **Timers module** for simple countdown timers.
- **Orders module** placeholder for future ordering features.
- **Integrations** with YouTube, Gmail and Twitter (currently placeholders).
- **Web UI** built with Next.js located in the `web` directory.

## Running

The project requires Python 3. Run the CLI using:

```bash
python -m everything_app.main
```

To run the HTTP API instead, launch:

```bash
uvicorn everything_app.api:app
```

Commands available in the demo:

- `notes` — add a note.
- `timer` — start a timer in seconds.
- `exit` — quit the app.

The web frontend can be started locally with:


