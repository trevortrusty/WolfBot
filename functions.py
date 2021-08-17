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
# from  cogs.bark import session
from paths import file, img_path, kernel_path, wl_path, bl_path
import csv
import re
import exceptions

def wrap_wolf(s):
    if 'Animate' not in s:
        return f'Export["{img_path}", Style[whit[{s}], Large, FontFamily -> "Cambria"], Background -> None]'
    else:
        return f'Export["{file}/output/output.gif", whit[{s}]]'

# Enlarges image output from Wolfram calculation, and then saves as png #
async def enlarge(ctx):
    img = Image.open(img_path, 'r')
    img_w, img_h = img.size

    background = Image.new('RGB', (img_w + 25, img_h + 25), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    background.paste(img,(13,12))
    final = PIL.ImageOps.invert(background)
    final.save(img_path)

async def crop():
    img = Image.open(f'{file}/output/alpha.jpg', 'r')
    img_w, img_h = img.size
    if img_w < 100:
        raise exceptions.BadQuery
    else:
        # Setting the points for cropped image 
        left = 0
        top = 0
        # right = img_w - 440
        right = img_w / 1.77
        bottom = img_h
        
        # Cropped image of above dimension 
        # (It will not change orginal image) 
        final = img.crop((left, top, right, bottom))

        final.save(f'{file}/output/alpha.jpg')
