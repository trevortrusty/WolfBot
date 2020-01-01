#!/usr/bin/python3

import discord
import os
from discord.ext import commands, tasks
from collections import defaultdict
from discord.utils import get

from wolframclient.evaluation import WolframLanguageSession, WolframLanguageAsyncSession
from wolframclient.language import wl, wlexpr
from wolframclient.evaluation import SecuredAuthenticationKey, WolframCloudSession
from wolframclient.exception import WolframEvaluationException
from wolframclient.exception import WolframKernelException
from PIL import Image

# Tracemelloc
import tracemalloc

tracemalloc.start()

# Is wolf bot running in server already?
inuse = False

# Authentication Key
sak = SecuredAuthenticationKey(

    't9JwbVPeUiX0G38n8/GtrLcz0S1vXrTiNfvHbNFl5U0=',

    'dbbLmj8rDSrTEe0A+baPcMIFgFhmVPfFMdLg4trDuFc=')
#

# Enlarges image output from Wolfram calculation, and then saves as png #
def enlarge():
    img = Image.open('D:/dev/discordbots/WolfBot/output/output.jpg', 'r')
    img_w, img_h = img.size
    if img_w < 100:
        background = Image.new('RGB', (img_w + 125, img_h), (255, 255, 255, 255))
        bg_w, bg_h = background.size
        background.paste(img,(15,12))
        background.save('D:/dev/discordbots/WolfBot/output/output.jpg')

    img = Image.open('D:/dev/discordbots/WolfBot/output/output.jpg', 'r')
    if img_h < 40:
        background = Image.new('RGB', (img_w, 40), (255, 255, 255, 255))
        bg_w, bg_h = background.size
        background.paste(img,(15,12))
        background.save('D:/dev/discordbots/WolfBot/output/output.jpg')

# Creates a discord.Embed object #
def createEmbed(t):
    # Embed message
    embed = discord.Embed(
        title = t)
    return embed

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def wolf(ctx, inuse=inuse):
    channel = ctx.message.channel
    def check(m):
        return m.channel == channel

    # #Handle any user attempting to use bot while the kernel is in use in another process already
    # try:
    #     #session = WolframLanguageSession('D:\\Program Files\\Wolfram Research\\Wolfram Engine\\12.0\\WolframKernel.exe')
    #     session = WolframLanguageAsyncSession('D:\\Program Files\\Wolfram Research\\Wolfram Engine\\12.0\\WolframKernel.exe')
    # except WolframKernelException:
    #     error_message = createEmbed('WolfBot already in use by another user!')
    #     await ctx.send(embed = error_message)

    # session.start()
    async with WolframLanguageAsyncSession('D:\\Program Files\\Wolfram Research\\Wolfram Engine\\12.0\\WolframKernel.exe') as session:
        await session.start()
        begin = 'Export["D:/dev/discordbots/WolfBot/output/output.jpg",'
        end = ']'

        n = 0

        # Embed message
        in_message = createEmbed(f'**In[{n}]:=**')
        await ctx.send(embed = in_message)
        
        msg = await client.wait_for('message', check = check)
        export = begin + msg.content + end
        while msg.content != 'exit' :
            if msg.content != 'exit':
                try:
                    async with ctx.typing():
                        await session.evaluate(wlexpr(export))
                        #enlarge()
                        out_message = createEmbed(f'**Out[{n}]:=**')
                        await ctx.send(embed = out_message)
                        await ctx.send(file=discord.File('D:/dev/discordbots/WolfBot/output/output.jpg'))
                    n = n + 1
                    in_message = createEmbed(f'**In[{n}]:=**')
                    await ctx.send(embed = in_message)
                    msg = await client.wait_for('message', check = check)
                    export = begin + msg.content + end
                except WolframEvaluationException as err:
                    await ctx.send('Evaluation error: ', err)
        # session.terminate()
        await session.stop()
    # Send Embed message for end of session #
    end_message = discord.Embed(
        title = f'**Wolfram session terminated!**', 
        color = discord.Color.blue(), 
        description = f'Session started by\n{ctx.message.author.mention}')
    await ctx.send(embed = end_message)

client.run('NjUzODA3MTM3NjkyMTg4Njcy.Xe8Xlg.-EDzSXrTejAAuJ2sCI-0mfwUxjY')




