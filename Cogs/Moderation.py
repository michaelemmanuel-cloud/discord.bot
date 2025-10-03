import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="kick", description="Kick a member from the server")
    # @commands.has_permissions(kick_members=True)
    async def kick(self, interaction: Interaction, member: nextcord.Member, *, reason: str ="No reason provided"):
        if member == interaction.user:
            await interaction.response.send_message("You cannot kick yourself")
            return
        if member == interaction.guild.me:
            await interaction.response.send_message("You can't kick me blud")
            return
        if member.top_role >= interaction.user.top_role and interaction.user != interaction.guild.owner:
            await interaction.response.send_message("You cannot kick someone with a role equal or higher than you")
            return
        await member.kick(reason=reason)
        await interaction.response.send_message(f"{member.mention} has been kicked.\nReason: {reason}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to kick blud. Go get admin")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned. Reason: {reason}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to ban blud. Go get admin")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: int):
        user = await self.bot.fetch_user(user_id)
        await ctx.guild.unban(user)
        await ctx.send(f"{user.mention} has been unbanned")

    @commands.command()
    async def poll(self, ctx, *, question):
        embeder = nextcord.Embed(title="Cloud's Server", description=question)
        message = await ctx.send(embed=embeder)
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await ctx.message.delete()

    @commands.command()
    async def embed(self, ctx, *, content):
        embedding = nextcord.Embed(title="Cloud's Server", description=content, color=0x0000ff)
        await ctx.send(embed=embedding)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Moderation(bot))
