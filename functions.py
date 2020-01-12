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

class WhiteListError(Exception):
    def __init__(self, bad = 0):
        if bad:
            self.message = f'{bad} is not currently in our list of allowed functions! Please contact the dev team to have it added'
        else:
            self.message = 'This function is not currently allowed! Please contact the dev team to have it added'

def wrap_wolf(s):
    if s == "bad":
        raise WhiteListError
    wrapped f'Export["{img_path}", Style[{s}, Large], Background -> None, ImageResolution -> 100]'
    return wrapped
