import discord
from discord.ext import commands
import random
import math
import asyncio
from bot_tools import *

class leveling_system(commands.Cog):
    def __init__(self,laymouna):
        self.laymouna = laymouna
        self.miw = True
   
    @commands.Cog.listener()
    async def on_ready(self):
        print("leveling_system.py is ready !")

    def level_up(self , author):

        try :
            current_exp = get_user_xp(author)
            current_level = get_user_level(author)
            next_level_xp = math.ceil((6*(int(current_level) ** 4 ))/2.5)

            if current_exp >= next_level_xp :
                current_level += 1
                set_user_level(author,current_level)
                return True
            else :
                return False
        
        except Exception as e:
            print(f"error : {e}")
            return False
        
    @commands.Cog.listener()
    async def on_message(self , message):
        
        if message.author.id == self.laymouna.user.id or message.author.bot :
            return
        
        author = message.author


       

        if not user_exists(author):
            
            create_user(author)

        
        
        
    
        user_xp = get_user_xp(author)
    

        
        
        random_exp = random.randint(5,15)

        

        new_user_xp = user_xp + random_exp

        

        set_user_xp(author,new_user_xp)

        

        
        
        
            
        

        if self.level_up(author) :
            
            try :
                reward = get_user_level(author) * 1000
                user_lem = get_user_lemons(author)
                user_lem += reward
                set_user_lemons(author,user_lem)
            
            
                level_up_embed = discord.Embed(title="lesssgooo level up !", color=discord.Color.yellow())
                level_up_embed.add_field(name="congratulation ! ", value=f"{message.author.mention} has just leveled up to level {get_user_level(author)} !!!" , inline=False)
                level_up_embed.add_field(name="level up reward : ", value=f"u got {reward} 🍋" , inline=False)
            except Exception as e:
                await message.channel.send(f"error : {e}")

            await message.channel.send(embed=level_up_embed)

    @commands.command(aliases=["rank","lvl"])
    async def level(self , ctx , user:discord.User=None):

        if user is None :
            user = ctx.author
        elif user is not None :
            user = user

        if not user_exists(user):
            create_user(user)

        try :

            current_level = get_user_level(user)
            current_exp = get_user_xp(user)
            next_level_xp = math.ceil((6*(int(current_level) ** 4 ))/2.5)

            level_card = discord.Embed(title=f"{user.name}'s level and experience", color=discord.Color.yellow())
            level_card.add_field(name="level : ",value=f"{current_level}")
            level_card.add_field(name="exp : ",value= f"{current_exp} / {next_level_xp}")
            level_card.set_footer(text=f"requested by {ctx.author.name}", icon_url=ctx.author.avatar)

        except Exception as e:
            await ctx.send(f"error : {e}")
            
        

        await ctx.send(embed=level_card)
    
    @level.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.MissingRequiredArgument):
            await ctx.send("u need to ask a question ! i don't read minds ..")
        if isinstance(error , commands.MissingPermissions):
            await ctx.send("u need permission.")






async def setup(laymouna):
    await laymouna.add_cog(leveling_system(laymouna))