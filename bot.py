import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os

client = discord.Client ()
Client = commands.Bot (command_prefix = "+")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="+help | By MegaPig"))
    print("Bot Is Ready")

   
@client.event
async def on_message(message):
    if message.content.startswith('ניר'):
        await client.send_message(message.channel, """זה עבד""")

client.run(osgetenv("TOKEN"))
