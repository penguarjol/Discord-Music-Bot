<a href="https://discord.gg/wRCgB7vBQv">
    <img src="https://img.shields.io/discord/811542332678996008?color=7289DA&label=Support&logo=discord&style=for-the-badge" alt="Discord">
</a>

# Vocard Bot
Vocard is a highly customizable Discord music bot, designed to deliver a user-friendly experience. It offers support for a wide range of streaming platforms including Youtube, Soundcloud, Spotify, Twitch, and more.

## Features
* Fast song loading
* Works with slash and message commands
* Lightweight design
* Smooth playback
* Clean and nice interface
* Supports many music platforms (YouTube, SoundCloud, etc.)
* Built-in playlist support
* Fully customizable settings
* Lyrics support
* Various sound effects
* Multiple languages available
* Easy to update
* Supports docker
* Premium dashboard (in beta)

## Screenshot
![features](https://github.com/user-attachments/assets/f34b542d-be37-4170-bb80-c44748d8eb04)

## Requirements
* [Python 3.11+](https://www.python.org/downloads/)
* [Lavalink Server (Requires 4.0.0+)](https://github.com/freyacodes/Lavalink)

## Setup
Please see the [Setup Page](https://docs.vocard.xyz) in the docs to run this bot yourself!

## Deploying to fly.io

### Setting up Secrets
Before deploying to fly.io, you need to set up your secrets. Use the following commands to securely store your sensitive information:

```bash
# Discord Bot Credentials
flyctl secrets set DISCORD_BOT_TOKEN="your_discord_bot_token"
flyctl secrets set DISCORD_CLIENT_ID="your_client_id"

# Spotify API Credentials
flyctl secrets set SPOTIFY_CLIENT_ID="your_spotify_client_id"
flyctl secrets set SPOTIFY_CLIENT_SECRET="your_spotify_client_secret"

# Genius API Token
flyctl secrets set GENIUS_TOKEN="your_genius_token"

# MongoDB Configuration
flyctl secrets set MONGODB_URL="your_mongodb_url"
flyctl secrets set MONGODB_NAME="your_mongodb_name"

# Lavalink Configuration
flyctl secrets set LAVALINK_HOST="your_lavalink_host"
flyctl secrets set LAVALINK_PORT="13592"
flyctl secrets set LAVALINK_PASSWORD="your_lavalink_password"
flyctl secrets set LAVALINK_SECURE="false"
```

### Local Development vs Production
- For local development:
  1. Copy `settings.example.json` to `settings.json`
  2. Fill in your credentials in `settings.json`
  3. The bot will use `settings.json` if environment variables are not set

- For production deployment:
  1. Make sure all secrets are set using the commands above
  2. The bot will automatically use the environment variables instead of settings.json
  3. settings.json is already in .gitignore to prevent accidentally committing sensitive data

## Need Help?
Join the [Vocard Support Discord](https://discord.gg/wRCgB7vBQv) for help or questions.

