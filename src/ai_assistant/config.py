from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_file_encoding="utf-8"
                )
    
    # --- GROQ Configuration ---
    GROQ_API_KEY: str
    GROQ_LLM_MODEL: str = "llama-3.3-70b-versatile"
    GROQ_SUMMARY_LLM_MODEL :str = "gemma2-9b-it"

    ELEVENLABS_API_KEY: str
    ELEVENLABS_VOICE_ID: str
    
    # --- Audio settings ---
    STT_MODEL_NAME: str = "whisper-large-v3-turbo"
    TTS_MODEL_NAME: str = "eleven_flash_v2_5"
    TTI_MODEL_NAME: str = "black-forest-labs/FLUX.1-schnell-Free"
    ITT_MODEL_NAME: str = "llama-3.2-90b-vision-preview"
    


    # --- Chroma Configuration ---
    CHROMA_DB_PATH: str = 'app/docs/vectordb/'
    RULES_SUMMARY_PATH: str = 'app/docs/resumen_w40k.txt'
    SHORT_TERM_MEMORY_DB_PATH: str = "/app/data/memory.db"

    # --- Short memory configuration ---
    ROUTER_MESSAGES_TO_ANALYZE: int = 3
    TOTAL_MESSAGES_SUMMARY_TRIGGER: int = 20
    TOTAL_MESSAGES_AFTER_SUMMARY: int = 5

   # --- RAG Configuration ---
    RAG_TEXT_EMBEDDING_MODEL_ID: str = "sentence-transformers/all-MiniLM-L6-v2"
    RAG_TEXT_EMBEDDING_MODEL_DIM: int = 384
    RAG_TOP_K: int = 6
    RAG_DEVICE: str = "cpu"
    RAG_CHUNK_SIZE: int = 1200




settings = Settings()
