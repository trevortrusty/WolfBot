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

from paths import img_path, kernel_path
import re
import csv
from functions import wrap_wolf
import exceptions

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
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))
        
    @commands.command()
    @commands.has_any_role('Admin', 'Bot Henchmen', 'Development Team', 'testing')
    async def bark(self, ctx,*, script):
        async with ctx.typing():
            try:
                export = wrap_wolf(script)

                # Evaluate given expression, exporting result as png
                eval = await asyncio.wait_for(session.evaluate_wrap(wlexpr(export)), 40)

                # Check for errors before sending result
                log = str(eval.messages)

                # Remove any (' and ') from error messages
                if  '(\'' in log and ('\')' in log or '\',)' in log):
                    log.replace('(\'', '')
                    log.replace('\')', '')

                # Determine output when there's a wolfram error
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
                        ##################enlarge()
                        await ctx.send(file=discord.File(img_path))
                        await ctx.send(embed = log) 
                else:
                    # No errors, continue
                    # Send image from Wolfram calculation results
                    await ctx.send(file=discord.File(img_path))

            except exceptions.WhiteListError as error:
                await ctx.send(error.message)
            except exceptions.BlackListError as error:
                await ctx.send(error.message)
            except asyncio.TimeoutError:
                await ctx.send(embed = embeds.time_error)

            await session.evaluate(wlexpr('ClearAll["Global`*"]'))
            embeds.tail_message.description = f'Requested by\n{ctx.message.author.mention}'
            await ctx.send(embed = embeds.tail_message)

    @commands.command()
    @commands.has_any_role('Admin', 'Bot Henchmen', 'Development Team')
    async def stop(self, ctx):
        session.terminate()


    # Ping
    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)
        if bot_latency <= 50:
            meter = discord.Color.green()
        elif bot_latency < 100:
            meter = discord.Color.gold()
        elif bot_latency >= 100:
            meter  = discord.Color.red()
        elif bot_latency >= 500:
            meter = discord.Color.dark_grey()

        ping_embed = discord.Embed(
            title = f'Woof! {bot_latency} ms',
            color = meter
        )
        ping_embed.set_footer(text = f'requested by {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed = ping_embed)

def setup(client):
    client.add_cog(Bark(client))
