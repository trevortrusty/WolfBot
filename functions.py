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
    with open(wl_path, 'r') as f:
        reader = csv.reader(f)
        whitelist = list(reader)[0]
    with open(bl_path, 'r') as f:
        reader = csv.reader(f)
        blacklist = list(reader)[0]    


    pattern = r"([A-Z]{1,2}[a-z]+'*)\[.*?"
    functions = re.findall(pattern, s)

    allow = True
    for function in functions:
        if function not in whitelist:
            allow = False
            raise exceptions.WhiteListError(function)
            break
    
    for phrase in blacklist:
        if phrase in s:
            raise exceptions.BlackListError(phrase)
            break

    if 'Animate' not in s:
        return f'Export["{img_path}", Style[{s}, Large], Background -> None]'
    else:
        return f'Export["{file}/output/output.gif", {s}]'
    #, ImageResolution -> 100
