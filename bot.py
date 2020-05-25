#!/usr/bin/python3
# Bot entry point
import discord
import os
from discord.ext import commands, tasks

import BotToken
from paths import cogs_path

client = commands.Bot(command_prefix = '##')
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

for filename in os.listdir(cogs_path):
#for filename in os.listdir('./cogs'): ## windows
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[: -3]}')

client.run(BotToken.token_str)
