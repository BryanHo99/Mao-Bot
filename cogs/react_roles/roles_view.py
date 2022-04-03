from abc import ABC, abstractmethod

from utils.embedder import build_embed


class RolesView(ABC):
    def __init__(self, title):
        self.title = title
        self.description = self.get_description()

    async def get_embed(self):
        """
        Get a Discord embed.
        """
        embed = build_embed(title=self.title, description=self.description)
        return embed

    @staticmethod
    @abstractmethod
    def get_description():
        return ""
