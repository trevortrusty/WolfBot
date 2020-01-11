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
                await ctx.send('Nothing here')
            elif command == 'alpha':
                await ctx.send('Nothing here')
            elif command == 'docs':
                await ctx.send('Nothing here')
        # await ctx.send(embeds.__file__)

    @commands.command()
    async def docs(self, ctx, query = 'none'):
        async with ctx.typing():
            if query == 'none':
                await ctx.send('Please enter a search term, using the syntax `\docs <search term>` (e.g. `\docs Plot`, `\docs integration`).')
            else:
                if query.lower() in ['plot', 'integrate', 'plot3d']:
                    link = f'https://reference.wolfram.com/language/ref/{query.capitalize()}.html'
                else:
                    link = f'https://reference.wolfram.com/search/?q={query}'
                embed = discord.Embed(
                    title = f'Online Wolfram Documentation: \'{query}\'',
                    color = discord.Color.dark_teal(),
                    url = link
                )
                embed.set_footer(text = f'requested by {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Help(client))