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


async def eval_input(script):
    export = f'Export["{img_path}", Style[{script}, Large]]'

    # Evaluate given expression, exporting result as png
    eval = await asyncio.wait_for(session.evaluate_wrap(wlexpr(export)), 40)

    # Check for errors before sending result
    log = str(eval.messages)
    return log

async def send_error(ctx, log):
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
        return 1
    else:
        return 0