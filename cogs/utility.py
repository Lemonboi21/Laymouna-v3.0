import asyncio
import datetime
from gemini import answer
import discord
from discord.ext import commands
from bot_tools import *



class utility(commands.Cog):
    def __init__(self,laymouna):
        self.laymouna = laymouna
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("utility.py is ready !")

    @commands.command()
    async def ping(self , ctx):
        bot_latency = round(self.laymouna.latency * 1000)
        await ctx.send(f"pong! {bot_latency} ms.")

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def prefix(self,ctx, *,newprefix=None):

        if newprefix == None:
            newprefix = "l "
        
        set_server_prefix(ctx.guild,newprefix)

        await ctx.send(f"the prefix is now set to {newprefix} ")
    
    @commands.command()
    async def help(self,ctx):

        #---------------------help command---------------------
        


        help_embed = discord.Embed(title="help !", description="all available commands for the bot",color=discord.Color.yellow())
        help_embed.add_field(name="**emots**",value="sad , blush , cry , thumbsup , sus , triggered , police , wizzard , ta7iya , f9tlk , lmblg",inline=False)
        help_embed.add_field(name="**economy**",value="lemon , daily , leaderboard , deposit , withdraw , rob , finebox , stealfinebox , lkhedma , navigui , give",inline=False)
        help_embed.add_field(name="**games**",value="gamble , coinflip , top , rps , guess , farouk",inline=False)
        help_embed.add_field(name="**fun**",value="ask , question , hikma , tod , memic , bored , morse , binary , text , yoda , number , nasa , yomoma , roast , useless , joke , paranoia , nhie ",inline=False)
        help_embed.add_field(name="**other**",value="math , ai , feedback",inline=False)


    

    
        await ctx.send(embed=help_embed)
    
    @prefix.error
    async def prefix_error(self , ctx , error):
        if isinstance(error , commands.MissingRequiredArgument):
            await ctx.send("error : missing required argument")
        if isinstance(error , commands.MissingPermissions):
            await ctx.send("you're not an admin hh ! spam YADA in the chat")
            await ctx.send("ki tweli admin ahder m3aya hh")

    @commands.command(aliases=["special","special thanks","thanks"])
    async def special_thanks(self,ctx):

        user_id = '897210626089320468' # replace with the user ID you want to mention
        guild = ctx.guild
        yuzu = guild.get_member(int(user_id))
    
        await ctx.send(f"I just wanted to take a moment to give a big shoutout to {yuzu.mention} for creating all the amazing artwork that I'm using in this bot. I couldn't have built this bot without her incredible talent and hard work, and I'm so grateful for everything she's done. Thank you so much, Yuzu, you're a true artist and an amazing friend! 🙏🏻")
        await ctx.send("||here's the fil li kounti tsalili 🐘 + 3 extra beans 🫘||")
        
    
    @commands.command()
    async def feedback(self,ctx,*,feedback):

        add_feedback(ctx,feedback)
        await ctx.send("thanks for your feedback 💛 !")

        

    @commands.command()
    async def math(self,ctx,*,equation):


            
        try:
            """remove spaces between numbers and operators"""
            equation = equation.replace(" ","")
            """replace x with *"""
            equation = equation.replace("x","*")
            """replace ÷ with /"""
            equation = equation.replace("÷","/")
            """replace ^ with **"""
            equation = equation.replace("^","**")
        
            if equation == "10+9":
                result = 21
            elif "**" in equation and int(equation[equation.index("**")+2:]) > 1000:
                await ctx.send("the result is infinity")
                return
            else:
                result = eval(equation)
            await ctx.send(f"the result is : {result}")
        except Exception as e:
            await ctx.send(f"error : {e}")
        

    @commands.command()
    async def testlvl(self,ctx,n:int,function):
        """tests the xp needed for the 10 first levels"""

        try:
            function = function.replace(" ","")
            function = function.replace("x","i")

            for i in range(1,n):
                result = eval(function)
                await ctx.send(f"level {i} : {result} xp")

            await ctx.send("done !")
        except Exception as e :
            await ctx.send(e)


    """ make it only for developers """


    @commands.command(aliases=["fl","feedbacks","feedback list"])
    @commands.has_permissions(administrator = True)
    #@commands.check(is_developer)
    async def feedback_list(self,ctx,type:str=None):

        feedback_count = get_feedback_count() +1
        print(feedback_count)

        """make an embed for feedbacks"""
        feedback_embed = discord.Embed(title="feedbacks",description="all feedbacks",color=discord.Color.blue())

        """add feedbacks to embed (feeedback and status)"""
        
        if type == None:
            for i in range(feedback_count):
                print(i)
                feedback = get_feedback(i)
                #test if the feedback isnt none
                if feedback != None:
                    feedback_embed.add_field(name=f"feedback {i}",value=f"{feedback}",inline=False)

        elif type == "false":
            for i in range(feedback_count):
                feedback = get_feedback(i)
                feedback_status = get_feedback_status(i)
                if feedback != None and feedback_status == False :
                    feedback_embed.add_field(name=f"feedback {i}",value=f"{feedback}",inline=False)

        elif type == "true":
            for i in range(feedback_count):
                feedback = get_feedback(i)
                feedback_status = get_feedback_status(i)
                if feedback != None and feedback_status == True :
                    feedback_embed.add_field(name=f"feedback {i}",value=f"{feedback}",inline=False)

        else:
            await ctx.send("error : invalid type")
            return

        """send embed"""
        await ctx.send(embed=feedback_embed)
        
        await ctx.send("done !")

    
    @commands.command(aliases=["fr","feedback review"])
    @commands.has_permissions(administrator = True)
    #@commands.check(is_developer)
    async def feedback_review(self,ctx,feedback_id:int):
            
            feedback = get_feedback(feedback_id)
            feedback_status = get_feedback_status(feedback_id)

            feedback_embed = discord.Embed(title=f"feedback {feedback_id}",description=f"{feedback}",color=discord.Color.blue())
            feedback_embed.set_footer(text=f"reviewed : {feedback_status}")
            await ctx.send(embed=feedback_embed)

            await ctx.send("change feedback status ? (yes/no)") 

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel
            
            try:
                msg = await self.laymouna.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send('you took too long to answer !')
            else:
                if msg.content == "yes":
                    set_feedback_status(feedback_id-1,True)
                    await ctx.send("done !")
                elif msg.content == "no":
                    await ctx.send("done !")
                else:
                    await ctx.send("invalid answer !")



    @commands.command()
    async def homework (self , ctx , *,args:str):

        """get parameters"""
        args = args.split(",")
        module = args[0]
        homework = args[1]
        dateDue = args[2]

        """remove whitespace from edges of module and homework and dateDue"""
        module = module.strip()
        homework = homework.strip()
        dateDue = dateDue.strip()

        """turn dateDue into a datetime object"""
        dateFormat = "%d/%m/%Y"
        dateDue = datetime.datetime.strptime(dateDue,dateFormat)
        print(dateDue)

        """print parameters"""

        print(module)
        print(homework)
        print(dateDue)


        """add homework to database"""
        add_homework(ctx.author,module,homework,dateDue)
        
        await ctx.send("homework added ! use the /homework_list command to see your homeworks")


    @commands.command(aliases=[])
    async def ai (self,ctx,*,prompt:str):
        
        response = answer(prompt)

        await ctx.send(response)


async def setup(laymouna):
    await laymouna.add_cog(utility(laymouna))

























"""

        else:
            # test the name of the command and show desc of the command and its aliases
            command = command.lower()
            command = command.strip()
            command = command.replace(" ","")
            
            #---------------------economy---------------------
            if command == "lemon":
                help_embed = discord.Embed(title="lemon",description="lemon command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="shows how many lemons u have",inline=False)
                help_embed.add_field(name="aliases",value="lemonade , lmn",inline=False)
                help_embed.add_field(name="usage",value="l lemon",inline=False)

            
            elif command == "daily":
                help_embed = discord.Embed(title="daily",description="daily command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="gives you your daily lemons",inline=False)
                help_embed.add_field(name="aliases",value="d",inline=False)
                help_embed.add_field(name="usage",value="l daily",inline=False)

            
            elif command == "leaderboard":
                help_embed = discord.Embed(title="leaderboard",description="leaderboard command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="shows the leaderboard",inline=False)
                help_embed.add_field(name="aliases",value="lb",inline=False)
                help_embed.add_field(name="usage",value="l leaderboard",inline=False)

            
            elif command == "deposit":
                help_embed = discord.Embed(title="deposit",description="deposit command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="deposit your lemons in the bank",inline=False)
                help_embed.add_field(name="aliases",value="dep",inline=False)
                help_embed.add_field(name="usage",value="l deposit <amount>",inline=False)

            
            elif command == "withdraw":
                help_embed = discord.Embed(title="withdraw",description="withdraw command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="withdraw your lemons from the bank",inline=False)
                help_embed.add_field(name="aliases",value="with",inline=False)
                help_embed.add_field(name="usage",value="l withdraw <amount>",inline=False)


            elif command == "rob":
                help_embed = discord.Embed(title="rob",description="rob command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="rob a user",inline=False)
                help_embed.add_field(name="aliases",value="steal",inline=False)
                help_embed.add_field(name="usage",value="l rob <user>",inline=False)

            
            elif command == "finebox":
                help_embed = discord.Embed(title="finebox",description="finebox command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="shows the finebox",inline=False)
                help_embed.add_field(name="aliases",value="fb",inline=False)
                help_embed.add_field(name="usage",value="l finebox",inline=False)


            elif command == "stealfinebox":
                help_embed = discord.Embed(title="stealfinebox",description="stealfinebox command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="steals the finebox",inline=False)
                help_embed.add_field(name="aliases",value="sfb",inline=False)
                help_embed.add_field(name="usage",value="l stealfinebox",inline=False)


            elif command == "lkhedma":
                help_embed = discord.Embed(title="lkhedma",description="lkhedma command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="shows the lkhedma",inline=False)
                help_embed.add_field(name="aliases",value="lk",inline=False)
                help_embed.add_field(name="usage",value="l lkhedma",inline=False)


            elif command == "navigui":
                help_embed = discord.Embed(title="navigui",description="navigui command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="shows the navigui",inline=False)
                help_embed.add_field(name="aliases",value="nav",inline=False)
                help_embed.add_field(name="usage",value="l navigui",inline=False)


            elif command == "give":
                help_embed = discord.Embed(title="give",description="give command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="gives a user lemons",inline=False)
                help_embed.add_field(name="aliases",value="g",inline=False)
                help_embed.add_field(name="usage",value="l give <user> <amount>",inline=False)


            #---------------------games---------------------
            elif command == "gamble":
                help_embed = discord.Embed(title="gamble",description="gamble command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="gamble your lemons",inline=False)
                help_embed.add_field(name="aliases",value="gamb",inline=False)
                help_embed.add_field(name="usage",value="l gamble <amount>",inline=False)


            elif command == "coinflip":
                help_embed = discord.Embed(title="coinflip",description="coinflip command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="coinflip game",inline=False)
                help_embed.add_field(name="aliases",value="cf",inline=False)
                help_embed.add_field(name="usage",value="l coinflip <amount> <side>",inline=False)


            elif command == "top":
                help_embed = discord.Embed(title="top",description="top command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="shows the top 10 players",inline=False)
                help_embed.add_field(name="aliases",value="t",inline=False)
                help_embed.add_field(name="usage",value="l top",inline=False)


            elif command == "rps":
                help_embed = discord.Embed(title="rps",description="rps command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="rock paper scissors game",inline=False)
                help_embed.add_field(name="aliases",value="rockpaperscissors",inline=False)
                help_embed.add_field(name="usage",value="l rps <amount> <choice>",inline=False)


            elif command == "guess":
                help_embed = discord.Embed(title="guess",description="guess command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="guess a number between 1 and 10",inline=False)
                help_embed.add_field(name="aliases",value="gss",inline=False)
                help_embed.add_field(name="usage",value="l guess <amount> <number>",inline=False)


            elif command == "farouk":
                help_embed = discord.Embed(title="farouk",description="farouk command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="farouk game",inline=False)
                help_embed.add_field(name="aliases",value="fk",inline=False)
                help_embed.add_field(name="usage",value="l farouk <amount> <choice>",inline=False)


            #---------------------fun---------------------
            elif command == "ask":
                help_embed = discord.Embed(title="ask",description="ask command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="ask the bot a question",inline=False)
                help_embed.add_field(name="aliases",value="question",inline=False)
                help_embed.add_field(name="usage",value="l ask <question>",inline=False)


            elif command == "question":
                help_embed = discord.Embed(title="question",description="question command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="ask the bot a question",inline=False)
                help_embed.add_field(name="aliases",value="ask",inline=False)
                help_embed.add_field(name="usage",value="l question <question>",inline=False)


            elif command == "hikma":
                help_embed = discord.Embed(title="hikma",description="hikma command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="shows a hikma",inline=False)
                help_embed.add_field(name="aliases",value="hk",inline=False)
                help_embed.add_field(name="usage",value="l hikma",inline=False)


            elif command == "tod":
                help_embed = discord.Embed(title="tod",description="tod command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="shows the tod",inline=False)
                help_embed.add_field(name="aliases",value="t",inline=False)
                help_embed.add_field(name="usage",value="l tod",inline=False)


            elif command == "memic":
                help_embed = discord.Embed(title="memic",description="memic command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="shows a memic",inline=False)
                help_embed.add_field(name="aliases",value="m",inline=False)
                help_embed.add_field(name="usage",value="l memic",inline=False)


            #---------------------other---------------------
            elif command == "math":
                help_embed = discord.Embed(title="math",description="math command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="do a math equation",inline=False)
                help_embed.add_field(name="aliases",value="m",inline=False)
                help_embed.add_field(name="usage",value="l math <equation>",inline=False)


            elif command == "feedback":
                help_embed = discord.Embed(title="feedback",description="feedback command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="send a feedback to the developers",inline=False)
                help_embed.add_field(name="aliases",value="fb",inline=False)
                help_embed.add_field(name="usage",value="l feedback <feedback>",inline=False)


            elif command == "specialthanks":
                help_embed = discord.Embed(title="specialthanks",description="specialthanks command",color=discord.Color.blue())
                help_embed.add_field(name="description",value="specialthanks command",inline=False)
                help_embed.add_field(name="aliases",value="special , thanks",inline=False)
                help_embed.add_field(name="usage",value="l specialthanks",inline=False)


            else:
                help_embed = discord.Embed(title="error",description="invalid command",color=discord.Color.red())

                

"""