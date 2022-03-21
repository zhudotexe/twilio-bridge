import httpx
from fastapi import FastAPI, Form

from . import config

app = FastAPI()
http = httpx.AsyncClient()


@app.post("/sms", status_code=204)
async def on_message_receive(
    source_number: str = Form(..., alias="From"),
    # destination_number: str = Form(..., alias="To"),
    body: str = Form(..., alias="Body"),
):
    payload = {"content": body, "username": source_number}
    await http.post(config.DISCORD_WEBHOOK_URL, json=payload)
