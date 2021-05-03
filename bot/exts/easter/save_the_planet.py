import json
from pathlib import Path

from discord import Embed
from discord.ext import commands

from bot.bot import Bot
from bot.utils.randomization import RandomCycle


with Path("bot/resources/easter/save_the_planet.json").open('r', encoding='utf8') as f:
    EMBED_DATA = RandomCycle(json.load(f))


class SaveThePlanet(commands.Cog):
    """A cog that teaches users how they can help our planet."""

    @commands.command(aliases=('savetheearth', 'saveplanet', 'saveearth'))
    async def savetheplanet(self, ctx: commands.Context) -> None:
        """Responds with a random tip on how to be eco-friendly and help our planet."""
        return_embed = Embed.from_dict(next(EMBED_DATA))
        await ctx.send(embed=return_embed)


def setup(bot: Bot) -> None:
    """Load the Save the Planet Cog."""
    bot.add_cog(SaveThePlanet())
