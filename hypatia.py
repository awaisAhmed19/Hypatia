import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random
from cogs.Welcome import Welcome

# Load environment variables from .env file
load_dotenv()
# Token and intents
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True  # To detect reactions

# Initialize bot
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    """Bot has connected to Discord."""
    print(f"Hypatia is awakened! Logged in as {bot.user}")


async def setup_hook():
    await bot.add_cog(Welcome(bot))


bot.setup_hook = setup_hook
# Run the bot
bot.run(TOKEN)
