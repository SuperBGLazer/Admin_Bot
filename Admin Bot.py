import os

import discord
import time
import asyncio

messages = joined = 0


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


client = discord.Client()


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)


@client.event
async def on_member_join(member):
    global joined
    joined += 1
    if joined == 1:
        await client.send_message(f"""Welcome to the server {member.mention}""")

@client.event
async def on_message(message):
    id = client.get_guild(592447508219953163)
    if message.content.find("!hello") != -1:
        print("User Said Hello")
        await message.channel.send("Hello")
    elif message.content == "!users":
        print("User Asked for !user")
        await message.channel.send(f""" Number of Members: {id.member_count}""")
    ...
    if message.content == "!help":
        embed = discord.Embed(title="Admin Bot", description="Some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        await message.channel.send(content=None, embed=embed)
    ...

print("Connected To Discord!")

client.loop.create_task(update_stats())
client.run(client.run(os.environ['TOKEN']))
