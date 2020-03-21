import discord
from discord.ext import commands

import supersecret
import re


BOT_TOKEN = supersecret.getSecret('discord_bot_ctfbot', 'bot_token')

NAME = "ctfbot#9398"
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith("!describe") and message.author != NAME:
            category_m = re.findall("!describe ([a-zA-Z0-9-]+)", message.content)
            if len(category_m) < 1:
                return
            category_name = category_m[0]
            for category in message.guild.categories:
                print(category.name)
                if category.name == category_name:
                    print("category object", repr(category))
                    result = await category.edit(position=1)
        elif message.content.startswith("!solved") and message.author != NAME:
            name = message.channel.name
            if not name.startswith("✅-"):
                result = await message.channel.edit(name="✅-" + name)
        elif message.content.startswith("!unsolved") and message.author != NAME:
            name = message.channel.name
            if name.startswith("✅-"):
                result = await message.channel.edit(name=name[2:])
        elif message.content.startswith("!help") and message.author != NAME:
            result = await message.channel.send("Commands supported: !help, !unsolved, !solved")
client = MyClient()
client.run(BOT_TOKEN)
