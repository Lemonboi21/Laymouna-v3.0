import discord
from discord.ext import commands
from discord import app_commands
from bot_tools import *

class slash(commands.Cog):
    def __init__(self,laymouna):
        self.laymouna = laymouna
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.laymouna.tree.sync()
        print("slash.py is ready !")

    @app_commands.command(name="fuckinhelp" , description="shows all available commands")
    async def fuckinhelp (self , interaction : discord.Interaction):

        help_embed = discord.Embed(title="help !", description="all available commands for the bot",color=discord.Color.yellow())
        help_embed.add_field(name="**emots**",value="sad , blush , cry , thumbsup , sus , triggered , police , wizzard , ta7iya , f9tlk , lmblg",inline=False)
        help_embed.add_field(name="**economy**",value="lemon , daily , leaderboard , deposit , withdraw , rob , finebox , stealfinebox , lkhedma , navigui , give",inline=False)
        help_embed.add_field(name="**games**",value="gamble , coinflip , top , rps , guess , farouk",inline=False)
        help_embed.add_field(name="**fun**",value="ask , question , hikma , tod , memic , bored , morse , binary , text , yoda , number , nasa , yomoma , roast , useless , joke , paranoia , nhie ",inline=False)
        help_embed.add_field(name="**other**",value="math , ai , feedback",inline=False)
    
        await interaction.response.send_message(embed=help_embed)

    @app_commands.command(name="feedback" , description="send a feedback to the bot's creator (bugs , suggestions , etc..)")
    async def feedback (self , interaction : discord.Interaction , *,feedback:str):

        add_feedback(interaction.user,feedback)
        await interaction.response.send_message("thank you for your feedback 💛 !")

    @app_commands.command(name="homework" , description="add a homework to get notified when it's time")
    async def homework (self , interaction : discord.Interaction , *,homework:str):

        homework = homework.split(",")

        """get parameters"""
        homework = homework.split(",")
        module = homework[0]
        homework = homework[1]
        dateDue = homework[2]

        """print parameters"""
        print(module)
        print(homework)
        print(dateDue)

        """add homework to database"""
        

        "add_homework(interaction.user,module,homework,dateDue)"
        
        await interaction.response.send_message("homework added ! use the /homework_list command to see your homeworks")

    """@app_commands.command(name="homework_list" , description="shows your homeworks")
    async def homeworklist (self , interaction : discord.Interaction):

        homeworks = get_user_homework(interaction.user)
        homework_list = discord.Embed(title="homework list",description="all your homeworks",color=discord.Color.blue())

        for homework in homeworks:
            homework_list.add_field(name=f"{homeworks[homework]['module']} : {homeworks[homework]['homework']}",value=f"due date : {homeworks[homework]['date due']}",inline=False)

        await interaction.response.send_message(embed=homework_list)
"""

async def setup(laymouna):
    await laymouna.add_cog(slash(laymouna))