import discord
from discord.ext import commands
from utils.Utilities import ANNOUNCEMENT_CHANNEL


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Welcome new members with an embed in the announcement channel."""

        self.channel = self.bot.get_channel(ANNOUNCEMENT_CHANNEL)
        print(f"Target Channel: {self.channel}")  # Debugging line
        if self.channel:
            embed = discord.Embed(
                title=f"Welcome {member.mention}!",
                description=f"to the {member.guild.name}!",
            )
            embed.set_thumbnail(url=member.avatar.url)
            await self.channel.send(embed=embed)
        else:
            print("Announcement channel not found.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.channel.send(f"{member.name} has left")

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f"hello {member.name}.")
        else:
            await ctx.send(f"Hello {member.name}... this feels familiar.")
        self._last_member = member

    # test
    @commands.command()
    async def fjoin(self, ctx):
        await self.on_member_join(ctx.author)

    @commands.command()
    async def fleave(self, ctx):
        await self.on_member_remove(ctx.author)


async def setup(bot):
    await bot.add_cog(Welcome(bot))
