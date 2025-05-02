import discord
from discord.ext import commands
from utils.Utilities import output_blocked_channels


Bot_Commands = """
📚 **General Commands**
/help – Show all available commands.
/rules – Show server rules (link or embed).
/info – Show info about the server (founding date, theme, goals).
/about – Lore of the Library of Alexandria.

📖 **Knowledge Commands**
/quote – Get a random quote from a philosopher historian.
/book [title] – Search or recommend books.
/define [word] – Dictionary lookup.
/fact [category] – Drop a random historical/scientific fact.

🎓 **Member Commands**
/profile – View your XP level, titles, or scholar rank.
/rankings – Leaderboard of top contributors.
/submit [topic] – Submit a book review, essay, or resource.
"""


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    @output_blocked_channels()
    async def Hyp_help(self, ctx):
        embed = discord.Embed(
            title="Hypatia's command index",
            description=Bot_Commands,
            color=discord.Color.purple(),
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))
