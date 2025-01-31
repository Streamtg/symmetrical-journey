from pyrogram.types import Message
from utils.hash_generator import generate_hash
from database.db_operations import save_to_db
from plugins.blogger_integration import create_blogger_post
import os

async def handle_file(client: Client, message: Message):
    # Descargar archivo temporalmente
    file_path = await message.download()
    
    # Generar hash
    with open(file_path, "rb") as file:
        file_data = file.read()
    hash_code = generate_hash(file_data)
    
    # Guardar en DB
    file_id = message.document.file_id
    await save_to_db(hash_code, file_id)
    
    # Crear entrada en Blogger
    blog_url = await create_blogger_post(hash_code, file_id)
    
    # Responder al usuario
    await message.reply(f"🔗 Enlace de descarga: {blog_url}")
    
    # Eliminar archivo temporal
    os.remove(file_path)
