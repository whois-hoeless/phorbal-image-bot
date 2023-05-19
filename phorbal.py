import discord
import random
from replit_keep_alive import keep_alive  #Credits in replit_keep_alive.py

intents=discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

file_list = []

with open('phorbalurl.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        file_list.append(line)
    f.close()


@client.event
async def on_message(message):

    #check if the message is from the bot itself
    if message.author == client.user:
        return

    #check if the message contains the string 'phorbal'
    if 'phorbal' in message.content.lower():
        
        #generate a random file from the file_list list
        linkie = random.choice(file_list)
        await message.channel.send(linkie)
    
    #check if the message contains the string 'p-stats'
    elif 'p-stats' in message.content.lower():

        #send the stats of the phorbal folder to the channel where the message was sent
        await message.channel.send('There are ' + str(len(file_list)) + ' files in the phorbalurl.txt. No duplicates detected.')

#run the bot
#keep_alive() #<- Uncomment this line if you want to host the bot on replit.com
client.run('TOKEN')
