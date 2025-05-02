import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random
from cogs.Welcome import Welcome
from cogs.General import General

# Load environment variables from .env file
load_dotenv()
# Token and intents
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True  # To detect reactions

# Initialize bot
bot = commands.Bot(command_prefix="/", intents=intents, help_command=None)


@bot.event
async def on_ready():
    """Bot has connected to Discord."""
    print(f"Hypatia is awakened! Logged in as {bot.user}")
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")


# Run the bot
bot.run(TOKEN)
