from discord.ext import commands

from cogs.chat.cog import ChatCog
from cogs.react_roles.cog import ReactRolesCog
from cogs.purge.cog import PurgeCog
from cogs.errors.cog import ErrorsCog


class MaoBot(commands.Bot):
    def __init__(self, command_prefix="!"):
        super().__init__(command_prefix=command_prefix)

        self.add_cog(ChatCog(self))
        self.add_cog(ReactRolesCog(self))
        self.add_cog(PurgeCog(self))
        self.add_cog(ErrorsCog(self))
