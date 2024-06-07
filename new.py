import discord
from discord import *
import os
from dotenv import load_dotenv
import asyncio
import hashlib
import json
from asyncio import *
from datetime import *
import uuid

# Initialize the message store
message_store = {}

async def bug_count():
    channel = client.get_channel(1239955122281250846)
    count = 0
    if channel:
        async for _ in channel.history(limit=None):
            count+=1
        count_dictionary = {
            "Found": count
        }
        directory = os.path.dirname(os.path.realpath(__file__))
        output_file = os.path.join("", "bugs_found.json")
        with open(output_file, "w") as outfile:
            json.dump(count_dictionary, outfile, indent=4)
    else:
        print('Channel not found or other error occurred')

def custom_hash(string, key):
    combined_string = string + key
    combined_bytes = combined_string.encode('utf-8')
    hashed_bytes = hashlib.sha256(combined_bytes).digest()
    hashed_hex = hashlib.sha256(hashed_bytes).hexdigest()
    return hashed_hex

key = 'bug id generation key'

load_dotenv()
TOKEN = os.getenv('TESTING_TOKEN')
intents = Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

class EST(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours = -5)
    def tzname(self, dt):
        return "EST"
    def dst(self, dt):
        return timedelta(0)

class ButtonView(discord.ui.View):
    def __init__(self, custom_id):
        super().__init__(timeout=None)
        self.custom_id = custom_id
        self.foo = None
        self.clicked = False

    @discord.ui.button(label='Resolved', style=discord.ButtonStyle.success, custom_id='resolved')
    async def resolved(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.clicked = True
        self.foo = True
        self.is_persistent = True
        message_id = self.custom_id
        if message_id in message_store:
            await message_store[message_id].delete()
            del message_store[message_id]
            await interaction.response.send_message("Message deleted!", ephemeral=True)
        else:
            await interaction.response.send_message("Message already deleted or not found.", ephemeral=True)
        self.stop()

@tree.command(name="testing", description="testing")
@app_commands.choices(severity=[
    app_commands.Choice(name="Low", value="0"),
    app_commands.Choice(name="Medium", value="1"),
    app_commands.Choice(name="High", value="2"),
    app_commands.Choice(name="Critical", value="3"),
    app_commands.Choice(name="Security", value="4")
])
@app_commands.choices(type=[
    app_commands.Choice(name="Web", value="0"),
    app_commands.Choice(name="Structure", value="1"),
])
async def testing(i: discord.Interaction, severity: app_commands.Choice[str], type: app_commands.Choice[str], bug: str):
    embed = discord.Embed(title="Bug Report", timestamp=i.created_at)
    if severity.value == "0":
        embed.color = discord.Colour.dark_green()
    elif severity.value == "1":
        embed.color = discord.Colour.gold()
    elif severity.value == "2":
        embed.color = discord.Colour.orange()
    elif severity.value == "3":
        embed.color = discord.Colour.red()
    elif severity.value == "4":
        embed.color = discord.Colour.purple()
    embed.add_field(name="Severity", value=f'> {severity.name}', inline=False)
    embed.add_field(name="Type", value=f'> {type.name}', inline=False)
    embed.add_field(name="Bug", value=f'```{bug}```', inline=False)
    embed.set_footer(text=f"Reported by {i.user.name}")
    timestamp = datetime.now(EST()).strftime("%m/%d/%Y %H:%M:%S")
    hashed_id = custom_hash(timestamp, key)
    
    # Generate a unique ID for the message
    custom_id = str(uuid.uuid4())
    
    view = ButtonView(custom_id)
    await i.response.send_message(embed=embed, view=view)
    
    message = await i.original_response()
    message_store[custom_id] = message
    
    dictionary = {
        "id": hashed_id,
        "Severity": severity.name,
        "Type": type.name,
        "Bug": bug,
        "Reported by": i.user.name,
        "Time": timestamp,
        "Status": "Open",
        "mID": custom_id
    }
    
    json_object = json.dumps(dictionary, indent=4)
    directory = os.path.dirname(os.path.realpath(__file__))
    output_file = os.path.join("", "bugs.json")
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        with open(output_file, "r") as infile:
            existing_data = json.load(infile)
        if isinstance(existing_data, list):
            existing_data.append(dictionary)
        else:
            existing_data = [existing_data, dictionary]
    else:
        existing_data = [dictionary]

    with open(output_file, "w") as outfile:
        json.dump(existing_data, outfile, indent=4)
    
    await view.wait()
    if view.foo:
        with open('bugs.json', 'r') as file:
            data = json.load(file)
        for bug in data:
            if bug['id'] == hashed_id:
                bug['Status'] = "Resolved"
        with open('bugs.json', 'w') as file:
            json.dump(data, file, indent=4)

@client.event
async def on_ready():
    client.add_view(ButtonView("dummy_id"))  # Add a dummy view to initialize
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="Restructure"))
    while True:
        await sleep(15)
        await tree.sync()
        await bug_count()
        print('Synced!')

client.run(TOKEN)
