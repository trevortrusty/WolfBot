import discord
from discord.ext import commands, tasks

class Staff(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events

    
    #### Commands ####

    # Echo
    @commands.command()
    @commands.has_any_role('Owners','Moderator', 'Admin')
    async def echo(self, ctx, *, message): ## Repeats message given by user calling the command
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'{message}')

    # Kick
    @commands.command()
    @commands.has_any_role('Owners','Moderator', 'Admin')
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)

    # Ban
    @commands.command()
    @commands.has_any_role('Owners','Moderator', 'Admin')
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)

    # Clear
    @commands.command()
    @commands.has_any_role('Owners','Moderator', 'Admin')
    async def clear(self, ctx, quantity=2): # 2 as default, because this number includes the command message
        await ctx.channel.purge(limit=quantity+1) # adding 1 so the message including the command isn't part of the amount. Future fix?: Purge without the command being deleted

    # Unban
    @commands.command()
    @commands.has_any_role('Owners','Moderator', 'Admin')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                return

def setup(client):
    client.add_cog(Staff(client))