import discord
from discord.ext.commands import bot
from discord.ext import commands

Client = discord.Client()
bot_prefix="?"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
	print("Bot Online!")
	print("Name: {}".format(client.user.name))
	print("ID: {}".format(client.user.id))

@client.command(pass context=True)
async def ping(ctx):
	await client.say("Pong!")

client.run("NDYyMjcyMDcyMjM2NzkzODU2.DhhSCQ.UK_3JEF59C87Ju36Z6dwbFvie9U")
