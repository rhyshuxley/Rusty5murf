import os
import discord
import requests
import json
from keep_alive import keep_alive

TOKEN = os.environ['TOKEN']
APIKEY = os.environ['APIKEY']
client = discord.Client()

def get_price(symbol, amount):
  response = requests.get('https://api.twelvedata.com/price?symbol=' + symbol + '&apikey=' + APIKEY)
  data = json.loads(response.content)
  return(float(data['price']) * float(amount))

@client.event
async def on_ready():
  print('{0.user}'.format(client) + ' is ready!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$stock'):
    args = message.content.split()
    symbol = args[1]

    if len(args) == 3:
      amount = args[2]
    else:
      amount = 1

    await message.channel.send('$' + "{:.2f}".format(get_price(symbol, amount)))

keep_alive()
client.run(TOKEN)