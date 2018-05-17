import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
@asyncio.coroutine
def on_ready():
    print("Bot is ready!")

@client.event
@asyncio.coroutine
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")
    if message.content.lower().startswith("!test"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Dit is een test, " % (userID))
    if message.content.lower().startswith("!say"):
        if message.author.id == "283554212019699722":
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "Je hebt hier geen permissies voor!")
    if message.content.lower().startswith("!speel"):
        if message.author.id == "283554212019699722":
            args = message.content.split(" ")
            await client.send_message(message.channel, " ".join(args[1:]))
            await client.change_presence(game=discord.Game(name=" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "Je hebt hier geen permissies voor!")
    if message.content.lower().startswith("!create"):
        userID = message.author.id
        server = message.server
        args = message.content.split(" ")
        await client.create_channel(server, (" ".join(args[1:]).replace(" ", "-")), type=discord.ChannelType.text)
        await client.send_message(message.channel, "Je hebt " % (" ".join(args[1:])) % "gemaakt!")

client.run("NDExNTQ2MDgzODQwMjI5Mzg3.DaFJ5w.5wVQUDbv68RxU4k21i1gUXy8Ezc")
