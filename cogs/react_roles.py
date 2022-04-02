from discord.ext import commands
from discord import Embed


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
        channel = self.bot.get_channel(959713149098020864)
        react_roles_embed = await self.get_react_roles_embed()
        special_roles_embed = await self.get_special_roles_embed()

        await channel.send(embed=react_roles_embed)
        await channel.send(embed=special_roles_embed)

    async def get_react_roles_embed(self):
        """
        Get react role embed.
        Any member can react to subscribe to these roles.
        """
        description = self.get_react_roles_description()
        embed = Embed(title="Notification Roles", description=description)
        return embed

    async def get_special_roles_embed(self):
        """
        Get special role embed.
        Description of special roles given to certain members within the server.
        """
        description = self.get_special_roles_description()
        embed = Embed(title="Special Roles", description=description)
        return embed

    @staticmethod
    def get_react_roles_description():
        return f"""
        React the following roles to be notified for games.
        A bot schedule system is planned to be implemented in the future
        which will mention these roles.
        
        ⚔ <@&959713387959418991>: Get this role to be notified for Dota games.
        🏔 <@&959713202155974677>: Get this role to be notified for Genshin games.
        """

    @staticmethod
    def get_special_roles_description():
        return f"""
        💠 <@&959795082708520980>: Exclusive role for the Bunch of maos gang.
        🔧 <@&959713538782400542>: Contributors of the Mao Bot.
        """
