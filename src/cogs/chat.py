from discord.ext import commands
from discord import Member


class ChatCog(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="hello")
    async def hello(self, ctx, member: Member=None):
        """Hello there..."""
        member = member or ctx.author
        await ctx.send(f"Hello there, {member.mention}")
