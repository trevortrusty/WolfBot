import discord
import os
from discord.ext import commands, tasks
from collections import defaultdict
from discord.utils import get


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))
        

def setup(client):
    client.add_cog(Events(client))
