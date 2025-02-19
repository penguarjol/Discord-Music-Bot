import os
from typing import (
    Dict,
    List,
    Any,
    Union
)

def get_env_or_setting(env_key: str, settings: Dict, settings_key: str, default: Any = None) -> Any:
    """Get value from environment variable or settings dict"""
    return os.getenv(env_key) or settings.get(settings_key, default)

class Settings:
    def __init__(self, settings: Dict) -> None:
        # Core credentials from environment variables or settings
        self.token: str = get_env_or_setting("DISCORD_BOT_TOKEN", settings, "token")
        self.client_id: int = int(get_env_or_setting("DISCORD_CLIENT_ID", settings, "client_id", 0))
        self.spotify_client_id: str = get_env_or_setting("SPOTIFY_CLIENT_ID", settings, "spotify_client_id")
        self.spotify_client_secret: str = get_env_or_setting("SPOTIFY_CLIENT_SECRET", settings, "spotify_client_secret")
        self.genius_token: str = get_env_or_setting("GENIUS_TOKEN", settings, "genius_token")
        self.mongodb_url: str = get_env_or_setting("MONGODB_URL", settings, "mongodb_url")
        self.mongodb_name: str = get_env_or_setting("MONGODB_NAME", settings, "mongodb_name")
        
        self.invite_link: str = "https://discord.gg/wRCgB7vBQv"
        
        # Handle Lavalink nodes with environment variables
        if os.getenv("LAVALINK_HOST"):
            self.nodes = {
                "DEFAULT": {
                    "host": os.getenv("LAVALINK_HOST"),
                    "port": int(os.getenv("LAVALINK_PORT", "443")),
                    "password": os.getenv("LAVALINK_PASSWORD"),
                    "secure": os.getenv("LAVALINK_SECURE", "false").lower() == "true",
                    "identifier": os.getenv("LAVALINK_IDENTIFIER", "DEFAULT")
                }
            }
        else:
            self.nodes: Dict[str, Dict[str, Union[str, int, bool]]] = settings.get("nodes", {})
        self.max_queue: int = settings.get("default_max_queue", 1000)
        self.bot_prefix: str = settings.get("prefix", "")
        self.activity: List[Dict[str, str]] = settings.get("activity", [{"listen": "/help"}])
        self.logging: Dict[Union[str, Dict[str, Union[str, bool]]]] = settings.get("logging", {})
        self.embed_color: str = int(settings.get("embed_color", "0xb3b3b3"), 16)
        self.bot_access_user: List[int] = settings.get("bot_access_user", [])
        self.sources_settings: Dict[Dict[str, str]] = settings.get("sources_settings", {})
        self.cooldowns_settings: Dict[str, List[int]] = settings.get("cooldowns", {})
        self.aliases_settings: Dict[str, List[str]] = settings.get("aliases", {})
        self.controller: Dict[str, Dict[str, Any]] = settings.get("default_controller", {})
        self.voice_status_template: str = settings.get("default_voice_status_template", "")
        self.lyrics_platform: str = settings.get("lyrics_platform", "A_ZLyrics").lower()
        self.ipc_client: Dict[str, Union[str, bool, int]] = settings.get("ipc_client", {})
        self.version: str = settings.get("version", "")