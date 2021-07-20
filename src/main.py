from discord.ext import commands
import discord
from playlistInteractor import PlaylistInteractor

bot = commands.Bot(command_prefix= '^')

@bot.event 
async def on_ready():
    print(f"Logged in and ready to run as {bot.user}")
    
@bot.event
async def on_message(msg: discord.Message):
    if msg.author == bot.user:
        return 
    
    if msg.channel.id == 833576458135666738 or msg.channel.id == 866951958937731102:
        channel = msg.channel
        if "open.spotify" in msg.content:
            if "track" in msg.content:
                song_url = msg.content
                song_id = song_url.split('/')[-1].split('?')[0]
                interactor = PlaylistInteractor([song_id])
                interactor.addToPlaylist()
                
                await msg.add_reaction("👍")
                await channel.send("Added Song To Playlist")
            
            else:
                await msg.add_reaction("👎")    
                await channel.send("Please Provide Link To A Single Song And Not A Playlist\\Album")
            
        else:
            await msg.add_reaction("👎")
            await channel.send(f"That is not a spotify song URL, please provide a Valid **SPOTIFY** URL")
            
    
with open(r"discord_auth.txt", "r") as f:
    token = f.read().splitlines()
    
bot.run(token[0])