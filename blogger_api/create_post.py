from googleapiclient.discovery import build
from config import Config
import logging

logger = logging.getLogger(__name__)

async def create_blogger_post(hash_code: str, file_id: str) -> str:
    try:
        service = build("blogger", "v3", developerKey=Config.BLOGGER_API_KEY)
        
        # URL de descarga de Telegram
        download_url = f"https://api.telegram.org/file/bot{Config.BOT_TOKEN}/{file_id}"
        
        # Cuerpo del post
        post_body = {
            "title": f"📥 Descarga {hash_code}",
            "content": f"""
                <script>
                    window.location.href = "{download_url}";
                </script>
                <p>Si no eres redirigido, haz clic <a href="{download_url}">aquí</a>.</p>
            """,
            "labels": ["Telegram Bot", "Descarga"]
        }
        
        # Publicar en Blogger
        request = service.posts().insert(blogId=Config.BLOG_ID, body=post_body)
        response = request.execute()
        return response["url"]
    
    except Exception as e:
        logger.error(f"Error en Blogger: {e}")
        return None
