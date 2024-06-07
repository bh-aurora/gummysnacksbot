import discord
from discord import *
import os
from dotenv import load_dotenv
import asyncio
import hashlib
import json
from asyncio import *
from datetime import *
from cairosvg import svg2png


class EST(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours = -5)
    def tzname(self, dt):
        return "EST"
    def dst(self, dt):
        return timedelta(0)
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
        output_file = os.path.join("C:/proj/drip/public/panel/modules/hub", "bug_count.json")
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
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

class ButtonView(discord.ui.View):
    foo : bool = None
    @discord.ui.button(label='Resolved', style=discord.ButtonStyle.success)
    async def resolved(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.foo = True
        self.stop()    
@tree.command(name="kit", description="Rust kit cost calculator")
@app_commands.choices(weapon=[
    app_commands.Choice(name="Thompson", value="0"),
    app_commands.Choice(name="AK", value="1"),
])
async def kit(interaction, weapon: app_commands.Choice[str], amount: int):
    if amount >= 21:
        await interaction.response.send_message("You don't need to craft more than 20 kits at a time.")
        return
    embed = discord.Embed(title=f"{amount}x {weapon.name} Kit")
    open('NewAKkitIMG.svg', 'w').write(open('AKkitIMG.svg').read().replace("""Wood_text</title>x200</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="75" y="55"><title>MF_Text</title>x665</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="135" y="55"><title>HQ_Text</title>x86</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="195" y="55"><title>Cloth_Text</title>x290</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="255" y="55"><title>Leather_Text</title>x150</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="315" y="55"><title>AF_Text</title>x90</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="315" y="115"><title>SK_Text</title>x21</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="255" y="115"><title>RS_Text</title>x2</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="195" y="115"><title>Spring_Text</title>x4</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="135" y="115"><title>RB_Text</title>x1</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="75" y="115"><title>Charcoal_Text</title>x810</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="15" y="115"><title>Sulfur_Text</title>x540</text>""", f"""Wood_text</title>x{200 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="75" y="55"><title>MF_Text</title>x{665 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="135" y="55"><title>HQ_Text</title>x{86 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="195" y="55"><title>Cloth_Text</title>x{290 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="255" y="55"><title>Leather_Text</title>x{150 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="315" y="55"><title>AF_Text</title>x{90 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="315" y="115"><title>SK_Text</title>x{21 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="255" y="115"><title>RS_Text</title>x{2 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="195" y="115"><title>Spring_Text</title>x{4 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="135" y="115"><title>RB_Text</title>x{1 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="75" y="115"><title>Charcoal_Text</title>x{810 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="15" y="115"><title>Sulfur_Text</title>x{540 * amount}</text>"""))

    svg2png(url="NewAKkitIMG.svg", write_to="AKkitIMG.png")
    open('NewThompsonkitIMG.svg', 'w').write(open('ThompsonkitIMG.svg').read().replace("""Wood_text</title>x100</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="75.792" y="55.527" transform="matrix(1, 0, 0, 1, 0.148682, 0)"><title>MF_Text</title>x360<tspan x="75.79199981689453" dy="1em">​</tspan></text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="135.941" y="55.527"><title>HQ_Text</title>x21</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="195.941" y="55.527"><title>Cloth_Text</title>x140</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="255.931" y="55.525"><title>AF_Text</title>x90</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="315.931" y="55.525"><title>Sulfur_Text</title>x280</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="15.931" y="115.525"><title>Charcoal_Text</title>x420</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="75.941" y="115.527"><title>SB_Text</title>x1</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="135.941" y="115.527"><title>Spring_Text</title>x1</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="195.941" y="115.527"><title>SK_Text</title>x2</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="255.941" y="115.527"><title>Tarp_Text</title>x5</text>""", f"""Wood_text</title>x{100 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="75.792" y="55.527" transform="matrix(1, 0, 0, 1, 0.148682, 0)"><title>MF_Text</title>x{360 * amount}<tspan x="75.79199981689453" dy="1em">​</tspan></text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="135.941" y="55.527"><title>HQ_Text</title>x{21 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="195.941" y="55.527"><title>Cloth_Text</title>x{140 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="255.931" y="55.525"><title>AF_Text</title>x{90 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="315.931" y="55.525"><title>Sulfur_Text</title>x{280 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="15.931" y="115.525"><title>Charcoal_Text</title>x{420 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="75.941" y="115.527"><title>SB_Text</title>x{1 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="135.941" y="115.527"><title>Spring_Text</title>x{1 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="195.941" y="115.527"><title>SK_Text</title>x{2 * amount}</text>
    <text style="fill: rgb(255, 255, 255); font-family: C059; font-size: 10px; font-style: italic; font-weight: 700; white-space: pre;" x="255.941" y="115.527"><title>Tarp_Text</title>x{5 * amount}</text>"""))
    svg2png(url="NewThompsonkitIMG.svg", write_to="ThompsonkitIMG.png")
    ak = discord.File("AKkitIMG.png")
    thompson = discord.File("ThompsonkitIMG.png")
    if weapon.value == "0":
        embed.set_image(url="attachment://ThompsonkitIMG.png")
    elif weapon.value == "1":
        embed.set_image(url="attachment://AKkitIMG.png")
    if weapon.value == "0":
        await interaction.response.send_message(file = thompson, embed=embed)
    elif weapon.value == "1":
        await interaction.response.send_message(file = ak, embed=embed)
@tree.command(name="bug", description="Report a bug to the developers")
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
async def bug(i: discord.Interaction, severity: app_commands.Choice[str], type: app_commands.Choice[str], bug: str):
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
    hashed_id = hashlib.sha256(timestamp.encode()).hexdigest()
    dictionary = {
            "id": hashed_id,
            "Severity": severity.name,
            "Type": type.name,
            "Bug": bug,
            "Reported by": i.user.name,
            "Time": timestamp,
            "Status": "Open"
        }
    json_object = json.dumps(dictionary, indent=4)
    directory = os.path.dirname(os.path.realpath(__file__))
    output_file = os.path.join("C:/quickstart/DiscordBot", "bugs.json")
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
    view = ButtonView()
    await i.response.send_message(embed=embed, view=view)
    response = await i.original_response()
    await view.wait()
    if view.foo == True:
        with open('bugs.json', 'r') as file:
            data = json.load(file)
        for bug in data:
            if bug['id'] == hashed_id:
                bug['Status'] = "Resolved"
        with open('bugs.json', 'w') as file:
            json.dump(data, file, indent=4)

        await response.delete(delay=2)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="/bug"))
    while True:
        await sleep(15)
        await tree.sync()
        await bug_count()
        print('Synced!')

client.run(TOKEN)