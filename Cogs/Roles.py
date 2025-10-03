import nextcord
from nextcord.ext import commands
from nextcord.types.interactions import Interaction



class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    serverId = 1364978562800685259

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, message, user: nextcord.Member, * , role: nextcord.Role):
        if role in user.roles:
            await ctx.send(f"{user.mention} already has that role {role}")
        else:
            await user.add_roles(role)
            await message.send(f"{user.mention} has been assigned {role}")

    @addrole.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Blud doesnt have permission to run this command")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, user: nextcord.Member, *, role: nextcord.Role):
        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f"{role} has been removed from {user.mention}")
        else:
            await user.remove_roles()
            await ctx.send(f"{user.mention} does not have that role")

    @removerole.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Blud doesnt have permission to run this command")

async def setup(bot):
     bot.add_cog(Roles(bot))