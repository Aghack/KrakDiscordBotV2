# Hydra
import os
import random
import krak as krakservice

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from dotenv import load_dotenv

load_dotenv()
TOKEN = ('BOT-TOKEN')

client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.command()
async def krak(ctx, arg: str):
    # if message.author == client.user:
    #     return

    # if message.content.startswith(">krak"):
        #name = arg.split(" ", 1)[1]
        await ctx.channel.send(krakservice.getlink(arg))

@client.command()
async def clear(ctx):
        await ctx.channel.send("Clearing!!...")
        await ctx.channel.purge()

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has kicked.')

@client.command()
@commands.has_any_role(702909770956406885, 545323952428417064, 545323570587369472)
async def invite(ctx, member: discord.Member):
    await member.invite()
    await ctx.send(f'Invited {member}.')

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has Banned.')

@client.command()
@commands.has_any_role(920005842483417138, 545323952428417064, 545323570587369472)
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_user:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title="Unbanned", description=f"{user.mention} Has been Unbanned!", color=discord.Color.green())
            await ctx.send(embed=embed)
            return

client.run(TOKEN)
