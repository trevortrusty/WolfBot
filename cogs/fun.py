import discord
import os
from discord.ext import commands, tasks
from collections import defaultdict
from discord.utils import get

import embeds

from discord_slash import SlashCommand
from discord_slash.utils import manage_commands # Allows us to manage the command settings.
from discord_slash import cog_ext, SlashContext

guild_ids = [662383643385135165]

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Say
    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(message)

    # Say
    @commands.command()
    async def test(self, ctx):
        await ctx.send(file='output/output.gif')

    # Slash Versions
    @cog_ext.cog_slash(
    name="say",
    description="WolfBot will literally just repeat your message",
    options=[manage_commands.create_option(
        name = "message",
        description = "yes",
        option_type = 3,
        required = True
    )]
    )
    async def _say(self, ctx, message: str):
        await ctx.send(message)

def setup(client):
    client.add_cog(Fun(client))
