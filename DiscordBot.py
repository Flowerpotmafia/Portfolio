import discord
import random
from discord import channel 
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

token = 'ENTER TOKEN HERE'

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

       


#Run the bot on the server
client.run(token)
