#!/usr/bin/python3
# Bot entry point
import discord
import os
from discord.ext import commands, tasks

import BotToken
from paths import cogs_path

from discord_slash import SlashCommand
from discord_slash.utils import manage_commands # Allows us to manage the command settings.

client = commands.Bot(command_prefix = '.')
slash = SlashCommand(client, sync_commands=True)
client.remove_command('help')

@client.command()
async def load(ctx, extension):
    if(ctx.message.author.id == 570812427944329216):
        client.load_extension(f'cogs.{extension}')
        await ctx.channel.purge(limit = 1)
    else:
        await ctx.send("Bark off, I only take orders from my master. Woof.")

@client.command()
async def unload(ctx, extension):
    if(ctx.message.author.id == 570812427944329216):
        client.unload_extension(f'cogs.{extension}')   
        await ctx.channel.purge(limit = 1)
    else:
        await ctx.send("Bark off, I only take orders from my master. Woof.")

@client.command()
async def reload(ctx, extension):
    if(ctx.message.author.id == 570812427944329216):
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.channel.purge(limit = 1)
    else:
        await ctx.send("Bark off, I only take orders from my master. Woof.")

for filename in os.listdir(cogs_path):
#for filename in os.listdir('./cogs'): ## windows
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[: -3]}')

client.run(BotToken.token_str)
