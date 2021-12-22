import discord

from settings import DISCORD_BOT_TOKEN

bot = discord.Bot()

extensions = [
    'cogs.example'
]

for extension in extensions:
    bot.load_extension(extension)

bot.run(DISCORD_BOT_TOKEN)
