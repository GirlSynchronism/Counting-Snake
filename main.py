import discord
import os
from keep_alive import keep_alive

#from vars import counter
#from vars import counting
#count = int(1)
#counting = bool(False)
client = discord.Client()
client.counter = 1
client.counting = False
client.highscore = 0
client.channelnum = 0

@client.event
async def on_ready():
    print('ready')

@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return
  elif message.content.startswith("count;start"):
     client.counting = True
     client.channelnum = message.channel
     client.counter = 1
     await message.channel.send("Counting start!")
  elif message.content.startswith("count;invite"):
     await message.channel.send("https://discord.com/api/oauth2/authorize?client_id=821053587475529749&permissions=67648&scope=bot")
  elif message.content.startswith("count;stop") and client.channelnum == message.channel:
     client.counting = False
     await message.channel.send("Counting end! You counted to: " + str(client.counter - 1))
     print(client.counter)
     print(client.highscore)
     if (client.counter-1 > client.highscore):
         client.highscore = client.counter-1
     await message.channel.send("Local highscore is: " + str(client.highscore))
     client.counter = 1
  elif (client.counting == False and msg == "1"):
     client.counting = True
     client.counter = 1
     client.counter = client.counter + 1
     await message.add_reaction('✅')
  elif (client.counting == True and msg == str(client.counter) and client.channelnum == message.channel):
     client.counter = client.counter + 1
     await message.add_reaction('✅')
  elif (client.counting == True and msg != str(client.counter) and client.channelnum == message.channel):
     await message.add_reaction('❌')
     client.counting = False
     await message.channel.send("Counting end! You counted to: " + str(client.counter - 1))
     if (client.counter-1 > client.highscore):
         client.highscore = client.counter-1
     await message.channel.send("Local highscore is: " + str(client.highscore))
  elif client.counting == False:
    return

keep_alive()

client.run(os.getenv('TOKEN'))