from pyrogram.types import Message

async def start_command(client: Client, message: Message):
    await message.reply_text(
        "¡Hola! Envíame un archivo y te generaré un enlace de descarga directa 📁.https://yoelmod.blogspot.com"
    )
