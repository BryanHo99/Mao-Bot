from discord.ext import commands
from discord.ext.commands import Context, Bot
from discord.ext.commands.errors import MissingRole, MissingAnyRole


class ErrorsCog(commands.Cog, name="Errors"):
    """
    Cog that listens to all exceptions.
    """
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error: Exception):
        """
        Event is triggered when MissingRole error is invoked.
        """
        if isinstance(error, (MissingRole, MissingAnyRole)):
            await ctx.send("You do not have access to this command.")
