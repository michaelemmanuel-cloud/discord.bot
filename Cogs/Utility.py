import nextcord
from nextcord import guild
from nextcord.ext import commands
from nextcord import Interaction

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    serverId = 1364978562800685259

    @commands.command()
    async def remind(self, ctx, *, msg):
        await ctx.author.send(f"Here to remind your about {msg}")

    @commands.command()
    async def membercount(self, ctx, *, member_count=None):
        await ctx.send(f"There are {member_count}")

async def setup(bot):
    bot.add_cog(Utility(bot))