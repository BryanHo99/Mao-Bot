from discord import Member
from discord.ext import commands
from discord.ext.commands import Context, Bot


class ChatCog(commands.Cog, name="Chat"):
    """
    Cog for bot chatting.
    Say hi to the bot...
    """
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="hello")
    async def hello(self, ctx: Context, member: Member=None):
        """
        Hello there...
        """
        member = member or ctx.author
        await ctx.send(f"Hello there, {member.mention}.")
