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

class Wolfsay(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Ping
    @commands.command()
    async def wolfsay(self, ctx, *, msg):
        length = len(msg)
        message = '```                       '
        for i in range(length):
            message += '_'
        message += ''
        message += '\n                      <' + msg + '>\n '
        message += '                      '
        for i in range(length):
            message += '-'
        message += '\n                          /'
        message += '\n                     .'
        message += '\n                    / V\\'
        message += '\n                  / `  /'
        message += '\n                 <<   |'
        message += '\n                 /    |'
        message += '\n               /      |'
        message += '\n             /        |'
        message += '\n           /    \\  \\ /'
        message += '\n          (      ) | |'
        message += '\n  ________|   _/_  | |'
        message += '\n<__________\______)\\__)'
        message += '```'
        await ctx.send(message)


    @cog_ext.cog_slash(
    name="wolfspeak",
    description="WolfBot says what you tell him to while revealing his true f0rm",
    options=[manage_commands.create_option(
        name = "msg",
        description = "thing you want WolfBot to say",
        option_type = 3,
        required = True
    )]
    )
    async def _wolfspeak(self, ctx, msg: str):
        length = len(msg)
        message = '```                       '
        for i in range(length):
            message += '_'
        message += ''
        message += '\n                      <' + msg + '>\n '
        message += '                      '
        for i in range(length):
            message += '-'
        message += '\n                          /'
        message += '\n                     .'
        message += '\n                    / V\\'
        message += '\n                  / `  /'
        message += '\n                 <<   |'
        message += '\n                 /    |'
        message += '\n               /      |'
        message += '\n             /        |'
        message += '\n           /    \\  \\ /'
        message += '\n          (      ) | |'
        message += '\n  ________|   _/_  | |'
        message += '\n<__________\______)\\__)'
        message += '```'
        await ctx.send(message)
def setup(client):
    client.add_cog(Wolfsay(client))
