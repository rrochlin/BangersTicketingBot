import discord
import responses
from configparser import ConfigParser


async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        if response:
            await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    config = ConfigParser()
    config.read("Web.config")
    TOKEN = config["SECRETS"]["TOKEN"]
    intents = discord.Intents(messages=True, guilds=True, message_content=True)
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        user_message = str(message.content)
        await send_message(message, user_message)

    client.run(TOKEN)
