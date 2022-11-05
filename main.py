import os
import random
import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents = intents)

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

TIPS = ["Drink more water!", "Eat more protein!", "Remember to use proper form!"]

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == 'tip':
    response = random.choice(TIPS)
    await message.channel.send(response)

client.run(TOKEN)