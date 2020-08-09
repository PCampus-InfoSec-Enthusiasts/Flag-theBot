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
    
    print(f'{client.user} is online.\nHurray')
    # print(f'Connected in server {guild.name} -> id:{guild.id}')

    # members = ', '.join([member.name for member in guild.members])
    # print(f'The members in the server are {members}')

@client.event 
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, welcome to the Discord server.'
    )

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content.split()

    # print(msg[0])

    if msg[0] != 'baje' and msg[0] != 'baaje':
        return
        
    # print(message)

    msg = msg[1:]

    # print(msg)


    response = msgchecker(msg)
    await message.channel.send(response)

client.run(TOKEN)