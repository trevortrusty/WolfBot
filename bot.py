#!/usr/bin/python3

import discord
import os
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '$')
client.remove_command('help')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.channel.purge(limit = 1)
    
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.channel.purge(limit = 1)

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.channel.purge(limit = 1)

for filename in os.listdir('./cogs'):
#for filename in os.listdir('./cogs'): ## windows
    if filename.endswith('.py') and filename.startswith('_'):
        client.load_extension(f'cogs.{filename[: -3]}')

client.run('NjUzODA3MTM3NjkyMTg4Njcy.Xe8Xlg.-EDzSXrTejAAuJ2sCI-0mfwUxjY')
