import json
import discord
from discord.ext import commands
import random
from aiohttp import request
import asyncio
import requests
from bot_tools import *
from config import nasa_api_key
from gemini import generate_response

party = []
last_chosen = []

class choose(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)
        

    @discord.ui.button(label="truth",style=discord.ButtonStyle.green)
    async def truth(self, interaction: discord.Interaction , button : discord.ui.Button):
        
        # get a random truth from an api
        url = "https://api.truthordarebot.xyz/v1/truth"

        async with request("GET",url) as response:
            if response.status == 200:
                data = await response.json()
                response = data["question"]
            else:
                response = "error in the api request ! try again later or report the bug to the developer"
                #show the error message in the console
                await interaction.channel.send(response)
                await interaction.channel.send(response.text)
                return
        
        await interaction.channel.send("u chose truth !")
        await interaction.channel.send(response)
        await interaction.message.edit(view=None)
        

    @discord.ui.button(label="dare",style=discord.ButtonStyle.red)
    async def dare(self, interaction: discord.Interaction , button : discord.ui.Button):
        
        # get a random dare from an api
        url = "https://api.truthordarebot.xyz/api/dare"
        

        async with request("GET",url) as response:
            if response.status == 200:
                data = await response.json()
                response = data["question"]
            else:
                response = "error in the api request ! try again later or report the bug to the developer"
                #show the error message in the console
                await interaction.channel.send(response)
                await interaction.channel.send(response.text)
                return
        
        await interaction.channel.send("u chose dare !")
        await interaction.channel.send(response)
        await interaction.message.edit(view=None)
        

    @discord.ui.button(label="random",style=discord.ButtonStyle.gray)
    async def random(self, interaction: discord.Interaction , button : discord.ui.Button):
        ran = random.randint(1,2)
        if ran == 1 :
            
            url = "https://api.truthordarebot.xyz/v1/truth"

            async with request("GET",url) as response:
                if response.status == 200:
                    data = await response.json()
                    response = data["question"]
                else:
                    response = "error in the api request ! try again later or report the bug to the developer"
                    
                    await interaction.channel.send(response)
                    await interaction.channel.send(response.text)
                    return
            
            await interaction.channel.send("it landed on truth !")
            await interaction.channel.send(response)
            await interaction.message.edit(view=None)

        else :
            
            url = "https://api.truthordarebot.xyz/api/dare"

            async with request("GET",url) as response:
                if response.status == 200:
                    data = await response.json()
                    response = data["dare"]
                else:
                    response = "error in the api request ! try again later or report the bug to the developer"
                    
                    await interaction.channel.send(response)
                    await interaction.channel.send(response.text)
                    return

            await interaction.channel.send("it landed on dare !")
            await interaction.channel.send(response)
            await interaction.message.edit(view=None)           

class fun(commands.Cog):
    def __init__(self,laymouna):
        self.laymouna = laymouna
    
        
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("fun.py is ready !")



    
    #---------------------------------------#
    
    @commands.command(aliases = ["q","book of questions","boq"])
    async def question(self ,ctx):
        with open("files/the_book_of_questions.txt","r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)
        await ctx.send(response)

    @commands.command(aliases = ["quote"])
    async def hikma(self ,ctx):
        
        url = "https://api.quotable.io/random"

        async with request("GET",url) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(f"{data['content']}\n- {data['author']}")
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")
                #show the error message in the console
                await ctx.send(response.text)

    @commands.command()
    async def tod (self , ctx ):

        if ctx.author != ctx.message.author:
            await ctx.send("you're not the one who used the command !", ephemeral = True)
        else :

            tod_button = choose()
            await ctx.send("choose one :", view = tod_button)


    @commands.command(aliases = ["8b" , "hmmm" ])
    async def ask(self ,ctx, *, question):
        response = generate_response(question)
        await ctx.send(response)


    @commands.command(aliases = [])
    async def bored(self ,ctx,):

        url = "https://www.boredapi.com/api/activity/"

        async with request("GET",url) as response:
            if response.status == 200:
                data = await response.json()
                
                await ctx.send(data["activity"])
                await ctx.send(f"type : {data['type']}")
                await ctx.send(f"participants : {data['participants']}")

                if data["link"] != "":
                    await ctx.send(f"link : {data['link']}")
                
                
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")


    @commands.command(aliases = ["morse"])
    async def tomorse(self ,ctx, *, text):
        text = text.lower()
        morse = ""
        
        url = "https://api.funtranslations.com/translate/morse.json"

        async with request("POST",url,data={"text":text}) as response:
            if response.status == 200:
                data = await response.json()
                morse = data["contents"]["translated"]
                await ctx.send(morse)
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")

    @commands.command(aliases = ["binary"])
    async def tobinary(self ,ctx, *, text):
        text = text.lower()
        binary = ""
        
        url = "https://api.funtranslations.com/translate/binary.json"

        async with request("POST",url,data={"text":text}) as response:
            if response.status == 200:
                data = await response.json()
                binary = data["contents"]["translated"]
                await ctx.send(binary)
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")

    @commands.command(aliases = ["hex"])
    async def tohex(self ,ctx, *, text):
        text = text.lower()
        hexa = ""
        
        url = "https://api.funtranslations.com/translate/hex.json"

        async with request("POST",url,data={"text":text}) as response:
            if response.status == 200:
                data = await response.json()
                hexa = data["contents"]["translated"]
                await ctx.send(hexa)
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")

    @commands.command(aliases = ["text"])
    async def totext(self ,ctx, *, text):
        # recieves a morse or binary or hex code and converts it to text

        text = text.lower()
        

        if text.__contains__(".") or text.__contains__("-"):
            url = "https://api.funtranslations.com/translate/morse2english.json"


            async with request("POST",url,data={"text":text}) as response:
                if response.status == 200:
                    data = await response.json()
                    text = data["contents"]["translated"]
                    await ctx.send(text)
                else:
                    await ctx.send("error in the api request ! try again later or report the bug to the developer")

        elif text.__contains__("0") or text.__contains__("1"):

            url = "https://api.funtranslations.com/translate/binary2text.json"

            async with request("POST",url,data={"text":text}) as response:
                if response.status == 200:
                    data = await response.json()
                    text = data["contents"]["translated"]
                    await ctx.send(text)
                else:
                    await ctx.send("error in the api request ! try again later or report the bug to the developer")


            """elif text.__contains__("a") or text.__contains__("b") or text.__contains__("c") or text.__contains__("d") or text.__contains__("e") or text.__contains__("f"):
                url = "https://api.funtranslations.com/translate/hex2text.json"

                async with request("POST",url,data={"text":text}) as response:
                    if response.status == 200:
                        data = await response.json()
                        text = data["contents"]["translated"]
                        await ctx.send(text)
                    else:
                        await ctx.send("error in the api request ! try again later or report the bug to the developer")
            """
        
        else:
        
            await ctx.send("invalid input ! it should be a morse or binary or hex code")


    @commands.command(aliases = [])
    async def yoda(self ,ctx, *, text):
        url = "https://api.funtranslations.com/translate/yoda.json"

        async with request("POST",url,data={"text":text}) as response:
            if response.status == 200:
                data = await response.json()
                text = data["contents"]["translated"]
                await ctx.send(text)
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")
                #show the error message in the console
                await ctx.send(response.text)

    @commands.command(aliases = [])
    async def number(self ,ctx, *, number: int):
        # recieves a number and gives interesting number facts.

        # recieves the type of fact the user wants
        await ctx.send("choose the type of fact u want : \n1 - trivia \n2 - math \n3 - date \n4 - year")
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        
        try:
            msg = await self.laymouna.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("u took too long to respond !")
        else:
            if msg.content == "1":
                type = "trivia"
            elif msg.content == "2":
                type = "math"
            elif msg.content == "3":
                type = "date"
            elif msg.content == "4":
                type = "year"
            else:
                await ctx.send("invalid input !")
                return

            url = f"http://numbersapi.com/{number}/{type}"

            async with request("GET",url) as response:
                if response.status == 200:
                    data = await response.text()
                    await ctx.send(data)
                else:
                    await ctx.send("error in the api request ! try again later or report the bug to the developer")
                    #show the error message in the console
                    await ctx.send(response.text)

    @commands.command(aliases = [])
    async def nasa (self , ctx):
        
        # recieves the type of fact the user wants
        await ctx.send("choose the type of fact u want : \n1 - apod \n2 - moon \n3 - epic \n4 - i've abondoned this idea after 7 hours of work cuz fuck la nasa and it's shitty api li maymedch meme pas nrml pics ki nas \n5 - العاعاعوط" )

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        
        try:
            msg = await self.laymouna.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("u took too long to respond !")
        else:
            if msg.content == "0":
                url = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={nasa_api_key}"
            elif msg.content == "1":
                url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}"
            elif msg.content == "2":
                url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={nasa_api_key}"
            elif msg.content == "3":
                url = f"https://api.nasa.gov/planetary/earth/assets?lon=100.75&lat=1.5&date=2014-02-01&&api_key={nasa_api_key}"
            elif msg.content == "4":
                url = None
            elif msg.content == "5":
                url = None
            



            else:
                await ctx.send("invalid input !")
                return
            


            if url != None:

                async with request("GET",url) as response:
                    if response.status == 200:
                        data = await response.json()


                        if msg.content == "1":
                            embed = nasa_apod_embed(data)
                        elif msg.content == "0":

                            i = random.randint(0,len(data)-1)
                            data = data[i]

                            #lon = data["centroid_coordinates"]["lon"]
                            #lat = data["centroid_coordinates"]["lat"]
                            #date = data["date"]
                            # convert date to yyyy-mm-dd
                            #date = date[0:4] + "-" + date[5:7] + "-" + date[8:10]

                            #get random lon , lat , date
                            lon = random.randint(-180,180)
                            lat = random.randint(-90,90)
                            date = f"{random.randint(2015,2021)}-{random.randint(1,12)}-{random.randint(1,28)}"

                            print(lon)
                            print(lat)
                            print(date)


                            img_url = f"https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&date={date}&dim=0.10&api_key={nasa_api_key}"


                            async with aiohttp.request("GET",img_url) as response:

                                if response.status == 200:
                                    print("im here 2 !")
                                    img = await response.json()
                                    print(img)
                                else:
                                    img = None
                            
                            embed = nasa_earth_embed(data,img)
                        elif msg.content == "2":

                            i = random.randint(0,len(data["photos"])-1)
                            data = data["photos"][i]

                            embed = nasa_moon_embed(data)
                        elif msg.content == "3":
        
                                embed = nasa_epic_embed(data)
                    
                    else:
                        await ctx.send("error in the api request ! try again later or report the bug to the developer")
                    
                    
            else:
                
                if msg.content == "4":
                        await ctx.send("yak 9oulna mafihech .. matforcich lmektoub")
                        return
                    
                elif msg.content == "5":

                    embed = l3a3a3out()

                        

                    
            await ctx.send(embed = embed)

    
    @commands.command(aliases = ["yomama"])
    async def yomoma(self ,ctx):
        
        url = f"https://api.yomomma.info/"

        async with request("GET",url) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["joke"])
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")
                #show the error message in the console
                await ctx.send(response.text)     

    @commands.command(aliases = [])
    async def roast(self ,ctx,*,user : discord.Member = None):
        
        if user == None:
            user = ctx.author

        url = f"https://evilinsult.com/generate_insult.php?lang=en&type=json"

        # generate a roast then test if the roast contains bad words and if it does , generate another one

        while True:
            
            async with request("GET",url) as response:
                if response.status == 200:
                    data = await response.json()
                    roast = data["insult"]
                    if not bad_words(roast):
                        
                        await ctx.send(f"{user.mention} {roast}")
                        break
                    

                else:
                    await ctx.send("error in the api request ! try again later or report the bug to the developer")
                    #show the error message in the console
                    await ctx.send(response.text) 
                    return
                
                

    @commands.command(aliases = [])
    async def useless(self ,ctx):
        
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random"

        async with request("GET",url) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(f"[useless fact] : {data['text']}")
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")
                #show the error message in the console
                await ctx.send(response.text)   

    @commands.command(aliases = [])
    async def joke(self ,ctx):
        
        url = "https://official-joke-api.appspot.com/random_joke"

        async with request("GET",url) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(f"{data['setup']}\n{data['punchline']}")
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")
                #show the error message in the console
                await ctx.send(response.text)

    @commands.command(aliases = [])
    async def meme(self ,ctx):
        
        #url = "https://some-random-api.ml/meme"
        url = None

        async with request("GET",url) as response:
            if response.status == 200:
                data = await response.json()

                print(data)
                
                embed = discord.Embed(title = None, color = discord.Color.blue())
                embed.set_image(url = data["image"])
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")
                #show the error message in the console
                await ctx.send(response.text)

    


    @commands.command(aliases = ["thisorthat","tot","wyr"])
    async def wouldyourather(self ,ctx,):
        
        url = f"https://api.truthordarebot.xyz/api/wyr"

        async with request("GET",url) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(f"{data['question']}")
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")
                #show the error message in the console
                await ctx.send(response.text)

    @commands.command(aliases = ["nhie","neverhaveiever","never"])
    async def never_have_i_ever(self ,ctx):

        url = "https://api.truthordarebot.xyz/api/nhie"

        async with request("GET",url) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(f"{data['question']}")
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")
                #show the error message in the console
                await ctx.send(response.text)


    @commands.command(aliases = ["para"])
    async def paranoia(self ,ctx):
        
        url = "https://api.truthordarebot.xyz/api/paranoia"

        async with request("GET",url) as response:

            if response.status == 200:
                data = await response.json()
                await ctx.send(f"{data['question']}")
            else:
                await ctx.send("error in the api request ! try again later or report the bug to the developer")
                await ctx.send(response.text)
        
        
    @commands.command(aliases = ["t","team","teams","tms","tm"])
    async def party(self ,ctx,options = None):
        

        if options == None:
            if len(party) == 0:
                await ctx.send("there's no one in the party !")
            else:
                

                await ctx.send("------------------------------")
                await ctx.send("people playing rn :")
                for i in party:
                    await ctx.send(f"{i.name}")
                await ctx.send("------------------------------")
                await ctx.send(f"total : {len(party)}")
                await ctx.send("to join the party , use the command ** l party join ** !")
            
        elif options == "join":

            if ctx.author in party:
                
                await ctx.send("u're already in the party !")
            else:
                
                party.append(ctx.author)
                
                await ctx.send("u've joined the party !")

        elif options == "leave" or options == "quit":
                if ctx.author in party:
                    party.remove(ctx.author)
                    await ctx.send("u've left the party !")
                else:
                    await ctx.send("u're not in the party !")

        elif options == "random":
            if len(party) == 0:
                await ctx.send("there's no one in the party !")
            else:
                # choose a random person from the party that hasn't been chosen the last time
                while True and len(party) > 1:
                    i = random.randint(0,len(party)-1)
                    if party[i] not in last_chosen:
                        last_chosen.clear()
                        last_chosen.append(party[i])
                        break
                await ctx.send(f"{party[i].mention} has been chosen !")
        else:
            await ctx.send("invalid option !")
        
                


    @commands.command(aliases = ["sup"])
    @commands.has_permissions(administrator = True)
    async def superparty(self ,ctx,* , args):
        
        # args = option user
        # option = clear , kick , add
        # user = member

        args = args.split(" ")
        option = args[0]
        user = None
        if len(args) == 2:
            user = await commands.MemberConverter().convert(ctx, args[1])
        elif len(args) > 2:
            await ctx.send("invalid input !")
            return
        



        # if user == None check the option

        if user == None:
            if option == None:
                await ctx.send("u need to specify an option !")
                return
            
            elif option == "clear":
                party.clear()
                await ctx.send("the party has been cleared !")
            else:
                await ctx.send("invalid option !")
                return
        else:
            if option == None:
                await ctx.send("u need to specify an option !")
                return
            elif option == "kick":
                if user in party:
                        
                    party.remove(user)
                    await ctx.send(f"{user.mention} has been kicked from the party !")
                    
                else:
                    await ctx.send("u're not in the party !")

            elif option == "add":
                if user in party:
                    await ctx.send("u're already in the party !")
                else:
                    
                    party.append(user)
                    
                    await ctx.send(f"{user.mention} has been added to the party !")
            
            else:
                await ctx.send("invalid option !")
                return
        
        
        
    






        



























































    #a command that talks like the person who used it
    @commands.command(aliases = ["talk"])
    async def memic(self ,ctx, *, question):
        await ctx.send(question)

    
    
            



async def setup(laymouna):
    await laymouna.add_cog(fun(laymouna))