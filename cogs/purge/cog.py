from discord.ext import commands
from discord.ext.commands import Bot, Context

import config


class PurgeCog(commands.Cog, name="Purge"):
    """
    Cog that clears the entire text channel.
    Command should only be granted to Bot Devs.
    """
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="purge")
    @commands.has_role(config.BOT_DEV_ROLE_ID)
    async def purge(self, ctx: Context):
        """
        Clear entire text channel.
        """
        await ctx.channel.purge()


