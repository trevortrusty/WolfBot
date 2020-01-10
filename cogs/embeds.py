import discord
import os
from discord.ext import commands, tasks
from collections import defaultdict
from discord.utils import get

# Creates a discord.Embed object #
def createEmbed(t):
    # Embed message
    embed = discord.Embed(
        title = t)
    return embed


# Invalid Syntax error
syntax_error = discord.Embed(
    title = 'Invalid syntax!'
)

# General errors in computation
general_error = discord.Embed(
    title = 'Errors were detected during computation'
)

# Not enough memory
memory_error = discord.Embed(
    title = 'Not enough memory available to rasterize Notebook expression.'
)

# Time error
time_error = discord.Embed(
    title = 'Timeout Error: Computation took too long!'
)

# Tail message
tail_message = discord.Embed(
    title = f'**Learn more the about Wolfram Language**',
    color = discord.Color.blue(),
    #description = f'Requested by\n{ctx.message.author.mention}',
    url = 'https://reference.wolfram.com/language/'
)
tail_message.set_thumbnail(url = 'https://media1.tenor.com/images/ed4da9a1bdbd4ff952638b19afa96506/tenor.gif?itemid=12660466')

# help
help_message = discord.Embed(
    title = 'Resting!'
)

