from pyrogram import Client
from pyrogram.types import Message
from utils.hash_generator import generate_hash
from database.db_operations import save_to_db
from blogger_api.create_post import create_blogger_post
import os

async def handle_file(client: Client, message: Message):
    # Descargar archivo temporalmente
    file_path = await message.download()
    
    try:
        # Generar hash
        with open(file_path, "rb") as f:
            file_data = f.read()
        hash_code = generate_hash(file_data)
        
        # Guardar en MongoDB
        file_id = message.document.file_id
        await save_to_db(hash_code, file_id)
        
        # Crear entrada en Blogger
        blog_url = await create_blogger_post(hash_code, file_id)
        
        # Responder al usuario
        await message.reply(f"🔗 Enlace de dedcarga: {blog_url}")
    
    except Exception as e:
        await message.reply("❌ Error al procesar el archivo.")
        raise e
    
    finally:
        # Eliminar archivo temporal
        if os.path.exists(file_path):
            os.remove(file_path)
