import nextcord
from nextcord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    serverId = 1364978562800685259

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.get_channel(1364978563236892695)
        embedding = nextcord.Embed(title="Welcome",
                                  description=f"Welcome to {member.guild.name} {member.mention}\n"f"You are the {member.guild.member_count}th member",
                                  color=0x008000)
        embedding.set_thumbnail(url=member.avatar.url)
        if channel:
            await channel.send(embed=embedding)

    @commands.Cog.listener() 
    async def on_member_remove(self, member):
        channel = member.guild.get_channel(1364978563404660825)
        embedding = nextcord.Embed(title="Goodbye",
                                  description=f" {member.mention} has left the sever\n"f"There are {member.guild.member_count}member now",
                                  color=0xff0000)
        embedding.set_footer(text="cloud.inc")
        if channel:
            await channel.send(embed=embedding)

async def setup(bot):
    bot.add_cog(Greetings(bot))