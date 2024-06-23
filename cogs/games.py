import discord
from discord.ext import commands
from discord.ui import Button , View
import json
import asyncio
import random
from bot_tools import *

class rps_buttons(discord.ui.View):
     
    def __init__(self):
        super().__init__()
        
    
    value : str = None
    

    @discord.ui.button(label="rock", style=discord.ButtonStyle.green)
    async def rock(self, interaction: discord.Interaction , button: discord.ui.Button):

        await interaction.response.send_message("you chose rock 🪨 !")
        self.value = "rock"
        self.stop()

    @discord.ui.button(label="paper", style=discord.ButtonStyle.green)
    async def paper(self, interaction: discord.Interaction , button: discord.ui.Button):
        await interaction.response.send_message("you chose paper 📄 !")
        self.value = "paper"
        self.stop()

    @discord.ui.button(label="scissors", style=discord.ButtonStyle.green)
    async def scissors(self, interaction: discord.Interaction , button: discord.ui.Button):
        await interaction.response.send_message("you chose scissors ✂️ !")
        self.value = "scissors"
        self.stop()

class games(commands.Cog):
    def __init__(self,laymouna):
        self.laymouna = laymouna
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("games.py is ready !")

            

    @commands.cooldown(1 , per = 60 , type = commands.BucketType.user)
    @commands.command(aliases=["n"])
    async def navigui(self , ctx , member:discord.Member=None):
        
        user_lem = get_user_lemons(ctx.author)

        
        amount = random.randint(-10 , 30)
        user_lem += amount

        if amount < 0 :
            lem_embed = discord.Embed(title="Nooooooooo sadfek didin !",description=f"hakmek b sator f trig sheraton w dalek {(-1)*amount} 🍋",color=discord.Color.red())
            lem_embed.add_field(name="hada wech b9alek : ", value=f"{user_lem} 🍋", inline=False)
            lem_embed.set_footer(text="tn7chatlek wlid houmtiiii hh" , icon_url=None)

        elif amount > 0 :
            lem_embed = discord.Embed(title="noiiice ! rahi zahya !",description=f"rak naviguit {amount} 🍋",color=discord.Color.green())
            lem_embed.add_field(name="wlaw 3ndk : ", value=f"{user_lem} 🍋", inline=False)
            lem_embed.set_footer(text="chikouuuur wlid houmtiiiii" , icon_url=None)


        elif amount == 0 :
            lem_embed = discord.Embed(title="ma naviguit ma chkoupi !",description="marahich ga3 takoul .. madekhelt walou",color=discord.Color.light_gray())
            lem_embed.set_footer(text="damn wlid houmtiiii.. rahi nachfa .." , icon_url=None)

        await ctx.send(embed = lem_embed)

        set_user_lemons(ctx.author , user_lem)

    @navigui.error
    async def navigui_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            await ctx.send(f"zid estena {error.retry_after} seconds ..")
    


    @commands.cooldown(1 , per = 600 , type=commands.BucketType.user)
    @commands.command(aliases=["lkhedma","khedma" ,"w"])
    async def work(self , ctx):

        user_lem = get_user_lemons(ctx.author)

        amount = random.randint(100,300)

        user_lem += amount

        lem_embed = discord.Embed(title="phew ! ",description="harimna ya chkp",color=discord.Color.green())
        lem_embed.add_field(name="lfayda : ", value=f"{amount} 🍋", inline=False)
        lem_embed.add_field(name="wlaw 3endek : ", value=f"{user_lem} 🍋", inline=False)
        lem_embed.set_footer(text="lkhedma is done , b9atlek slat w riyada hbb" , icon_url=None)

        set_user_lemons(ctx.author , user_lem)

        await ctx.send(embed = lem_embed)

    @work.error
    async def on_command_error(sefl , ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            em = discord.Embed(title=f"Slow it down wlid houmtiii!",description=f"3awed seyi mor : {int(error.retry_after/60)}m.",color=discord.Color.red() )
            err_msg = await ctx.send(embed=em)
            await asyncio.sleep(5)
            await err_msg.delete()



    @commands.cooldown(1 , per = 10 , type=commands.BucketType.user)
    @commands.command()
    async def gamble(self,ctx,amount=None):

        amount = right_amount(ctx , amount) 
            
        if amount < 0 :
            await ctx.send("u can't gamble negative lemons !")
        else :

            user_lem = get_user_lemons(ctx.author)

            if amount > user_lem :

                await ctx.send("you don't have enough lemons ! ya lhsnawi talab")

            else :

                user_strikes = random.randint(1,15)
                laymouna_strikes = random.randint(5,15)

                if user_strikes > laymouna_strikes :

                    percentage = random.randint(50,100)
                    amount_won = int(amount*(percentage/100))

                    user_lem += amount_won
                    

                    win_embed = discord.Embed(description=f"you won {amount_won} 🍋 !\n percentge = {percentage}% \n new balance : { user_lem }",color=discord.Color.green())
                    win_embed.add_field(name=f"{ctx.author.name}",value=f"strikes : {user_strikes}")
                    win_embed.add_field(name="laymouna",value=f"strikes : {laymouna_strikes}")

                    
                    await ctx.send(embed=win_embed)
                elif user_strikes < laymouna_strikes :

                    percentage = random.randint(0,80)
                    amount_lost = int(amount*(percentage/100))

                    user_lem -= amount_lost

                    loss_embed = discord.Embed(description=f"oh no ! you lost {amount_lost} 🍋 !\n percentge = {percentage}% \n new balance : { user_lem } ",color=discord.Color.red())
                    loss_embed.add_field(name=f"{ctx.author.name}",value=f"strikes : {user_strikes}")
                    loss_embed.add_field(name="laymouna",value=f"strikes : {laymouna_strikes}")

            
                    await ctx.send(embed = loss_embed)
                
                else:
                    tie_embed = discord.Embed(description=f"it was a tie !",color=discord.Color.light_grey())
                    tie_embed.add_field(name=f"{ctx.author.name}",value=f"strikes : {user_strikes}",inline=False)
                    tie_embed.add_field(name="laymouna",value=f"strikes : {laymouna_strikes}",inline=False)

                    await ctx.send("aaaa")
                    await ctx.send(embed=tie_embed)

                set_user_lemons(ctx.author , user_lem)
    
    @gamble.error
    async def on_command_error(sefl , ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            em = discord.Embed(title=f"Slow it down wlid houmtiii!",description=f"3awed seyi mor : {int(error.retry_after)}s.",color=discord.Color.red() )
            err_msg = await ctx.send(embed=em)
            await asyncio.sleep(5)
            await err_msg.delete()

    
    @commands.cooldown(1, 0, commands.BucketType.user)
    @commands.command(aliases=["cf"])
    async def coinflip (self,ctx,amount=None):

        user_lem = get_user_lemons(ctx.author)
        amount = right_amount(ctx , amount) 


        if amount <= 0 :
            await ctx.send("u can't gamble negative lemons !")
        else :

            if amount > user_lem :

                await ctx.send("you don't have enough lemons ! ya lhsnawi talab")

            else :

                coin = random.randint(1,2)

                if coin == 1 :

                    user_lem += amount

                    await ctx.send("u won")

                    win_embed = discord.Embed(title="coinflip" , description=f"{ctx.author.name} bet {amount} 🍋 \n and won {amount * 2} 🍋 " , color=discord.Color.green())
                    win_embed.set_footer(text="congratulations ! bashtek hbb")

                    await ctx.send(embed = win_embed)
                
                else:

                    user_lem -= amount

                    await ctx.send("u lost")

                    loss_embed = discord.Embed(title="coinflip" , description=f"{ctx.author.name} bet {amount} 🍋 \n and lost everythin 🍋", color=discord.Color.red())
                    loss_embed.set_footer(text="hhhhhhhhhh k3ba")

                    await ctx.send(embed = loss_embed)

        
        set_user_lemons(ctx.author , user_lem)

    @coinflip.error
    async def on_command_error(sefl , ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            em = discord.Embed(title=f"Slow it down !",description=f"try after : {int(error.retry_after)}s.",color=discord.Color.red() )
            err_msg = await ctx.send(embed=em)
            await asyncio.sleep(5)
            await err_msg.delete()



    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    @commands.command(aliases=["f"])
    async def farouk(self,ctx,amount=None):


        amount = right_amount(ctx , amount) 

        


        if amount < 0 :
            await ctx.send("you can't bet negative numbers !")
        else :
         
            user_lem = get_user_lemons(ctx.author)

            if amount > user_lem :

                await ctx.send("you don't have enough lemons ! ya lhsnawi talab")

            else :

                user_lem -= amount

                rate = random.randint(1,10)
                await ctx.send(f"you bet {amount} 🍋 at a rate of {rate} !")
                win_loss = random.randint(1,2)
                
                if win_loss == 1 :
                    user_lem += amount*rate
                    await ctx.send(f"you won {amount*rate} 🍋 !")

                else:
                    user_lem += amount
                    user_lem -= int(amount/rate)
                    await ctx.send(f"you lost {int(amount/rate)} 🍋 !")

                set_user_lemons(ctx.author , user_lem)

    @farouk.error
    async def on_farouk_error(sefl , ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            em = discord.Embed(title=f"Slow it down wlid houmtiii!",description=f"3awed seyi mor : {int(error.retry_after)}s.",color=discord.Color.red() )
            err_msg = await ctx.send(embed=em)
            await asyncio.sleep(5)
            await err_msg.delete()


    
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(aliases=["g"])
    async def guess(self,ctx,amount=None):
            
            amount = right_amount(ctx , amount)
            
            user_lem = get_user_lemons(ctx.author)
             
            if amount < 0 :
                await ctx.send("you can't bet negative numbers !")

            elif amount > user_lem :
                await ctx.send("you don't have enough lemons ! ya lhsnawi talab")
                
            else :
            
                
    
                number = random.randint(1,100)
                tries = 5
                await ctx.send(f"you bet {amount} 🍋 !")

                await ctx.send("guess a number between 1 and 100 !")

                
                while tries > 0 :

                    
                    while True :
                        guess = await self.laymouna.wait_for("message" , check=lambda message: message.author == ctx.author)
                        if guess.content.isdigit() :
                            guess = int(guess.content)
                            break
                        else :
                            err = await ctx.send("enter a number ! :unamused: ")
                            await asyncio.sleep(4)
                            await err.delete()


                    
                        
                    
                    if guess == number :
                        await ctx.send(f"congratulations ! you won {amount*tries} 🍋 !")
                        user_lem += amount*(tries+1)
                        break
                    elif guess > number :
                        await ctx.send(f"the number is lower than {guess} !")
                        
                    elif guess < number :
                        await ctx.send(f"the number is higher than {guess} !")
                    
                    tries -= 1
                    
                if tries == 0 :
                    user_lem -= amount
                    await ctx.send(f"you lost ! the number was {number}")

                set_user_lemons(ctx.author , user_lem)

    @guess.error
    async def on_guess_error(sefl , ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            em = discord.Embed(title=f"Slow it down !",description=f"try after : {int(error.retry_after)}s.",color=discord.Color.red() )
            err_msg = await ctx.send(embed=em)
            await asyncio.sleep(5)
            await err_msg.delete()

   
    @commands.command(aliases=["rock" , "paper" , "scissors"])
    async def rps(self,ctx,amount=None):
        
        amount = right_amount(ctx , amount)

    
        if amount < 0 :
            await ctx.send("you can't bet negative numbers !")
        else :
            
            user_lem = get_user_lemons(ctx.author)

            if amount > user_lem :

                await ctx.send("you don't have enough lemons ! ya lhsnawi talab")

            else :

                user_lem -= amount

                await ctx.send(f"you bet {amount} 🍋 !")
                await ctx.send("choose one :")

                rps_view = rps_buttons()
                
                await ctx.send(view=rps_view)
                await rps_view.wait()
                
                
                    
                #to check
                def check(res):
                    return ctx.author == res.user and res.channel == ctx.channel
                
                
                if rps_view.value == "rock" :
                    user_choice = 1
                elif rps_view.value == "paper" :
                    user_choice = 2
                elif rps_view.value == "scissors" :
                    user_choice = 3

                bot_choice = random.randint(1,3)

                if bot_choice == 1 :
                    await ctx.send("i chose rock 🪨 !")
                elif bot_choice == 2 :
                    await ctx.send("i chose paper 📄 !")
                elif bot_choice == 3 :
                    await ctx.send("i chose scissors ✂️ !")

                if user_choice == bot_choice :
                    await ctx.send("it's a tie !")
                    await ctx.send("you get your lemons back !")
                    user_lem += amount
                    
                elif user_choice == 1 and bot_choice == 2 :
                    await ctx.send("i won !")
                    await ctx.send(f"you lost {amount} 🍋 !")


                elif user_choice == 1 and bot_choice == 3 :
                    await ctx.send("you won !")
                    await ctx.send(f"you won {amount} 🍋 !")
                    user_lem += amount*2

                elif user_choice == 2 and bot_choice == 1 :
                    await ctx.send("you won !")
                    await ctx.send(f"you won {amount} 🍋 !")
                    user_lem += amount*2

                elif user_choice == 2 and bot_choice == 3 :
                    await ctx.send("i won !")
                    await ctx.send(f"you lost {amount} 🍋 !")

                elif user_choice == 3 and bot_choice == 1 :
                    await ctx.send("i won !")
                    await ctx.send(f"you lost {amount} 🍋 !")

                elif user_choice == 3 and bot_choice == 2 :
                    await ctx.send("you won !")
                    await ctx.send(f"you won {amount} 🍋 !")
                    user_lem += amount*2

                    

                set_user_lemons(ctx.author , user_lem)



    



async def setup(laymouna):
    await laymouna.add_cog(games(laymouna))

