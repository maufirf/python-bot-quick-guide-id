import discord

from key_loader import GENERAL_ACCESS_TOKEN as TKN

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global on_watch_users
    # Prevents recursive parsing
    if message.author == client.user:
        return

    # Checks if the message is a "ping", will reply with "pong" if it is
    if message.content.lower().startswith('ping'):
        await message.channel.send("Pong!")

client.run(TKN.DISCORD.value)