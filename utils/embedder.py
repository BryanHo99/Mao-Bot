from typing import Optional, Union
from discord import Embed, Colour, embeds


def build_embed(
        title: str,
        description: Optional[str] = None,
        footer: Optional[str] = None,
        url: embeds.EmptyEmbed = embeds.EmptyEmbed,
        colour: Colour = Colour.orange(),
        image: Optional[str] = None,
        thumbnail: Optional[str] = None,
) -> Embed:
    """
    Helper method that builds a Discord embed.
    Colour is defaulted to orange because much wow.
    """
    return Embed(
        title=title,
        description=description,
        footer=footer,
        url=url,
        colour=colour,
        image=image,
        thumbnail=thumbnail
    )
