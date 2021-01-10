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
from  cogs.bark import session
from paths import img_path, kernel_path

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events

    
    #### Commands ####
        
    @commands.command()
    async def help(self, ctx, command = 'none'):
        # await ctx.send('USELESS TEST HELP MESSAGE')
        async with ctx.typing():
            if command == 'none':
                await ctx.send(embed = embeds.help_message)
            elif command == 'bark':
                await ctx.send('```.bark <Wolfram Code>```')
            elif command == 'alpha':
                await ctx.send('```.alpha <Wolfram Alpha Query>```')
            elif command == 'docs':
                await ctx.send('```.docs <Search keyword in the Wolfram Documentation```')
            #elif command == 'prob':
                #await ctx.send('```.prob <math topic>```')
        # await ctx.send(embeds.__file__)

    

def setup(client):
    client.add_cog(Help(client))
