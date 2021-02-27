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

    @cog_ext.cog_slash(
    name="ping",
    description="tells you WolfBot's latency"
    )
    async def _ping(self, ctx):
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
        ping_embed.set_footer(text = f'requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed = ping_embed)

def setup(client):
    client.add_cog(Ping(client))
