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

from paths import img_path, kernel_path, file
import re
import csv
from functions import wrap_wolf
import exceptions

from discord_slash import SlashCommand
from discord_slash.utils import manage_commands # Allows us to manage the command settings.
from discord_slash import cog_ext, SlashContext

session = WolframLanguageAsyncSession(kernel_path)
session.start()

guild_ids = [662383643385135165]

class Bark(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['w', 'wl', 'WL', 'run', 'woof', 'howl'])
    # @commands.has_any_role('Admin', 'Bot Henchmen', 'Development Team', 'testing')
    async def bark(self, ctx,*, script):
        async with ctx.typing():
            script = script.replace('```', '')
            try:
                # Set Up Whitelist using string of Wolfram code, only allowed functions specified here are able to execute (see WOLFRAM_WHITELIST.txt for formatted text for the following string)
                code = 'WHITELIST = {List, CompoundExpression, Set, SetDelayed, Blank, Pattern, Real, Complex, Hold, Sin, Cos, Plus, Times, Power, Log, Symbol, Integer, N, NIntegrate, Integrate, D, ReplaceAll, Rule, Style, FontFamily, Background, Plot, Graphics}; SetAttributes[whit, HoldFirst]; whit[REPLACE_] := Block[{i, k}, If[Length[Flatten[List[DeleteMissing[DeleteDuplicates[Evaluate[Map[Head, Level[Hold[REPLACE], {0, Infinity}]]/.Table[WHITELIST[[i]] -> Missing[], {i, Length[WHITELIST]}]] /. Missing[][u__] -> {u}]]]]] > 0, "Grrr, banned function(s)! " <> ToString[DeleteMissing[DeleteDuplicates[Evaluate[Map[Head, Level[Hold[REPLACE], {0, Infinity}]]] /.Table[WHITELIST[[k]] -> Missing[], {k, Length[WHITELIST]}] /. Missing[][u__] -> {u}]]], REPLACE]];'
                await session.evaluate(wlexpr(code))
                export = wrap_wolf(script)

                # Evaluate given expression, exporting result as png
                eval = await asyncio.wait_for(session.evaluate_wrap(wlexpr(export)), 40)

                # Check for errors before sending result
                log = str(eval.messages)

                # Remove any (' and ') from error messages
                if  '(\'' in log and ('\')' in log or '\',)' in log):
                    log = log.replace('(\'', '')
                    log = log.replace('\')', '')

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
                        if 'Animate' not in script:
                            await ctx.send(file=discord.File(img_path))
                        else:
                            await ctx.send(file=discord.File(f'{file}/output/output.gif'))
                        await ctx.send(embed = log) 
                else:
                    # No errors, continue
                    # Send image from Wolfram calculation results
                    if 'Animate' not in script:
                        await ctx.send(file=discord.File(img_path))
                    else:
                        await ctx.send(file=discord.File(f'{file}/output/output.gif'))

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
    async def stop(self, ctx):
        if(ctx.message.author.id == 570812427944329216):
            session.terminate()
            exit()
        else:
            await ctx.send("Bark off, I only take orders from my master. Woof.")

def setup(client):
    client.add_cog(Bark(client))
