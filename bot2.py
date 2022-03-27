# bot.py
import os
import random
import krak

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = ('BOT-TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(">krak"):
        name = message.content.split(" ", 1)[1]
        await message.channel.send(krak.getlink(name))

# @client.event
# async def on_message(message):
#     if message.content.startswith('>clear'):
#         await message.channel.send("Clearing!!...")
#         await message.channel.purge()

client.run(TOKEN)