import discord
import os
from discord.ext import commands, tasks
from collections import defaultdict
from discord.utils import get

from wolframclient.evaluation import WolframLanguageSession, WolframLanguageAsyncSession
from wolframclient.language import wl, wlexpr
from wolframclient.evaluation import SecuredAuthenticationKey, WolframCloudSession
from wolframclient.exception import WolframEvaluationException, WolframLanguageException, WolframKernelException
from PIL import Image
import PIL.ImageOps 
import asyncio
import embeds
from  cogs._bark import session
from cogs.paths import img_path, kernel_path

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events

    
    #### Commands ####
        
    @commands.command()
    async def help(self, ctx):
        # await ctx.send('USELESS TEST HELP MESSAGE')
        await ctx.send(embed = embeds.help_message)
        # await ctx.send(embeds.__file__)

def setup(client):
    client.add_cog(Help(client))