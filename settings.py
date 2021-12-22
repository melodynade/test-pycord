import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']
GUILD_ID = int(os.environ['GUILD_ID'])
