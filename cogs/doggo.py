import discord
import os
from discord.ext import commands, tasks
from collections import defaultdict
from discord.utils import get
from random import randint

class Doggo(commands.Cog):

    def __init__(self, client):
        self.client = client

    gifs = [
        1 : 'https://tenor.com/view/king-mirella-doggo-happy-massage-gif-12450202',
        2 : 'https://tenor.com/view/dog-nose-boop-massage-gif-11159084',
        3 : 'https://tenor.com/view/cf-bepis-show-fire-evil-gif-14758874',
        4 : 'https://tenor.com/baumT.gif',
        5 : 'https://tenor.com/view/pizza-dog-dogs-happy-delighted-gif-4088893',
        6 : 'https://tenor.com/view/wolf-gif-8325560',
        7 : 'https://tenor.com/view/rest-wolf-sleeping-gif-5469684',
        8 : 'https://tenor.com/view/doggo-good-gamer-mcdonalds-puppy-gif-14662701',
        9 : 'https://tenor.com/view/doggo-puppers-goldens-gif-7550362',
    ]

    @commands.command()
    # @commands.has_any_role('Admin', 'Bot Henchmen', 'Development Team', 'testing')
    async def doggo(self, ctx):
        async with ctx.typing():
            x = gifs[randint(1,9)]
            embed = discord.Embed()
            embed.set_image(url= x)
            await ctx.send(embed = embed)

                


def setup(client):
    client.add_cog(Doggo(client))
