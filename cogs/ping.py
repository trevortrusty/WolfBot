import discord
import os
from discord.ext import commands, tasks
from collections import defaultdict
from discord.utils import get

import embeds

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Ping
    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)
        if bot_latency <= 50:
            meter = discord.Color.green()
        elif bot_latency < 100:
            meter = discord.Color.gold()
        elif bot_latency >= 100:
            meter  = discord.Color.red()
        elif bot_latency >= 500:
            meter = discord.Color.dark_grey()

        ping_embed = discord.Embed(
            title = f'Woof! {bot_latency} ms',
            color = meter
        )
        ping_embed.set_footer(text = f'requested by {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed = ping_embed)

def setup(client):
    client.add_cog(Ping(client))
