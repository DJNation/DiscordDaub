import discord
import random
import asyncio
#import requests
from discord import Game
from discord.ext.commands import Bot
import os
import nltktest
from nltktest import *

BOT_PREFIX = ("?", "!") #Bot prefixes
TOKEN = 'NDMxMjA3NzcwNDk5NDQ4ODMy.DabZMQ.GPEv11wl_oMhEVhw9QtvZiAO7g4' #Bot specific "secret" token
client = Bot(command_prefix=BOT_PREFIX) #Bot only respeonds to given prefixes

#Medieval Parser
@client.command(name='medieval', 
                description="Ye ole English",
                brief="Here ye!",
                aliases=['yeOle', 'king', 'jest', 'olde'],
                pass_context = True)
async def medieval(ctx):
    msg = ctx.message.content.split(" ", 1)
    if len(msg) > 1: #Change to a 'try' later
        print(msg)
        await client.delete_message(ctx.message)
        await client.send_message(ctx.message.channel, nltktest.medieval(str(msg[1])))
    else: #Change to catch/exception
        print('Empty message handled: ' + str(msg))
        await client.delete_message(ctx.message)
        x = ''
        return await client.send_message(ctx.message.channel, 'You must enter a message, ' + nltktest.postpend(x))

#img command
@client.command(pass_context = True)
async def img(ctx):

<<<<<<< HEAD
        imgList = os.listdir("/home/pi/DiscordDaub/Daubs/") # Creates a list of filenames from your folder

        imgString = random.choice(imgList) # Selects a random element from the list

        path = "/home/pi/DiscordDaub/Daubs/" + imgString # Creates a string for the path to the file
=======
        imgList = os.listdir("/home/pi/DiscordDaub/Daubs") # Creates a list of filenames from your folder

        imgString = random.choice(imgList) # Selects a random element from the list

        path = "/home/pi/DiscordDaub/Daubs" + imgString # Creates a string for the path to the file
>>>>>>> 11d8e5eba7a96817e9bbfe82f322410b2df821e0

        await client.send_file(ctx.message.channel, path) # Sends the image in the channel the command was used

#hello command
@client.command(pass_context = True)
async def hello(context):
    await client.say('Hello, '+ context.message.author.mention + ', check out my show OnlyInJapan @ http://onlyinjapan.tv/')

#magic 8ball command
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'Yes.',
        'No.',
        'What a dumb question.',
        'Better not tell you now...',
        'Without a doubt.',
        'As I see it, yes.',
        'Outlook good.'
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

#square command
@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

#Change game played by bot, logs the terminal
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Only in Japan TV!"))
    print("Logged in as " + client.user.name)

#Lists bot's active servers
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

#Loops active servers
client.loop.create_task(list_servers())
#Launches bot
client.run(TOKEN)
