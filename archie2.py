import discord
import asyncio
from discord.ext.commands import bot
from discord.ext import commands

Client = discord.Client()
bot_prefix="?"
client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
	print("Bot Online!")
	print("Name: {}".format(client.user.name))
	print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def ping(ctx):
	await client.say("Pong!")

if __name__ == '__main__':
    import config
    client.run(config.token)

# Do not share the token with anyone and less to publish it on GitHub. Use .gitignore files or similar to hide the file that contains the token.
