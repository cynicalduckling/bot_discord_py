import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
  print('logged in')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(message.content)
    # reply = "i know responses ar appreciated"

    # await message.channel.send(content = reply)

client.run(os.getenv('BOT_TOKEN'))  # your bot token goes here
