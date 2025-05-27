# Simple bot that will return a random beatmap within a certain star rating
# This will take quite a while, but hopefully it will be working just fine
# by the end of the summer.
# will ask people for help, they will be credited at the end.

# osu!rand ver. 1.0.0 Started On July 17th, 2020
# Last edited on July 18th, 2020

import discord
import random # the key to victory is in random.... aha..
import os

from discord.ext import commands # of course, super important when we're creating commands

client = commands.Bot(command_prefix = '$') # idk but maybe use ! or smth too

# simple online message (next 3 lines)
@client.event
async def on_ready():
    # await client.change_presence(activity=discord.Game(name='osu!')
    print('osu!rand is online!')

# straightforward
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

# straightforward
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

# fake working system lol ( {round(client.latency * 1000)} ms )
num1 = random.randint(0,297933)

@client.command(aliases=['getmap', 'findmap'])
async def rand(ctx):
    await ctx.send(f'`Finding Beatmap... `')
    await ctx.send(f'osu!rand has found a random beatmap for you!\nhttps://osu.ppy.sh/beatmapsets/{num1}#osu/{random.randint(0,num1)}  ( {round(client.latency * 1000)} ms )')

num3 = random.randint(0,100000)
@client.command(aliases=['getplayer', 'findplayer'])
async def randplayer(ctx):
    await ctx.send(f'`Finding Random Player... `')
    await ctx.send(f'osu!rand has found a random player for you!\nhttps://osu.ppy.sh/users/{num3}  ( {round(client.latency * 1000)} ms )')

# just some fun osu wisdom
@client.command(aliases=['q', '8ball'])
async def wisdom(ctx, *, question):
    response = ['yes, without a doubt',
                'although unsure, i think the outcome will be positive'
                'bruh just click circles lol wut idk how to answer that',
                'okay, i MIGHT sound toxic but i dont care',
                'nah, just straight up nah',
                'no. there is no conceivable way that is happening']
    await ctx.send(f'{random.choice(response)}')


# not sure if this is necessary but idk
# yah, this is all unnecessary
# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f'cogs.{extension})
#
# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f'cogs.{extension})
#
# for filename in os.listdir('./cogs')
#     if file.endswith('.py'):
#         client.load_extension(f'cogs.{filename[]}'')

client.run('NzMzODUzNTY2NTM1NzI5MTUz.XxJ5Eg.g3Wka3GQ9PwJtFhSYLOL4EW9NG0')
