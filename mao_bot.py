# Dependencies
from discord.ext import commands


# Local imports
from src.cogs.chat import ChatCog


class MaoBot(commands.Bot):
    def __init__(self, command_prefix="!"):
        super().__init__(command_prefix=command_prefix)

        self.add_cog(ChatCog(self))
