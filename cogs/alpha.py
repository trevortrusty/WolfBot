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
        
    @commands.command()
    # @commands.has_any_role('Admin', 'Bot Henchmen', 'Development Team')
    async def alpha(self, ctx,*, query):
        # Prepares the user input to be passed into Wolfram functions that export the output image, and limit the time of the computation 
        async with ctx.typing():
            # begin = f'Export["{img_path}", Style['
            # end = ', Large]]'
            # export = begin + query + end

            try:
                '''old method'''
                # # Evaluate given expression, exporting result as png
                # # eval = await asyncio.wait_for(session.evaluate_wrap(wlexpr(export)), 40)
                # graphic = wl.WolframAlpha(query, "FullOutput")
                # png_export = wl.Export(img_path, graphic, "PNG")
                
                # eval = await asyncio.wait_for(session.evaluate(png_export), 40)
                # # enlarge()
                # await ctx.send(file=discord.File(img_path))
                '''new method'''
                send = f'Export["{file}/output/alpha.jpg", WolframAlpha["{query}", "FullOutput", TimeConstraint -> {E, .45, .45, .45}, Asynchronous -> All]]'
                await asyncio.wait_for(session.evaluate(send), 10)
            except Exception:
                await ctx.send(embed = embeds.time_error)

            await ctx.send(file=discord.File(f'{file}/output/alpha.jpg'))
            embeds.tail_message.description = f'Query by\n{ctx.message.author.mention}'
            await ctx.send(embed = embeds.tail_message)


def setup(client):
    client.add_cog(Alpha(client))