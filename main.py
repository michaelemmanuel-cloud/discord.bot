import asyncio
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import logging
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="bot.logs", encoding="UTF-8", mode="w")
intent = nextcord.Intents.default()
intent.members = True
intent.message_content = True

bot = commands.Bot(command_prefix="!", intents=intent)

serverId = 1364978562800685259

@bot.slash_command(name="pest", description="slash commands", guild_ids=[serverId])
async def test(interaction: Interaction):
    await interaction.response.send_message("This is the test brotherblud")

async def load_cogs():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"{bot.user} is online ✅")
    await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Game("GTA XI"))
    await load_cogs()

if __name__ == "__main__":
    bot.run(TOKEN)



