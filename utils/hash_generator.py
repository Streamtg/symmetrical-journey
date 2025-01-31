import hashlib

def generate_hash(file_data: bytes) -> str:
    return hashlib.sha256(file_data).hexdigest()[:12]  # 12 caracteres (ej: a1B2c3D4e5F6)
