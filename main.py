import os
import discord
import requests
import json
import re

TOKEN = os.environ['TOKEN']
APIKEY = os.environ['APIKEY']
client = discord.Client()

def get_price():
  response = requests.get('https://api.twelvedata.com/price?symbol=AMC&apikey=' + APIKEY)
  data = json.loads(response.content)
  return(float(data['price']))

@client.event
async def on_ready():
  print('{0.user}'.format(client) + ' is ready!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$amc'):
    if '-s' in message.content:
      stocks = re.findall(r'\d+', message.content)
      price = get_price() * int(stocks[0])
    else:
      price = get_price()

    await message.channel.send('$' + "{:.2f}".format(price))

client.run(TOKEN)