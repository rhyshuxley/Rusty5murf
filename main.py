import discord

client = discord.Client()

@client.event
async def on_ready():
  print('{0.user}.format(client) is ready!')

@client.event
async def on_message(message):
  if message.authro == client.user:
    return

  if message.content.startswith('$hello')
    await message.channel.send('Hey!')