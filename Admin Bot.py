import os
import discord

messages = joined = 0


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


client = discord.Client()


@client.event
async def on_member_join(member):
    global joined
    joined += 1
    if joined == 1:
        await client.send_message(f"""Welcome to the server {discord.member.mention}""")


@client.event
async def on_message(message):
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
        if message.content == "^bot":
            await message.channel.send(f"Here is my source code https://github.com/Gunn1/Admin_Bot")
            print(f"{message.author} Just typed GitHub")
            found = True
        if "^help" in message.content:
            embed = discord.Embed(title="Admin Bot", description="Some useful commands")
            embed.add_field(name="^hello", value="Greets the user")
            embed.add_field(name="^users", value="Prints number of users")
            embed.add_field(name="^welcome", value="Welcome People")
            embed.add_field(name="^bot", value="GitHub bot source code")
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


print("Connected To Discord!")
client.run(client.run(os.environ['TOKEN']))
