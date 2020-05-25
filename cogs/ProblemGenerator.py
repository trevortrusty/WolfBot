##
#  Problem Generator Cog for GodsAperture's Wolfram Problem Generator
##

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
from paths import img_path, kernel_path, file
from functions import crop
import exceptions

class ProblemGenerator(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    pFile = open(f'{file}/ProblemGeneratorScript.txt')
    script = pFile.read()

    @commands.command(aliases = ['problemgenerator', 'Problem', 'prob', 'Prob'])
    async def problem(self, ctx,*, subject, script = script):
        # Prepares the user input to be passed into Wolfram functions that export the output image, and limit the time of the computation 
        async with ctx.typing():
            await session.evaluate(script)
            await session.evaluate(f'Export["{file}/output/problemgen.jpg", Prob[{subject}]]')

            # await crop()
            await ctx.send(file=discord.File(f'{file}/output/problemgen.jpg'))

           
            #embeds.tail_message.description = f'Requested by\n{ctx.message.author.mention}'
            #await ctx.send(embed = embeds.tail_message)
            
                

def setup(client):
    client.add_cog(ProblemGenerator(client))