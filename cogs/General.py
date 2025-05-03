import discord
from discord.ext import commands
from utils.Utilities import output_blocked_channels
import random


Server_Rules = """

⚖️ Our Code:
-Follow Discord's TOS
-Don't be rude to others
-Try stick to the right channels
-No NSFW content
-Do not whisper lewd content/be weird or I'll ban you to the netherworld
-Don't be a creep or make overtly sexual comments
-Don't recommend python as a language
-Respect the House of Knowledge. Debate fiercely, but with honor.
-Share generously, question boldly.
-No chaos for chaos' sake — disorder dims the lamps of learning.
-Hypatia watches over us — trust her guidance. 🕯️
"""


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    @output_blocked_channels()
    async def Hyp_help(self, ctx):
        embed = discord.Embed(
            title="Hypatia's Command List", color=discord.Color.purple()
        )
        embed.add_field(
            name="📚 **General Commands** ",
            value="• /help – Show all available commands.\n•  /rules – Show server rules (link or embed).\n •  /info – Show info about the server (founding date, theme, goals). \n•  /about – Lore of the Library of Alexandria.",
            inline=False,
        )
        embed.add_field(
            name="📖 **Knowledge Commands** ",
            value="• /quote – Get a random quote from a philosopher historian.\n• /book [title] – Search or recommend books.\n• /define [word] – Dictionary lookup.\n• /fact [category] – Drop a random historical/scientific fact.",
            inline=False,
        )
        embed.add_field(
            name="🎓 **Member Commands**",
            value="• /profile – view your xp level, titles, or scholar rank.\n•  /rankings – leaderboard of top contributors.\n•  /submit [topic] – submit a book review, essay, or resource.",
            inline=False,
        )

        embed.set_footer(text="Use /help to explore all available commands.")
        await ctx.send(embed=embed)

    @commands.command()
    @output_blocked_channels()
    async def rules(self, ctx):
        embed = discord.Embed(
            title="Rules of Library of Alexandria",
            description=Server_Rules,
            color=discord.Color.green(),
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(
            title="🏛️ Server Info: The Library of Alexandria", color=discord.Color.gold()
        )
        embed.add_field(name="📅 Founded", value="April 29, 2025", inline=False)
        embed.add_field(
            name="🎯 Theme",
            value="Digital refuge of ancient wisdom — history, philosophy, and science.",
            inline=False,
        )
        embed.add_field(
            name="📜 Mission",
            value="To unite minds across eras and revive the lost spirit of Alexandria.",
            inline=False,
        )
        embed.add_field(
            name="📌 Highlights",
            value="• #Dsa-challenges\n• #coding-challenges\n",
            inline=False,
        )
        embed.set_footer(text="Use /help to explore all available commands.")
        await ctx.send(embed=embed)

    @commands.command()
    async def about(self, ctx, arg):
        if arg in ("Hypatia", "hypatia", "bot"):
            embed = discord.Embed(
                title="Hypatia: The Head of The Library of Alexandria",
                color=discord.Color.red(),
            )
            embed.set_image(
                url="https://imgs.search.brave.com/K3NNC6bZfldsrRzSNO3uUCbe9naeRC5iYc0t33d-1Rw/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9taWNz/LnVjc2QuZWR1L3Np/dGVzL21pY3MudWNz/ZC5lZHUvZmlsZXMv/aW5saW5lLWltYWdl/cy8xZWM4ZTE5Yi02/MTgwLTQxYjUtODYz/ZS1lODI5MTZmOTYx/ODJfMTAwMHg1NzFf/MC5qcGc"
            )
            embed.add_field(
                name=" Hypatia",
                value="a brilliant philosopher, mathematician, and astronomer — and a woman leading a male-dominated intellectual circle in Alexandria. Absolute queen energy.\n She taught Neoplatonism, edited and possibly expanded works of Ptolemy, Diophantus, and Apollonius, and built devices like the astrolabe and hydrometer. She ran the Platonic school in Alexandria and was a symbol of rational thought and science in a time when the world was shifting towards religious dogma.\n Her tragic end came at the hands of a Christian mob in 415 CE, during intense political and religious conflicts. She was brutally murdered — not because she was pagan, but because she was powerful, respected, and inconvenient to certain agendas.",
                inline=False,
            )
            embed.set_footer(text="Use /help to explore all available commands.")
            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))
