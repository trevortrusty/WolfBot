 #!/usr/bin/python3

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

#Define paths
img_path = 'D:/dev/discordbots/WolfBot/output/output.jpg'
#img_path = '/home/pi/WolfBot/output/output.jpg'
kernel_path = 'D:/Program Files/Wolfram Research/Wolfram Engine/12.0/WolframKernel.exe'
#kernel_path = '/opt/Wolfram/WolframEngine/12.0/Executables/WolframKernel'

# Authentication Key
sak = SecuredAuthenticationKey(

    't9JwbVPeUiX0G38n8/GtrLcz0S1vXrTiNfvHbNFl5U0=',

    'dbbLmj8rDSrTEe0A+baPcMIFgFhmVPfFMdLg4trDuFc=')
#

# Enlarges image output from Wolfram calculation, and then saves as png #
def enlarge():
    img = Image.open(img_path, 'r')
    img_w, img_h = img.size

    background = Image.new('RGB', (img_w + 25, img_h + 25), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    background.paste(img,(13,12))
    final = PIL.ImageOps.invert(background)
    final.save(img_path)

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

session = WolframLanguageAsyncSession(kernel_path)
session.start()

@client.command()
@commands.has_any_role('Admin', 'Bot Henchmen', 'Development Team')
async def bark(ctx,*, script):
    # Prepares the user input to be passed into Wolfram functions that export the output image, and limit the time of the computation 
    async with ctx.typing():
        begin = f'Export["{img_path}", TimeConstrained[Style['
        end = ', Large], 60, "Your computation has exceeded one minute."]]'
        export = begin + script + end

        #await session.start()
        try:
            eval = await session.evaluate_wrap(wlexpr(export), timeout= 5)

            # Check for errors before sending result
            log = str(eval.messages)

            if len(log) > 256:
                #log = log[0 : 255 : 1] # Shorten length of string to 255 characters to satify discord embed char limit
                log = 'Errors were detected during computation'
            if log != 'None':
                if (log).startswith('(\'Invalid syntax'):
                    log = createEmbed('Invalid syntax!')
                    await ctx.send(embed = log)
                else:
                    log = createEmbed(log)
                    enlarge()
                    await ctx.send(file=discord.File(img_path))
                    await ctx.send(embed = log) 
            else:
                # No errors, continue
                enlarge()
                
                # Send image from Wolfram calculation results
                await ctx.send(file=discord.File(img_path))
        except TimeoutError:
            log = createEmbed('Timeout Error: Computation took too long!')
            await ctx.send(embed = log)

        # Send Goodbye Embed message
        end_message = discord.Embed(
            title = f'**Learn more the about Wolfram Language**',
            color = discord.Color.blue(),
            description = f'Requested by\n{ctx.message.author.mention}',
            url = 'https://reference.wolfram.com/language/')
        end_message.set_thumbnail(url = 'https://media1.tenor.com/images/ed4da9a1bdbd4ff952638b19afa96506/tenor.gif?itemid=12660466')
        await ctx.send(embed = end_message)
        #await session.stop()

client.run('NjUzODA3MTM3NjkyMTg4Njcy.Xe8Xlg.-EDzSXrTejAAuJ2sCI-0mfwUxjY')



