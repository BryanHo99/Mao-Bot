from discord import Embed
from abc import ABC, abstractmethod


class RolesView(ABC):
    def __init__(self, title):
        self.title = title
        self.description = self.get_description()

    async def get_embed(self):
        """
        Get a Discord embed.
        """
        embed = Embed(title=self.title, description=self.description)
        return embed

    @staticmethod
    @abstractmethod
    def get_description():
        return ""
