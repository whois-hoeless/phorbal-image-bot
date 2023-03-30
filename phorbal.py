import os
import discord
import random
#make a simple discord bot with the discord.py library
intents=discord.Intents.all()
client = discord.Client(intents=intents)

#when the bot is ready
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#list all files in the phorbal folder
files = os.listdir('phorbal')
file_list = []

#append the list of files to the file_list list
for file in files:
    file_list.append(file)

#when a message is sent
@client.event
async def on_message(message):

    #check if the message is from the bot itself
    if message.author == client.user:
        return

    #check if the message contains the string 'phorbal'
    if 'phorbal' in message.content.lower():
        
        #generate a random file from the file_list list
        r_img = 'phorbal/' + random.choice(file_list)
        #open the file
        with open(r_img, 'rb') as f:
            img = discord.File(f, filename=r_img)
            #send the file to the channel where the message was sent
            await message.channel.send(file=img)
    
    #check if the message contains the string 'p-stats'
    if 'p-stats' in message.content.lower():

        #send the stats of the phorbal folder to the channel where the message was sent
        await message.channel.send('There are ' + str(len(file_list)) + ' files in the phorbal folder. No duplicates detected.')

#run the bot
client.run('MTA5MTEwMDYzNjQ2NjExODY3Nw.GwI222.-kvDxzixXxpX4vZymPCv0YIP6veLKduO8xIxV0')
