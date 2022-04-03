from discord.ext import commands

import config
from cogs.react_roles.special_roles_view import SpecialRolesView
from cogs.react_roles.react_roles_view import ReactRolesView


class ReactRolesCog(commands.Cog, name="React Roles"):
    """
    Cog that allows members to react to get certain roles.
    Currently planned to have reacts for Dota and Genshin.
    """
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Print react role embeds once bot is ready
        """
        channel = self.bot.get_channel(config.BOT_SPAM_CHANNEL_ID)
        react_roles_embed = await ReactRolesView().get_embed()
        special_roles_embed = await SpecialRolesView().get_embed()

        await channel.send(embed=react_roles_embed)
        await channel.send(embed=special_roles_embed)
