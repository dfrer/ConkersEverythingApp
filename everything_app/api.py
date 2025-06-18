from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

from . import EverythingApp


def create_api(app_instance: EverythingApp) -> FastAPI:
    """Return a FastAPI app wired to an EverythingApp instance."""
    api = FastAPI()

    class NoteRequest(BaseModel):
        text: str

    class TimerRequest(BaseModel):
        seconds: int

    @api.post("/notes")
    def add_note(note: NoteRequest):
        """Append a note using the Notes module."""
        app_instance.modules["notes"].add(note.text)
        return {"status": "saved"}

    @api.post("/timer")
    async def start_timer(req: TimerRequest):
        """Start a timer asynchronously via the Timers module."""
        asyncio.create_task(
            asyncio.to_thread(app_instance.modules["timers"].start_timer, req.seconds)
        )
        return {"status": "started"}

    return api


# Default app used when running ``uvicorn everything_app.api:app``
_default_app = EverythingApp()
_default_app.start()
app = create_api(_default_app)
