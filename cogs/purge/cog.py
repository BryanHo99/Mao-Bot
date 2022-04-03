from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands.errors import MissingRole, MissingAnyRole

import config


class PurgeCog(commands.Cog, name="Purge"):
    """
    Cog that clears the entire text channel.
    Command should only be granted to Bot Devs.
    """
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="purge")
    @commands.has_role(config.BOT_DEV_ROLE_ID)
    async def purge(self, ctx: Context):
        """
        Clear entire text channel.
        """
        await ctx.channel.purge()

    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error: Exception):
        """
        Event is triggered when MissingRole error is invoked.
        """
        if isinstance(error, (MissingRole, MissingAnyRole)):
            await ctx.send("You do not have access to this command.")
