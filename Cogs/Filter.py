import nextcord
from nextcord.ext import commands
from nextcord import Interaction
bad_words = (
    "poop",
    "medicine",
    "eden"

)

banned_words = (
    "fuck",
    "lol",
)
class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if any(word in message.content.lower() for word in banned_words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} sent a bad word")
        if any(word in message.content.lower() for word in bad_words):
            await message.channel.send(f"{message.author.mention}sorry, this is not a trading server")
async def setup(bot):
     bot.add_cog(Filter(bot))