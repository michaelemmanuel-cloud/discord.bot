# #from glob import magic_check
#
# import discord
# # from Tools.demo.mcast import sender
# # from Tools.scripts.generate_opcode_h import footer
# from discord.app_commands.checks import has_permissions
# from discord.ext import commands
# import logging
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
# token =os.getenv("DISCORD_TOKEN")
# bad_words = (
#     "poop",
#     "medicine",
#     "eden"
# )
#
# banned_words = (
#     "trade",
#     "trading",
#     "lf"
# )
#
# #logging stuff
# handler = logging.FileHandler(filename = "bot.logs", encoding="UTF-8", mode = "w")
# intent = discord.Intents.all()
# intent.members = True
# intent.message_content = True
#
# #command prefix
# bot = commands.Bot(command_prefix = "!", intents = intent)
#
# #reminder/list
# @bot.command()
# async def remind(ctx, *, msg):
#     await ctx.author.send(f"Here to remind your about {msg}")
#
# @bot.event
# async def on_ready():
#     print(f"{bot.user.name} is online 🤖")
#     await bot.change_presence(status=discord.Status.idle, activity=discord.Game("GTA XI"))
#
# #polls
# @bot.command()
# async def poll(ctx, *,  question):
#     embeder = discord.Embed(title="Cloud's Sever", description=question)
#     poll.message = await ctx.send(embed=embeder)
#     await poll.message.add_reaction("1️⃣")
#     await poll.message.add_reaction("2️⃣")
#     await ctx.message.delete()



#welcomer with member's pfp/ event
# @bot.event
# async def on_member_join(member):
#     channel = member.guild.get_channel( 1364978563236892695)
#     embedding = discord.Embed(title="Welcome", description=f"Welcome to {member.guild.name} {member.mention}\n"f"You are the {member.guild.member_count}th member", color=0x008000)
#     embedding.set_thumbnail(url=member.avatar.url)
#     if channel:
#         await channel.send(embed=embedding)
# #member leave / event
# @bot.event
# async def on_member_remove(member):
#     channel = member.guild.get_channel(1364978563404660825)
#     embedding = discord.Embed(title="Goodbye", description=f" {member.mention} has left the sever\n"f"There are {member.guild.member_count}member now",color=0xff0000)
#     embedding.set_footer(text="cloud.inc")
#     await channel.send(embed=embedding)

#word filter
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if any (word in message.content.lower() for word in bad_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention} sent a bad word")
    if any (word in message.content.lower() for word in banned_words):
        await message.channel.send(f"{message.author.mention}sorry, this is not a trading server")

    await bot.process_commands(message)

#help function
@bot.command()
async def about(ctx):
    embedding = discord.Embed(title="Commands", description=" The command prefix is (!)"
                   "Here are the commands you can use:\n"
                   "**ban**<username> - bans a member\n"
                   "**kick**<username> -kicks a member\n"
                   "**help** - Display this help message\n"
                   "**addrole** <role_name> - Add a role to yourself by specifying the role name\n"
                   "**removerole** <role_name> - Removes a role from yourself\n"
                   "**embed** <message> - To embed messages\n"
                   "**poll** <message> - Creating polls with in-built reactions\n"
                   "**remind** <message> - Dm's you", color=0x0000ff)
    await ctx.send(embed=embedding)


#adding roles tto self
# @bot.command()
# async def addrole(ctx, *, role_name):
#     role = discord.utils.get(ctx.guild.roles, name =role_name)
#     # await ctx.author.add_roles(role)
#     if role:
#         await ctx.author.add_roles(role)
#         await ctx.send(f"{role} has been assigned to {ctx.author.mention}")
#     else:
#         await ctx.send("That role does not exist")
#
# #removing role from self
# @bot.command()
# async def removerole(ctx, *, role_name):
#     role = discord.utils.get(ctx.guild.roles, name=role_name)
#     # await ctx.author.add_roles(role)
#     if role:
#         await ctx.author.remove_roles(role)
#         await ctx.send(f"{role.mention} has been removed from {ctx.author.mention}")
#     else:
#         await ctx.send("That role does not exist")

# @bot.command()
# @has_permissions(kick_members= True)
# async def kick(ctx, member:discord.Member, * , reason=None):
#     await member.kick(reason=reason)
#     await ctx.send(f"{member.mention} has been kicked.\n Reason; {reason}")
#
#
# @kick.error
# async def kick_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send("You do not have permission to kick blud.Go get admin")
#
# @bot.command()
# @has_permissions(ban_members= True)
# async def ban(ctx, member:discord.Member, * , reason=None):
#     await member.ban(reason=reason)
#     await ctx.send(f"{member.mention} has been banned. Reason; {reason}")
#
# @ban.error
# async def ban_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send("You do not have permission to ban blud.Go get admin")
#
# @bot.command()
# @has_permissions(ban_members=True)
# async def unban(ctx, member:discord.Member, * ,reason=None):
#     await member.unban(reason=reason)
#     await ctx.send(f"{member.mention} has been unbanned")

bot.run(token, log_handler = handler, log_level = logging.DEBUG )
