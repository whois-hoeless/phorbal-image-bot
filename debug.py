import os
import discord
import time
#make a simple discord bot with the discord.py library
intents=discord.Intents.all()
client = discord.Client(intents=intents)



# IMPORTANT

ID = 000000000000000000
folder = 'phorbal'

# put  the folder name in which you have the images stored
# and the channel ID of the channel in which you want to store the images
# this can be just some random test server with a channel..
# you just can't delete the channel else the pictures should get deleted off of discord servers

# Then you just need to type "send_imgs" in the channel and it will start sending the images and saving the links to phorbalurl.txt
# the links will get loaded into RAM and will get saved after the process has finished


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

files = os.listdir(folder)
file_list = []


for file in files:
    file_list.append(file)

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if 'send_imgs' in message.content.lower():
        count = 1
        
        with open('phorbalurl.txt', 'w') as f:
            for file in file_list:
                with open(f'{folder}/' + file, 'rb') as j:
                    img = discord.File(j, filename=file)
                    await message.channel.send(file=img)

                chan = client.get_channel(ID)
                message = await chan.fetch_message(chan.last_message_id)
            

                f.write(f'{message.attachments[0].url}\n')
                print('saved ' + message.attachments[0].url + f' count: {count}/808')
                time.sleep(3) # 3 seconds seemed fine, I did not get any rate limit errors
                count+=1
        f.close()
        print('Done')
                    
                
client.run('TOKEN')
