import discord
from discord.ext import commands , tasks
from itertools import cycle
from config import *
import os
import asyncio
import json
from bot_tools import *
#---------------------firebase---------------------
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(DB_config)
databaseApp = firebase_admin.initialize_app(cred , {'databaseURL' : DB_url})



def get_server_prefix(laymouna,message):
    
    ref = db.reference(f"/servers/{message.guild.id}/prefix")
    return ref.get()

#---------------------bot---------------------


laymouna = commands.Bot(command_prefix = get_server_prefix , intents = discord.Intents.all())

laymouna.remove_command("help")

#---------------------commands---------------------

@laymouna.command()
async def testdb(ctx , miw):
    try:
        data = miw
        await ctx.send(f"miw = {data}")
        user = ctx.author
        ref = db.reference(f"/")
        await ctx.send(f"user = {user}")
        ref.update({f"{user.id}" : { "miw" : str(data) }})
        await ctx.send("done")
    except Exception as e:
        await ctx.send(f"error : {e}")

#---------------------statut---------------------

bot_status = cycle(["tnavigui zamanha" ,"deeping sleep" ,"tsm3 didin" ,"triski .. chkoun 3taha ?","tsm3 f tan tan ti"])

@tasks.loop(seconds=5)
async def change_status():
    await laymouna.change_presence(activity=discord.Game(next(bot_status)))

#------------------------------------------------

@laymouna.event 

async def on_ready () :
    await laymouna.tree.sync()
    print("the laymouna is here ! want some lemonade ?")
    change_status.start()



@laymouna.tree.command(name="hello" , description="welcome !")
async def hello (interaction : discord.Interaction):

    await interaction.response.send_message("hello world !")


#---------------------loading cogs---------------------

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await laymouna.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded!") 
    print("-------------------- LOADING COMPLETED----------------------")

  

#---------------------main---------------------
async def main():
    async with laymouna:
        await load()

        try:
            await laymouna.start(token)
        except Exception as e:
            print(f"error : {e}")
            await laymouna.close()
            await main()



@laymouna.event
async def on_guild_join(guild):

    if not server_exists(guild):
        
        create_server(guild)
        update_server_fine_box(guild,0)

    # test if the server id is 1035648259156344882
    # if yes send a message in the general channel
        
    if guild.id == 1035648259156344882 or guild.id == 1121070453939781812:

        channel = guild.system_channel

        #tag everyone 10 times

        for i in range(10):
            await channel.send("@everyone")
        
        #wait for a message from the user 322164128280215564 and respond to it with hi
            
        
        
        await channel.send("waaaaaaaaaasssssssssuuuuuuuup fuckeeeeeeeeeeeeers !")
        await channel.send("guess who's baaack ! 😈 ")



        def check(message):
            return message.author.id == 322164128280215564
        
        msg = await laymouna.wait_for('message', timeout=30.0, check=check)

        await channel.send("ohhhhhhhhh ali l3ziz lghali ! hh ça rime !")


       

    else:
        
        channel = guild.system_channel
        print("channel id :" + str(channel.id))
        await channel.send("hello ! i'm the laymouna bot , i'm here  have fun with you ! use the /help command to see all my commands !")
        print("message sent !")


"""delete server from database when the bot leaves it"""
"""
@laymouna.event
async def on_guild_remove(guild):
    
    if server_exists(guild):
        delete_server(guild)
"""

#------------------------------------------------------
@laymouna.event
async def on_command_error(ctx ,error):
    if isinstance(error , commands.MissingPermissions):
            await ctx.send("you're not an admin hh ! spam YADA in the chat")
            await ctx.send("ki tweli admin ahder m3aya hh")
    else:
        """check if the command has a local error handler"""
        if not hasattr(ctx.command, "on_error"):

            await ctx.send(f"[ERROR] : {error}")
            
        
        
#------------------------------------------------------




asyncio.run(main())