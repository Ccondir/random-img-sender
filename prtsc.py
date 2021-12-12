import random
import time
import discord

a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9"]
b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9"]
c = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9"] 
d = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9"]
e = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9"]
f = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9"]

def mejn():
    client = discord.Client()
    @client.event
    async def on_ready():
        print ("yep, it do be workin as: {0.user}".format(client))
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith("&help"):
            await message.channel.send("""`&help` - show help
    `&prntsc` - show random print screen
    ||Bot created by Ccondir#0556 and Perchant#2178||
            """)
        if message.content.startswith("&prntsc"):
            await message.channel.send("https://prnt.sc/"+random.choice(a)+random.choice(b)+random.choice(c)+random.choice(d)+random.choice(e)+random.choice(f))
    client.run("your token here")

for i in range(999999):
    mejn()
    time.sleep(1)
