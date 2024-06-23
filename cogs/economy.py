import discord
from discord.ext import commands
import json
import random
from bot_tools import *




class economy(commands.Cog):
    def __init__(self,laymouna):
        self.laymouna = laymouna

    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("economy.py is ready !")


    @commands.command(aliases=["money" , "balance" , "cash" , "lemons" , "l"])
    async def lemon(self , ctx , member:discord.Member=None):

        if member == None:
            member=ctx.author
        elif member is not None:
            member = member

        user_lemons = get_user_lemons(member)
        user_bank = getUserBank(member)

        
        eco_embed = discord.Embed(title=f"{member.name}'s current lemons :", description="dak chi li kayen ..",color=discord.Color.green())
        eco_embed.add_field(name="current lemons : ", value=f"{user_lemons} 🍋")
        eco_embed.add_field(name="bank", value=f"{user_bank} 🍋 ", inline=False)
        eco_embed.set_footer(text="note : matmedhoumch l farouk ..", icon_url=None)
        
        await ctx.send(embed=eco_embed)

         

    @commands.command()
    async def give (self , ctx , member:discord.User ,amount=None):

        amount = right_amount(ctx , amount) 

        if member == ctx.author :
            await ctx.send("u want to give lemons to yourself ? harech harech ..")
        elif amount < 0 :
             await ctx.send("u can't give negative lemons !")
        else :
                
                user_lem = get_user_lemons(ctx.author)
                member_lem = get_user_lemons(member)

                if user_lem >= amount:

                    user_lem -= amount
                    member_lem += amount                           
                
                    set_user_lemons(ctx.author , user_lem)
                    set_user_lemons(member , member_lem)
            
                    await ctx.reply("transaction complete \n" + f"{ctx.author.name} gave {amount} 🍋 to {member.name}")

                else : await ctx.send("u don't have this much lemons")



    @commands.command( aliases=["top"])
    async def leaderboard(self,ctx,cat=None):
             
            """show top 10 richest people in the curent server"""

            if cat == "lemon":

                server = ctx.guild    
                server_lem = {}

                for member in server.members:
                    if not member.bot:
                        if user_exists(member):
                            server_lem[str(member.id)] = get_user_lemons(member)
                        

                sorted_lem = sorted(server_lem.items(), key=lambda x: x[1], reverse=True)

                lem_embed = discord.Embed(title="leaderboard", description="based on lemons", color=discord.Color.gold())

                for i in range(10):
                    try:
                        id = sorted_lem[i][0]
                        member = server.get_member(int(id))
                        name = member.name
                        lem = sorted_lem[i][1]
                        lem_embed.add_field(name=f"{i+1}. {name}", value=f"{lem} 🍋", inline=False)
                    except:
                        pass

                await ctx.send(embed=lem_embed)

            elif cat == "bank":
                server = ctx.guild    
                server_bank = {}

                for member in server.members:
                    if not member.bot:
                        if user_exists(member):
                            server_bank[str(member.id)] = getUserBank(member)
                        

                sorted_bank = sorted(server_bank.items(), key=lambda x: x[1], reverse=True)

                bank_embed = discord.Embed(title="leaderboard", description="based on bank", color=discord.Color.gold())

                for i in range(10):
                    try:
                        id = sorted_bank[i][0]
                        member = server.get_member(int(id))
                        name = member.name
                        bank = sorted_bank[i][1]
                        bank_embed.add_field(name=f"{i+1}. {name}", value=f"{bank} 🍋", inline=False)
                    except:
                        pass

                await ctx.send(embed=bank_embed)
            
            elif cat == "level" or cat == "lvl":
                server = ctx.guild    
                server_level = {}

                for member in server.members:
                    if not member.bot:
                        if user_exists(member):
                            server_level[str(member.id)] = get_user_level(member)
                        

                sorted_level = sorted(server_level.items(), key=lambda x: x[1], reverse=True)

                level_embed = discord.Embed(title="leaderboard", description="based on level", color=discord.Color.gold())

                for i in range(10):
                    try:
                        id = sorted_level[i][0]
                        member = server.get_member(int(id))
                        name = member.name
                        level = sorted_level[i][1]
                        level_embed.add_field(name=f"{i+1}. {name}", value=f"{level} 🍋", inline=False)
                    except:
                        pass

                await ctx.send(embed=level_embed)

            elif cat == None:
                """shows the leaderboard of the server based on net worth (lemons + bank)"""
                server = ctx.guild
                server_net = {}
                for member in server.members:
                    if not member.bot:
                        if user_exists(member):
                            server_net[str(member.id)] = get_user_lemons(member) + getUserBank(member)

                sorted_net = sorted(server_net.items(), key=lambda x: x[1], reverse=True)

                net_embed = discord.Embed(title="leaderboard", description="based on net worth", color=discord.Color.gold())

                for i in range(10):
                    try:
                        id = sorted_net[i][0]
                        member = server.get_member(int(id))
                        name = member.name
                        net = sorted_net[i][1]
                        net_embed.add_field(name=f"{i+1}. {name}", value=f"{net} 🍋", inline=False)
                    except:
                        pass

                await ctx.send(embed=net_embed)

            else:
                await ctx.send("invalid category !")


    
    
    @commands.command(aliases=[])
    async def deposit(self,ctx,amount=None):

        amount = right_amount(ctx , amount)

        if amount < 0 :
            await ctx.send("you can't deposit negative numbers !")
        else :
   
            user_lem = get_user_lemons(ctx.author)
            user_bank = getUserBank(ctx.author)

            if amount > user_lem :

                await ctx.send("you don't have enough lemons ! ya lhsnawi talab")

            else :

                user_lem -= amount
                user_bank  += amount

                set_user_lemons(ctx.author , user_lem)
                setUserBank(ctx.author , user_bank)

                await ctx.send(f"you deposited {amount} 🍋 !")


    @commands.command(aliases=["with"])
    async def withdraw(self,ctx,amount=None):
            
            amount = right_amount(ctx , amount)
             
            if amount < 0 :
                await ctx.send("you can't withdraw negative numbers !")
            else :
            
                user_lem = get_user_lemons(ctx.author)
                user_bank = getUserBank(ctx.author)
    
                if amount > user_bank :
    
                    await ctx.send("you don't have enough lemons in your bank ! ya lhsnawi talab")
    
                else :
    
                    user_lem += amount
                    user_bank -= amount

                    set_user_lemons(ctx.author , user_lem)
                    setUserBank(ctx.author , user_bank)
    
                    await ctx.send(f"you withdrew {amount} 🍋 !")
    

    

    @commands.command(aliases=["steal"])
    async def rob(self,ctx,member:discord.Member):
             
            robber_lem = get_user_lemons(ctx.author)
            victim_lem = get_user_lemons(member)
    
            if member == ctx.author :
                await ctx.send("u want to steal from yourself ? harech harech ..")
            elif member.bot :
                await ctx.send("u can't steal from a bot !")
            else :
                if victim_lem < 2000 :
                    await ctx.send("this user doesn't have enough lemons to steal !")
                else :
                    if robber_lem < 2000 :
                        await ctx.send("you don't have enough lemons to steal !")
                    else :
                        if random.randint(0,1) == 0 :

                            robber_lem -= 2000
                            update_server_fine_box(ctx.guild , get_server_fine_box(ctx.guild) + 2000)
                            """send a dm to the victim"""
                            dm = await member.send(f"you got robbed by {ctx.author.name} in {ctx.guild} !\n they got caught !")

                            await ctx.send("you got caught !")
                            await ctx.send("you paid 2000 🍋 as a fine !")
                        else :
                            stolen = random.randint(100, victim_lem)
                            victim_lem -= stolen
                            robber_lem += stolen
                            await ctx.send(f"you stole {stolen} 🍋 !")
                            """send a dm to the victim"""
                            dm = await member.send(f"you got robbed by {ctx.author.name} in {ctx.guild} !\n they stole {stolen} 🍋 !")
                            
    
                        set_user_lemons(ctx.author , robber_lem)
                        set_user_lemons(member , victim_lem)

    @commands.command(aliases=["fine","fine_box","box"])
    async def finebox(self,ctx):
                 
        fine_box = get_server_fine_box(ctx.guild)

        fine_box_embed = discord.Embed(title="fine box", color=discord.Color.gold())
        fine_box_embed.add_field(name="the fine box containes", value=f"{fine_box} 🍋", inline=False)
        fine_box_embed.set_footer(text="yall are a bunch of dumbasses.. stop stealing from each other!")

        
        await ctx.send(embed = fine_box_embed)

    

         

    """to be changed"""
    @commands.command()
    @commands.cooldown(1, 60*60*24, commands.BucketType.user)
    async def daily(self,ctx):

        user = ctx.author

        if not user_exists(user):
            create_user(user)

        
        user_lem = get_user_lemons(user)
        user_streak = get_user_streak(user)
        
        user_lem += 1000 + user_streak*100
        user_streak += 1

        set_user_lemons(user,user_lem)
        set_user_streak(user,user_streak)

        daily_embed = discord.Embed(title="daily reward",description=f"you got {1000 + user_streak*100} 🍋 !",color=discord.Color.green())
        daily_embed.add_field(name="**streak**",value=f"your streak is now {user_streak} days 🔥 !",inline=False)
        daily_embed.set_footer(text=f"requested by <{ctx.author.name}>",icon_url=ctx.author.avatar)

        await ctx.send(embed=daily_embed)

    @daily.error
    async def on_error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            time = error.retry_after
            if time > 3600 :
                time = int (time/3600)
                cooldown_msg = await ctx.send(f"🚫 you have to wait {time} hours before you can claim your daily again !")

            elif time > 60 :
                time = int (time/60)
                cooldown_msg = await ctx.send(f"🚫 you have to wait {time} minutes before you can claim your daily again !")
            
            else :
                time = int (time)
                cooldown_msg = await ctx.send(f"🚫 you have to wait {time} seconds before you can claim your daily again !")

            await cooldown_msg.delete(delay=10)   
            
            
    @commands.command(aliases=["sfb","steal_finebox","steal finebox","steal fine box","stealbox"])
    @commands.cooldown(1, 18000, commands.BucketType.guild)
    async def stealfinebox (self , ctx):
         
        user_lem = get_user_lemons(ctx.author)
        fine_box = get_server_fine_box(ctx.guild)
        
        if fine_box == 0 :
            await ctx.send("the fine box is empty !") 
        elif user_lem > 500 :
            await ctx.send("you need at least 500 🍋 !") 
        else:
            """make a 5% chance if success at stealing the fine box"""
            chance = random.randint(1,100)
            if chance <= 5 :
                await ctx.send(f"you stole {fine_box} 🍋 from the fine box !")
                update_server_fine_box(ctx.guild,0)
                set_user_lemons(ctx.author,user_lem + fine_box)
            else:
                await ctx.send("you failed to steal the fine box ! you're now in jail for 5 hour !")

    @stealfinebox.error
    async def on_error(self,ctx,error):
        if error.isinstance(error, commands.CommandOnCooldown):
            try:
                time = int(error.retry_after)
                await ctx.send(f"you're in jail ! you'll get out in " + time_handler(time) + " !")    
            except Exception as e:
                print(e)
                await ctx.send(f"you're in jail ! you'll get out in {time} !")
                 
            


    @commands.command(aliases=[""])
    @commands.has_permissions(administrator=True)
    async def miw(self,ctx,amount=None,member:discord.Member=None):
                
        if member == None :
             member = ctx.author

        if ctx.author.id == 322164128280215564 :    
            amount = right_amount(ctx , amount)
            user_lem = get_user_lemons(member)
            user_lem += amount
            set_user_lemons(member , user_lem)
            await ctx.reply("tama l miw bi naja7")

        else :
            await ctx.send("u ain't ali .. roh roh makanch khobz yabes !")
         



        

        



            




        



async def setup(laymouna):
    await laymouna.add_cog(economy(laymouna))