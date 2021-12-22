from discord.commands import slash_command
from discord.ext import commands

from settings import GUILD_ID

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    @slash_command(guild_ids=[GUILD_ID])
    async def hello(self, ctx):
        await ctx.respond('hello')

def setup(bot):
    bot.add_cog(Example(bot))
