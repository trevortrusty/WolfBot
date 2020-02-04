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

#Enlarges image output from Wolfram calculation, and then saves as png #
def enlarge():
    img = Image.open(img_path, 'r')
    img_w, img_h = img.size

    background = Image.new('RGB', (img_w + 25, img_h + 25), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    background.paste(img,(13,12))
    final = PIL.ImageOps.invert(background)
    final.save(img_path)

# session = WolframLanguageSession(kernel_path)
# session.start()

class Alpha(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases = ['fetch', 'awoo', 'beg', 'wa', 'WA'])
    # @commands.has_any_role('Admin', 'Bot Henchmen', 'Development Team')
    async def alpha(self, ctx,*, query):
        # Prepares the user input to be passed into Wolfram functions that export the output image, and limit the time of the computation 
        async with ctx.typing():
            if not '-link ' in query:
                try:
                    '''new method'''
                    send = f'Export["{file}/output/alpha.jpg", WolframAlpha["{query}", ' + '"FullOutput", Asynchronous -> All, AppearanceElements -> {"Pods"}, IncludePods -> {"Input", "Result", "BasicInformation:PeopleData", "Image:PeopleData", "IndefiniteIntegral", "Plot", "DefiniteIntegral", "VisualRepresentationOfTheIntegral", "PartialSums"}]]'
                    
                    await asyncio.wait_for(session.evaluate(send), 40)
                    await crop()
                    await ctx.send(file=discord.File(f'{file}/output/alpha.jpg'))
                except asyncio.TimeoutError:
                    await ctx.send(embed = embeds.time_error)
                except Exception as err:
                    await ctx.send(f'Error: {err}')
            else:
                q = query
                q = q.replace('-link', '')
                q = q.strip()
                q.replace(' ', '+')
                send = f'https://www.wolframalpha.com/input/?i={q}'
                link = discord.Embed(
                    title = 'Click for Wolfram Online Result',
                    url = send
                )
                await ctx.send(embed = link)
            embeds.tail_message.description = f'Query by\n{ctx.message.author.mention}'
            await ctx.send(embed = embeds.tail_message)
                
                

def setup(client):
    client.add_cog(Alpha(client))