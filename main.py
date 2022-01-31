import os
import discord
import requests
import json
import re
from keep_alive import keep_alive

TOKEN = os.environ['TOKEN']
APIKEY = os.environ['APIKEY']
client = discord.Client()

def get_price(symbol):
  response = requests.get('https://api.twelvedata.com/price?symbol=' + symbol + '&apikey=' + APIKEY)
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
      price = get_price('AMC') * int(stocks[0])
    else:
      price = get_price('AMC')

    await message.channel.send('$' + "{:.2f}".format(price))

  if message.content.startswith('$gme'):
    if '-s' in message.content:
      stocks = re.findall(r'\d+', message.content)
      price = get_price('GME') * int(stocks[0])
    else:
      price = get_price('GME')

    await message.channel.send('$' + "{:.2f}".format(price))

keep_alive()
client.run(TOKEN)