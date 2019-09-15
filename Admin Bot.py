import os

import discord

import Command

messages = joined = 0


client = discord.Client()


@client.event
async def on_member_join(member):
    global joined
    joined += 1
    if joined == 1:
        await client.send_message(f"Welcome to the server {discord.member.mention}")


@client.event
async def on_message(message):
    # On Message Sent
    id = client.get_guild(os.environ['CLIENT_ID'])
    if "^" in message.content:
        found = False
        if "^hello" in message.content:
            await message.channel.send(f"Hello {message.author}")
            print(f" {message.author} Said Hello")
            found = True
        if "^users" in message.content:
            await message.channel.send(f" Number of Members: {id.member_count}")
            print(f"""{message.author} Asked for users""")
            found = True
        if "^bot" in message.content:
            await message.channel.send("Here is my source code https://github.com/Gunn1/Admin_Bot")
            print(f"{message.author} Just typed ^bot")
            found = True
        if "^python" in message.content:
            await message.channel.send("Here is the Python website https://www.python.org/")
            print(f"{message.author} Just typed ^python")
            found = True
        if "^ninja modding" in message.content:
            await message.channel.send("Here is the Ninja Modding website https://www.ninjamodding.com/")
            print(f"{message.author} Just typed ^ninja modding")
            found = True
        if "^help" in message.content:

            embed = discord.Embed(title="Admin Bot", description="Some useful commands")

            embed.add_field(name="^hello", value="Greets the user")

            embed.add_field(name="^users", value="Prints number of users")

            embed.add_field(name="^welcome", value="Welcome People")

            embed.add_field(name="^bot", value="GitHub bot source code")

            embed.add_field(name="^python", value="Python website")

            embed.add_field(name="^ninja modding", value="Ninja Modding website")
            found = True
            await message.channel.send(content=None, embed=embed)
        if "^welcome" in message.content:
            await message.channel.send("Welcome All")
            found = True

        if not found:
            # This will check to see if the ^ is before some text
            pos = message.content.find("^")
            if pos != -1:
                if message.content[pos + 1] != " ":
                    await message.channel.send("Sorry I do not know that.")

def register_command(command, message):
    Command.commands.add(Command.Command(command, message))

print("Connected To Discord!")
client.run(client.run(os.environ['TOKEN']))
