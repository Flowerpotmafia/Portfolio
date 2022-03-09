import discord
import random
from discord import channel 
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

token = 'ODY2NDg4NzEyMjI1NzUxMDkz.YPTSfw.AWZOqc7U0Gz8hBh6mjYKVCYa0U8'

#PING PONG Command
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

#8Ball command
@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    responses =   [ 'It is certian.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes - definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    "Don't count on it.",
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#On ready event
@client.event
async def on_ready():

    general_channel = client.get_channel(707471350809362463)
    #await general_channel.send("What's up homies")

    print('Bot is ready')

#Fuck you nerd event THIS BREAKS COMMANDS WHEN IT IS UNCOMMENTED/IMPLEMENTED NOT SURE WHY
# @client.event
# async def on_message(message):

#     fuck_you_nerd_channel = client.get_channel(868352527748440104)

#     if message.content != "Fuck you nerd" and message.channel == fuck_you_nerd_channel:        
#         await fuck_you_nerd_channel.send("Fuck you nerd")
       


#Run the bot on the server
client.run(token)