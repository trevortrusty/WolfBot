import discord
import os
from discord.ext import commands, tasks
from collections import defaultdict
from discord.utils import get

import embeds

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Say
    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(message)

def setup(client):
    client.add_cog(Fun(client))
