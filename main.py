import discord

client = discord.Client()

@client.event
async def on_ready():
  print('{0.user}.format(client) is ready!')