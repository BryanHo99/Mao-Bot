from discord.ext import commands
from discord.ext.commands import Bot, Context
from discord.utils import get, find
from discord import RawReactionActionEvent

import config
from cogs.react_roles.special_roles_view import SpecialRolesView
from cogs.react_roles.react_roles_view import ReactRolesView


class ReactRolesCog(commands.Cog, name="React Roles"):
    """
    Cog that allows members to react to get certain roles.
    Currently planned to have reacts for Dota and Genshin.
    """
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot
        self.react_roles = ReactRolesView()
        self.special_roles = SpecialRolesView()

    @commands.command(name="react-roles")
    @commands.has_role(config.BOT_DEV_ROLE_ID)
    async def react_roles(self, ctx: Context):
        """
        Setup react role embeds in "react-roles" channel.
        Please update REACT_ROLES_MESSAGE_ID in .env and rebuild the bot after calling this command.
        """
        channel = self.bot.get_channel(config.REACT_ROLES_CHANNEL_ID)
        await channel.purge()

        react_roles_embed = await self.react_roles.get_embed()
        special_roles_embed = await self.special_roles.get_embed()

        # Send embeds to "react-roles" channel.
        react_roles_message = await channel.send(embed=react_roles_embed)
        await channel.send(embed=special_roles_embed)

        # Pre-add the emojis that members can react to.
        await react_roles_message.add_reaction(self.react_roles.dota_emoji)
        await react_roles_message.add_reaction(self.react_roles.genshin_emoji)

        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: RawReactionActionEvent):
        message_id = payload.message_id
        if message_id == config.REACT_ROLES_MESSAGE_ID:
            member = payload.member
            emoji = str(payload.emoji)
            guild_id = payload.guild_id
            guild = find(lambda g: g.id == guild_id, self.bot.guilds)
            role = None

            if member.id == config.MAO_BOT_ID:
                return

            if emoji == self.react_roles.dota_emoji:
                role = get(guild.roles, id=config.DOTA_ROLE_ID)
            elif emoji == self.react_roles.genshin_emoji:
                role = get(guild.roles, id=config.GENSHIN_ROLE_ID)

            if role is not None:
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: RawReactionActionEvent):
        message_id = payload.message_id

        if message_id == config.REACT_ROLES_MESSAGE_ID:
            emoji = str(payload.emoji)
            guild_id = payload.guild_id
            guild = find(lambda g: g.id == guild_id, self.bot.guilds)
            role = None

            if emoji == self.react_roles.dota_emoji:
                role = get(guild.roles, id=config.DOTA_ROLE_ID)
            elif emoji == self.react_roles.genshin_emoji:
                role = get(guild.roles, id=config.GENSHIN_ROLE_ID)

            member = await guild.fetch_member(payload.user_id)

            if role is not None and member is not None:
                await member.remove_roles(role)
