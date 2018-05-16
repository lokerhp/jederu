import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import yaml


path = "voorbeelden.yaml"

def load_yaml(path):
    with open(path, "r") as file:
        voorbeelden = yaml.load(file)
        voorbeelden = voorbeelden.get('voorbeelden').get('events')
        voorbeelden_events_1 = voorbeelden[1]
        voorbeelden_events_2 = voorbeelden[2]
        voorbeelden_events_3 = voorbeelden[3]
    with open(path, "r") as file:
        voorbeelden = yaml.load(file)
        voorbeelden = voorbeelden.get('voorbeelden').get('effects')
        voorbeelden_effects_1 = voorbeelden[1]
        voorbeelden_effects_2 = voorbeelden[2]
        voorbeelden_effects_3 = voorbeelden[3]
    with open(path, "r") as file:
        voorbeelden = yaml.load(file)
        voorbeelden = voorbeelden.get('voorbeelden').get('placeholders')
        voorbeelden_placeholders_1 = voorbeelden[1]
        voorbeelden_placeholders_2 = voorbeelden[2]
        voorbeelden_placeholders_3 = voorbeelden[3]
    with open(path, "r") as file:
        voorbeelden = yaml.load(file)
        voorbeelden = voorbeelden.get('voorbeelden').get('conditions')
        voorbeelden_conditions_1 = voorbeelden[1]
        voorbeelden_conditions_2 = voorbeelden[2]
        voorbeelden_conditions_3 = voorbeelden[3]

def dump_yaml(path):
    with open(path, "w") as file:
        yaml.dump(voorbeelden, file)



Client = discord.Client()
client = commands.Bot(command_prefix = "!")



@client.event
@asyncio.coroutine
def on_ready():
    print("Bot is ready!")

@client.event
@asyncio.coroutine
async def on_message(message):
    if message.content.lower() == "cookie":
        await client.send_message(message.channel, ":cookie:")
    if message.content.lower() == "cookies":
        await client.send_message(message.channel, ":cookie::cookie::cookie:")
    if message.content.lower() == "!kanaal":
        await client.send_message(message.channel, "Dit is mijn youtube kanaal: https://www.youtube.com/citycraft")
    if message.content.lower().startswith("!speel"):
        if message.author.id == "283554212019699722":
            args = message.content.split(" ")
            await client.send_message(message.channel, " ".join(args[1:]))
            await client.change_presence(game=discord.Game(name=" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "Je hebt hier geen permissies voor!")
    if message.content.lower().startswith("!skript"):
        args = message.content.split(" ")
        if len(args) > 1:
            if args[1].lower() == "help":
                if len(args) > 2:
                    if args[2].lower() == "events":
                        embed = discord.Embed(title="Skript Events", colour=0xDEADBF)
                        embed.add_field(name="Uitleg", value="Skript events doen iets als er iets in minecraft gebeurd.", inline=False)
                        embed.add_field(name="Gebruik", value="Gebruik dit altijd op een lijn zonder tabs, je hebt geen trigger nodig.", inline=False)
                        embed.add_field(name="Lijst", value="http://en.njol.ch/projects/skript/doc/events", inline=False)
                        embed.add_field(name="Voorbeeld 1:", value=voorbeelden_events_1, inline=False)
                        embed.add_field(name="Voorbeeld 2:", value=voorbeelden_events_2, inline=False)
                        embed.add_field(name="Voorbeeld 3:", value=voorbeelden_events_3, inline=False)
                        await client.send_message(message.channel, embed=embed)
                    if args[2].lower() == "effects":
                        embed = discord.Embed(title="Skript Effects", colour=0xDEADBF)
                        embed.add_field(name="Uitleg", value="Een effect gebruik je om iets te doen in minecraft", inline=False)
                        embed.add_field(name="Gebruik", value="Je kan dit overal in gebruiken, behalve een lijn zonder tabs", inline=False)
                        embed.add_field(name="Lijst", value="http://en.njol.ch/projects/skript/doc/effects", inline=False)
                        await client.send_message(message.channel, embed=embed)
                    if args[2].lower() == "placeholders":
                        embed = discord.Embed(title="Skript Placeholders", colour=0xDEADBF)
                        embed.add_field(name="Uitleg", value="Een placeholder gebruik je om iets te vermelden dat kan veranderen. Bijvoorbeeld de tijd", inline=False)
                        embed.add_field(name="Gebruik", value="Om een placeholder aan te geven zet je % om wat je wilt toevoegen. Bijvoorbeeld %time%", inline=False)
                        embed.add_field(name="Lijst", value="http://en.njol.ch/projects/skript/doc/expressions", inline=False)
                        await client.send_message(message.channel, embed=embed)
                    if args[2].lower() == "conditions":
                        embed = discord.Embed(title="Skript Conditions", colour=0xDEADBF)
                        embed.add_field(name="Uitleg", value="Een placeholder is iets dat je kan checken, bijvoorbeeld **is flying**", inline=False)
                        embed.add_field(name="Gebruik", value="Een placeholder gebruik je altijd in een **if** statement", inline=False)
                        embed.add_field(name="Lijst", value="http://en.njol.ch/projects/skript/doc/conditions", inline=False)
                        await client.send_message(message.channel, embed=embed)
                    if args[2].lower() == "expressions":
                        embed = discord.Embed(title="Skript Conditions", colour=0xDEADBF)
                        embed.add_field(name="Uitleg", value="Een Expression gebruik je om iets te vermelden dat kan veranderen. Bijvoorbeeld de tijd", inline=False)
                        embed.add_field(name="Gebruik", value="Om een expression aan te geven zet je % om wat je wilt toevoegen. Bijvoorbeeld %time%", inline=False)
                        embed.add_field(name="Lijst", value="http://en.njol.ch/projects/skript/doc/expressions", inline=False)
                        await client.send_message(message.channel, embed=embed)
                    if args[2].lower() == "loops":
                        embed = discord.Embed(title="Skript Conditions", colour=0xDEADBF)
                        embed.add_field(name="Uitleg", value="Een loop gebruik je om meerdere keren iets  te doen", inline=False)
                        embed.add_field(name="Gebruik", value="Je kan met **loop (zoveel) times** een paar keer loopen of je kan bijvoorbeeld alle spelers loopen met **loop all players**", inline=False)
                        embed.add_field(name="Lijst", value="http://en.njol.ch/projects/skript/doc/loops", inline=False)
                        await client.send_message(message.channel, embed=embed)
                    if args[2].lower() == "variables":
                        embed = discord.Embed(title="Skript Variabelen", colour=0xDEADBF)
                        embed.add_field(name="Uitleg", value="Een variabele is een stukje text dat je naar een waarde kan zetten", inline=False)
                        embed.add_field(name="Gebruik", value="Variabelen geef je aan door er **{ }** omheen te zettten", inline=False)
                        embed.add_field(name="Lijst/Meer uitleg", value="http://en.njol.ch/projects/skript/doc/variables", inline=False)
                        await client.send_message(message.channel, embed=embed)
                    if args[2].lower() == "variabelen":
                        embed = discord.Embed(title="Skript Variabelen", colour=0xDEADBF)
                        embed.add_field(name="Uitleg", value="Een variabele is een stukje text dat je naar een waarde kan zetten", inline=False)
                        embed.add_field(name="Gebruik", value="Variabelen geef je aan door er **{ }** omheen te zettten", inline=False)
                        embed.add_field(name="Lijst/Meer uitleg", value="http://en.njol.ch/projects/skript/doc/variables", inline=False)
                        await client.send_message(message.channel, embed=embed)
                    if args[2].lower() == "variabeles":
                        embed = discord.Embed(title="Skript Variabelen", colour=0xDEADBF)
                        embed.add_field(name="Uitleg", value="Een variabele is een stukje text dat je naar een waarde kan zetten", inline=False)
                        embed.add_field(name="Gebruik", value="Variabelen geef je aan door er **{ }** omheen te zettten", inline=False)
                        embed.add_field(name="Lijst/Meer uitleg", value="http://en.njol.ch/projects/skript/doc/variables", inline=False)
                        await client.send_message(message.channel, embed=embed)
                    if args[2].lower() == "variablen":
                        embed = discord.Embed(title="Skript Variabelen", colour=0xDEADBF)
                        embed.add_field(name="Uitleg", value="Een variabele is een stukje text dat je naar een waarde kan zetten", inline=False)
                        embed.add_field(name="Gebruik", value="Variabelen geef je aan door er **{ }** omheen te zettten", inline=False)
                        embed.add_field(name="Lijst/Meer uitleg", value="http://en.njol.ch/projects/skript/doc/variables", inline=False)
                        await client.send_message(message.channel, embed=embed)
                else:
                    embed = discord.Embed(title="Skript Help", colour=0xDEADBF)
                    embed.add_field(name="Events", value="Leer hier meer over events!", inline=False)
                    embed.add_field(name="Effects", value="Leer hier meer over effects!", inline=False)
                    embed.add_field(name="Placeholders", value="Leer hier meer over placeholders!", inline=False)
                    embed.add_field(name="Conditions", value="Leer hier meer over conditions!", inline=False)
                    embed.add_field(name="Expressions", value="Leer hier meer over expressions!", inline=False)
                    embed.add_field(name="Loops", value="Leer hier meer over loops!", inline=False)
                    embed.add_field(name="Variabelen", value="Leer hier meer over variabelen!", inline=False)
                    await client.send_message(message.channel, embed=embed)
            if args[1].lower() == "tutorial":
                if args[2].lower() == "scoreboard":
                    embed = discord.Embed(title="Skript Scoreboard", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=y5sy5AXLCuc", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "prefix":
                    embed = discord.Embed(title="Skript Prefix", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=ahNwT5HnLpE", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "gui":
                    embed = discord.Embed(title="Skript GUI", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=4FGA9JON2VA", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "usage":
                    embed = discord.Embed(title="Skript Usage", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=AzynmlBA00s", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "alias":
                    embed = discord.Embed(title="Skript Alias", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=AzynmlBA00s", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "aliases":
                    embed = discord.Embed(title="Skript Alias", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=AzynmlBA00s", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "permission":
                    embed = discord.Embed(title="Skript Permission", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=AzynmlBA00s", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "if":
                    embed = discord.Embed(title="Skript If-Else", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=WZcYIhzJGgo", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "else":
                    embed = discord.Embed(title="Skript If-Else", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=WZcYIhzJGgo", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "variables":
                    embed = discord.Embed(title="Skript Variabelen", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=WZcYIhzJGgo", inline=False)
                    embed.add_field(name="Video (Advanced)", value="https://www.youtube.com/watch?v=adjmrZtsOIY", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "variabeles":
                    embed = discord.Embed(title="Skript Variabelen", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=WZcYIhzJGgo", inline=False)
                    embed.add_field(name="Video (Advanced)", value="https://www.youtube.com/watch?v=adjmrZtsOIY", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "variabelen":
                    embed = discord.Embed(title="Skript Variabelen", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=WZcYIhzJGgo", inline=False)
                    embed.add_field(name="Video (Advanced)", value="https://www.youtube.com/watch?v=adjmrZtsOIY", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "arguments":
                    embed = discord.Embed(title="Skript Argumenten", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=Pk4x1dhJg3A", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "argumenten":
                    embed = discord.Embed(title="Skript Argumenten", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=Pk4x1dhJg3A", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "argument":
                    embed = discord.Embed(title="Skript Argumenten", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=Pk4x1dhJg3A", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "command":
                    embed = discord.Embed(title="Skript Commando's", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=Pk4x1dhJg3A", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "commands":
                    embed = discord.Embed(title="Skript Commando's", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=Pk4x1dhJg3A", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "effect":
                    embed = discord.Embed(title="Skript Effecten", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=Pk4x1dhJg3A", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "effects":
                    embed = discord.Embed(title="Skript Effecten", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=Pk4x1dhJg3A", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "effecten":
                    embed = discord.Embed(title="Skript Effecten", colour=0xDEADBF)
                    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=Pk4x1dhJg3A", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "loop":
                    embed = discord.Embed(title="Skript Loops", colour=0xDEADBF)
                    embed.add_field(name="Video (Advanced)", value="https://www.youtube.com/watch?v=Pk4x1dhJg3A", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "loops":
                    embed = discord.Embed(title="Skript Loops", colour=0xDEADBF)
                    embed.add_field(name="Video (Advanced)", value="https://www.youtube.com/watch?v=Pk4x1dhJg3A", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "config":
                    embed = discord.Embed(title="Skript Configs", colour=0xDEADBF)
                    embed.add_field(name="Video (Advanced)", value="https://www.youtube.com/watch?v=ZJXytyuc_-Q", inline=False)
                    await client.send_message(message.channel, embed=embed)
                if args[2].lower() == "configs":
                    embed = discord.Embed(title="Skript Configs", colour=0xDEADBF)
                    embed.add_field(name="Video (Advanced)", value="https://www.youtube.com/watch?v=ZJXytyuc_-Q", inline=False)
                    await client.send_message(message.channel, embed=embed)
            if args[1].lower() == "download":
                embed = discord.Embed(title="Download", description="Download hier skript", colour=0xDEADBF)
                embed.add_field(name="Laatste Skript versie", value="https://github.com/bensku/Skript/releases/download/dev35/Skript.jar", inline=False)
                await client.send_message(message.channel, embed=embed)
        if args[1].lower() == "maakvoorbeeld":
            if len(args) > 2:
                if args[2].lower() == "events":
                    iets = "iets"
        else:
            embed = discord.Embed(title="Skript Help", colour=0xDEADBF)
            embed.add_field(name="Help", value="Leer hier meer over skript", inline=False)
            embed.add_field(name="Download", value="Download hier skript", inline=False)
            embed.add_field(name="Maakvoorbeeld", value="Maak hier voorbeelden die in het help commando komen", inline=False)
            await client.send_message(message.channel, embed=embed)





load_yaml(path)

client.run("NDMwNzcwODc5Mjg3Mzk0MzE0.DaVCyA.h6Vi4SnZYqJRZpXAlcBGwhhi-PQ")

load_yaml(path)
