# Personal Everything App

This repository contains the initial foundation for a personal "Everything App". The app aims to unify many day–to–day tasks such as note taking, timers and basic integrations with services like YouTube, Gmail and Twitter.

## Features

- **Deep customization** via a JSON configuration file.
- **Notes module** for quick text notes.
- **Timers module** for simple countdown timers.
- **Orders module** placeholder for future ordering features.
- **Integrations** with YouTube, Gmail and Twitter (currently placeholders).

## Running

The project requires Python 3. Run the CLI using:

```bash
python -m everything_app.main
```

Commands available in the demo:

- `notes` &mdash; add a note.
- `timer` &mdash; start a timer in seconds.
- `exit` &mdash; quit the app.

Feel free to extend the modules and integrations to suit your personal workflow.

## Installation

### Python dependencies

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install required packages (FastAPI and Uvicorn are used for the API server):

   ```bash
   pip install fastapi uvicorn
   ```

### Node dependencies

1. Navigate to your Next.js frontend directory (for example `frontend/`):

   ```bash
   cd frontend
   ```

2. Install packages with npm:

   ```bash
   npm install
   ```

## Development

### Start the FastAPI server

Run Uvicorn pointing at your FastAPI app. Assuming the app is exposed as
`app` inside `everything_app/api.py`:

```bash
uvicorn everything_app.api:app --reload
```

### Run the Next.js frontend

From the `frontend` directory, start the development server:

```bash
npm run dev
```

The frontend will typically be available at `http://localhost:3000`.

## Deployment

The recommended way to deploy the Next.js app is via [Vercel](https://vercel.com/).
After installing the Vercel CLI and logging in, deploy with:

```bash
vercel --prod
```


