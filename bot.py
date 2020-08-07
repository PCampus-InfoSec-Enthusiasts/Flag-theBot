import os

import discord
from dotenv import load_dotenv

from msgcheck import msgchecker

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} is online.\nHurray!')
    print(f'Successfully connected to server {guild.name} -> id:{guild.id}')

    # members = ', '.join([member.name for member in guild.members])
    # print(f'The members in the server are {members}')

@client.event 
async def on_member_join(member):
    guild = discord.utils.get(client.guilds, name=GUILD)
    await member.create_dm()
    await member.dm_channel.send(
        f"Hello {member.name}, welcome to {guild.name}. I am glad you are here! Type 'baje help' to see all the commands I can follow. Let's go!"
    )

@client.event 
async def on_message(message):
    msg_parts = message.content.lower().split()
    
    if message.author == client.user:
        return
    
    if msg_parts[0] != 'baaje' or msg_parts[0] != 'baje':
        return
    
    # msg = msg_parts[1:].split()

    response = msgchecker(msg_parts[1:])
    await message.channel.send(response)

client.run(TOKEN)
