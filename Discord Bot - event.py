import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

client = discord.Client ()
Client = commands.Bot (command_prefix = "+")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="+help | By MegaPig"))
    print("Bot Is Ready")

   
@client.event
async def on_message(message):
    if message.content.startswith('+info'):
        await client.send_message(message.channel, """Hello! My name is MegaBot!
I have 3 types of commands:
**Information Commands**
**General Commands**
**Staff Commands**
For see all the commands type: __+help__""")

    if message.content.startswith('+creator'):
        await client.send_message(message.channel, """**My Creator Is MegaPig#1576!**
__If you see bug in the bot say to him!__
__And you can ask him for support!__""")
        await client.send_message(client.get_channel('log'), 'hello')
        await client.add_reaction('\U0001F44D')
        
    if message.content.startswith('+invite'):
        await client.send_message(message.channel, """https://discordapp.com/api/oauth2/authorize?client_id=459490391146627073&permissions=8&scope=bot
__You Can Invite Me When Ever You Want!__
You Can Help If You Say Bugs To My Creator- **MegaPig#1576**""")

    if message.content.startswith('+help'):
        embed = discord.Embed(title="Command List", description="""
__**Information Commands**__

**+info** - Small Information Of The Bot.
**+invite** - The Bot Invite Link.
**+creator** - The Bot Creator.

__**General Commands**__

**+avatar @tag** - The avatar of the member.
**+servericon** - the picture of the server.
**+servers** - how many servers the bot in.
**+question (שאלת כן ולא)** - The Bot answear to you.

__**Staff Commands**__

**+warn** @TAG- warn member (move members permission)
**+mute** @TAG- mute member (mute members permission)
**+clear (2-100)** - clear messages (manage_messages permission)
**+kick** @TAG - kick member (kick members permission)
**+ban** @TAG - ban member (ban members permission)
""", color=0xe88af4)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('תצעק'):
        await client.send_message(message.channel, "האהאהאההאהאהאהאהאהאהאהאאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאההאאהאההאהההאהאהאהאהאהאאהאהאהאהאהאהאאהאאאהאאאהאהאהאאהאההאהאאההאהאאהאהאהאהאאהאהאהאהאהאהאהאאהאהאהאהאהאאהאהאהאהאהאהאאהאהאהאהאאהאהאהאהאאהאהאהאהאהאהאהאהאההאההאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאההאהאהאאהאהאהאהאההאאהאהאהאהאהאהאהאהאהאהאאהאהאהאהאאההאאהאהאהאהאהאהאהאהאהאאאהאהאהאהאהאהאהאהאהאהה")

                      
client.run("NDU5NDkwMzkxMTQ2NjI3MDcz.Dg29_w.dxSVxwf0G-iJlCzckdcVlItfCu8")
