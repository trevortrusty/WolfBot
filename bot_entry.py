##msg = await client.wait_for('message', check=check)

import discord
import os
from discord.ext import commands, tasks
from collections import defaultdict
from discord.utils import get

from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
from PIL import Image


def enlarge():
    img = Image.open('D:/dev/discordbots/WolfBot/output/output.png', 'r')
    img_w, img_h = img.size
    if img_w < 100 and img_h < 40:
        background = Image.new('RGBA', (100, 40), (255, 255, 255, 255))
        bg_w, bg_h = background.size
        # offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        # background.paste(img, offset)
        background.paste(img,(15,12))
        background.save('D:/dev/discordbots/WolfBot/output/output.png')


client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def wolf(ctx):
    channel = ctx.message.channel
    def check(m):
        return m.channel == channel

    session = WolframLanguageSession('D:\\Program Files\\Wolfram Research\\Wolfram Engine\\12.0\\WolframKernel.exe')
    
    begin = r'Export["D:\\dev\\discordbots\\WolfBot\\output\\output.png",'
    end = ']'
    
    counter = 0
    await ctx.send(f'```In[{counter}]:=    ```')
    msg = await client.wait_for('message', check = check)
    export = begin + msg.content + end
    while msg.content != 'exit' :
        if msg.content != 'exit':
            async with ctx.typing():
                session.evaluate(export)
                enlarge()
                await ctx.send(file=discord.File('D:\dev\discordbots\WolfBot\output\output.png'))
            #await ctx.send(f'```Out[{counter}]:= {(session.evaluate(wlexpr(msg.content)))}```')
            counter = counter + 1
            await ctx.send(f'```In[{counter}]:=    ```')
            msg = await client.wait_for('message', check = check)
            export = begin + msg.content + end
    session.terminate()
    await ctx.send('>>> Wolfram session terminated!')

client.run('NjUzODA3MTM3NjkyMTg4Njcy.Xe8Xlg.-EDzSXrTejAAuJ2sCI-0mfwUxjY')




