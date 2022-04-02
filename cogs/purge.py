from discord.ext import commands
from discord.ext.commands.errors import MissingRole, MissingAnyRole


class PurgeCog(commands.Cog, name="Purge"):
    """
    Cog that clears the entire text channel.
    Command should only be granted to Bot Devs.
    """
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="purge")
    @commands.has_role(959713538782400542)
    async def purge(self, ctx):
        """
        Clear entire text channel.
        """
        await ctx.channel.purge()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        Event is triggered when MissingRole error is invoked.
        """
        if isinstance(error, (MissingRole, MissingAnyRole)):
            await ctx.send("You do not have access to this command.")
