import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

load_dotenv()


greetings = (
    "yo",
    "sup",
    "what's poppin'",
    "hey bestie",
    "howdy",
    "heyyy",
    "wassup",
    "yooo",
    "ayoo",
    "hiii",
    "what’s good",
    "sheeesh",
    "top of the morning",
    "yo fam",
    "my slime",
    "greetings earthling",
    "what it do",
    "wagwan",
    "hola",
    "eyy",
    "hey hey hey",
)
welcome_messages = [
    "I, Hypatia of Alexandria, welcome you {name}, seeker of wisdom 🧠✨",
    "Greetings {name}, another light joins our eternal library 📚🔥",
    "Welcome {name}, may your scrolls overflow with knowledge 🏛️📝",
]
TOKEN = os.getenv("DISCORD_TOKEN")
intent = discord.Intents.default()
intent.message_content = True
intent.members = True
intents.reactions = True  # to detect reactions
bot = commands.Bot(command_prefix="/", intents=intent)


@bot.event
async def on_ready():
    print(f"Hypatia is awakened! logged in as {bot.user}")


# Welcome messages
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1365689319200915477)
    if channel:
        message = random.choice(welcome_messages).format(name=member.name)
        await channel.send(message)


# test
@bot.command()
async def fakejoin(ctx):
    await on_member_join(ctx.author)


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    if msg.content.lower() in greetings:
        await msg.channel.send(random.choice(greetings))
    await bot.process_commands(msg)


@bot.command()
async def qoute(ctx):
    qoutes = [
        "Reserve your right to think, for even to think wrongly is better than not to think at all.",
        "Life is an unfoldment, and the further we travel the more truth we can comprehend.",
        "All formal dogmatic religions are fallacious and must never be accepted by self-respecting persons.",
    ]

    await ctx.send(random.choice(qoutes))


@bot.command()
async def Hypatia(ctx):
    replies = ["Yes?", "How can I help you?", "elegant day isnt it?"]

    await ctx.send(random.choice(replies))


bot.run(TOKEN)
