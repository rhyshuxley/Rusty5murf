import os
import discord
import requests
import json

TOKEN = os.environ['TOKEN']
APIKEY = os.environ['APIKEY']
client = discord.Client()

def get_price():
  response = requests.get('https://api.twelvedata.com/price?symbol=AMC&apikey=' + APIKEY)
  data = json.loads(response.content)
  return(data['price'])

@client.event
async def on_ready():
  print('{0.user}'.format(client) + ' is ready!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$amc'):
    await message.channel.send('$' + get_price())

client.run(TOKEN)