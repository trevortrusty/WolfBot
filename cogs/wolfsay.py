import discord
import os
from discord.ext import commands, tasks
from collections import defaultdict
from discord.utils import get

import embeds

class Wolfsay(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Ping
    @commands.command()
    async def wolfsay(self, ctx, *, str):
        length = len(str)
        message = '```                       '
        for i in range(length):
            message += '_'
        message += ''
        message += '\n                      <' + str + '>\n '
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
