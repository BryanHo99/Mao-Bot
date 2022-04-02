# Dependencies
from discord.ext import commands


# Local imports
from cogs.chat import ChatCog
from cogs.react_roles import ReactRolesCog
from cogs.purge import PurgeCog


class MaoBot(commands.Bot):
    def __init__(self, command_prefix="!"):
        super().__init__(command_prefix=command_prefix)

        self.add_cog(ChatCog(self))
        self.add_cog(ReactRolesCog(self))
        self.add_cog(PurgeCog(self))
