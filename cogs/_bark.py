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
from cogs.paths import img_path, kernel_path


# Enlarges image output from Wolfram calculation, and then saves as png #
def enlarge():
    img = Image.open(img_path, 'r')
    img_w, img_h = img.size

    background = Image.new('RGB', (img_w + 25, img_h + 25), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    background.paste(img,(13,12))
    final = PIL.ImageOps.invert(background)
    final.save(img_path)

session = WolframLanguageAsyncSession(kernel_path)
session.start()

class Bark(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    #### Commands ####

    # Echo
    @commands.command()
    @commands.has_any_role('Owners','Moderator', 'Admin')
    async def echo(self, ctx, *, message): ## Repeats message given by user calling the command
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'{message}')
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))
        
    @commands.command()
    @commands.has_any_role('Admin', 'Bot Henchmen', 'Development Team')
    async def bark(self, ctx,*, script):
        # Prepares the user input to be passed into Wolfram functions that export the output image, and limit the time of the computation 
        async with ctx.typing():
            # begin = f'Export["{img_path}", Style['
            # end = ', Large]]'
            # export = begin + script + end
            export = f'Export["{img_path}", Style[{script}, Large]]
            try:
                # Evaluate given expression, exporting result as png
                eval = await asyncio.wait_for(session.evaluate_wrap(wlexpr(export)), 40)

                # Check for errors before sending result
                log = str(eval.messages)

                if log != 'None':
                    if(len(log) > 256):
                        await ctx.send(embed = embeds.general_error)
                    elif (log).startswith('(\'Invalid syntax'):
                        await ctx.send(embed = embeds.syntax_error)
                    elif log.startswith('(\'Not enough memory available to rasterize Notebook expression.\',)'):
                        await ctx.send(embed = embeds.memory_error)
                        await ctx.send(f'```{await session.evaluate_wrap(wlexpr(script), timeout = 5)}```')
                    else:
                        log = embeds.createEmbed(log)
                        enlarge()
                        await ctx.send(file=discord.File(img_path))
                        await ctx.send(embed = log) 
                else:
                    # No errors, continue
                    enlarge()
                    # Send image from Wolfram calculation results
                    await ctx.send(file=discord.File(img_path))
            except Exception:
                await ctx.send(embed = embeds.time_error)

            embeds.tail_message.description = f'Requested by\n{ctx.message.author.mention}'
            await ctx.send(embed = embeds.tail_message)

    @commands.command()
    @commands.has_any_role('Admin', 'Bot Henchmen', 'Development Team')
    async def stop(self, ctx,*, script):
        session.terminate()


    # Ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Woof! {round(self.client.latency *1000)} ms')

def setup(client):
    client.add_cog(Bark(client))