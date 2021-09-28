import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!inspect'):
        mess_list = message.content.split(" ")
        player = mess_list[1]
        armory_link = f"https://ironforge.pro/?player={player}"
        await message.channel.send(armory_link)

    if message.content.startswith('!investigate'):
        mess_list = message.content.split(" ")
        instance = mess_list[1]
        instance_link = f"https://tbc.wowhead.com/{instance}"
        await message.channel.send(instance_link)

client.run(os.environ['TOKEN'])
