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
#700141579528306759
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        JoinLog = self.client.get_channel(700141579528306759)
        #await JoinLog.send(f'{guild.name} has added WolfBot to their server!')
        log = discord.Embed(
            title = f'**{guild.name} has added WolfBot to their server!**',
            color = discord.Color.blue(),
            #description = f'Requested by\n{ctx.message.author.mention}',
        )
        log.set_thumbnail(url = guild.icon_url)
        await JoinLog.send(embed = log)
        #print('We have logged in as {0.user}'.format(self.client))
        

def setup(client):
    client.add_cog(Events(client))
