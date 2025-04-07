
from telethon import TelegramClient, events
import os

# Variabili da configurare
API_ID = int(os.environ.get("TELEGRAM_API_ID", "YOUR_API_ID"))
API_HASH = os.environ.get("TELEGRAM_API_HASH", "YOUR_API_HASH")
SESSION_NAME = os.environ.get("SESSION_NAME", "telegh_session")

# Crea il client Telegram
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    print(f"Messaggio da {sender.username or sender.id}: {event.raw_text}")
    await event.reply("Messaggio ricevuto! Questo è un bot di test.")

# Avvia il bot
print("Avvio del bot...")
client.start()
client.run_until_disconnected()
