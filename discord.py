import discord
import time
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix = "!j")
botstatus = {1 , 0}

@client.event
async def on_ready():
    print('{0.user}'.format(client))

@client.event
async def on_message(message):
    if botstatus == 1:
        client.send_Message(message.author,'Bot bakımda!')

    if message.author == client.user:
        return

    if message.content.startswith('bmamb'):
        await client.send_message(message.channel, content="image \n Buna benzeyen arkadaşı diyorsun herhalde.")

    if message.content.startswith('!nc'):
        await client.change_nickname(message.author,"bmamb")

    elif message.content.startswith('!status'):
        await client.change_status(game=discord.Game(name="Tracking Bmamb"))

    elif message.content.startswith('!uppy'):
        await client.send_message(message.channel, time.clock())


client.run(' key:) ')

