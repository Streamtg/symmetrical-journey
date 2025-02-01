from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from handlers.file_handler import handle_file
from handlers.commands import start_command

app = Client(
    "TG-Blogger-Bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# Comandos
app.add_handler(filters.command("start")(start_command))

# Manejador de archivos
@app.on_message(filters.document | filters.video | filters.audio)
async def file_handler(client: Client, message: Message):
    await handle_file(client, message)

if __name__ == "__main__":
    app.run()
