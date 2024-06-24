import io
import discord
from discord.ext import commands
import aiohttp
import asyncio

class wizzard_buttons(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.value : bool = None
    
    

    @discord.ui.button(label="accept", style=discord.ButtonStyle.green , emoji="✅")
    async def accept(self, interaction: discord.Interaction , button: discord.ui.Button):
        
        await interaction.response.defer()
        self.value = True
        self.stop()

    @discord.ui.button(label="decline", style=discord.ButtonStyle.red , emoji="❌")
    async def decline(self, interaction: discord.Interaction , button: discord.ui.Button):
        
        await interaction.response.defer()
        self.value = False
        self.stop()

class emotes(commands.Cog):
    def __init__(self,laymouna):
        self.laymouna = laymouna
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("emotes.py are ready !")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def sad(self , ctx):
        act_embed = discord.Embed(title="sad" , description="this is sooo sad .. can we get 5 likes ?" , color=discord.Color.dark_blue())
        act_embed.set_image(url="https://imgur.com/a1SVFXW.png")
        await ctx.send(embed = act_embed )
    @sad.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            err_msg = await ctx.send("u can't use this command again ! wait 5 seconds !")
            await asyncio.sleep(5)
            await err_msg.delete()



    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def blush(self , ctx):
        act_embed = discord.Embed(title="blush" , description="damn .. u got me on that sweet shit !" , color=discord.Color.dark_blue())
        act_embed.set_image(url="https://imgur.com/DWHCoYe.png")
        await ctx.send(embed = act_embed )
    
    @blush.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            err_msg = await ctx.send("u can't use this command again ! wait 5 seconds !")
            await asyncio.sleep(5)
            await err_msg.delete()


    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def cry(self , ctx):
        act_embed = discord.Embed(title="cry" , description="matbkiiich gouli da mktoubiiii" , color=discord.Color.dark_blue())
        act_embed.set_image(url="https://imgur.com/a1SVFXW.png")
        await ctx.send(embed = act_embed )
    @cry.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            err_msg = await ctx.send("u can't use this command again ! wait 5 seconds !")
            await asyncio.sleep(5)
            await err_msg.delete()


    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def thumbsup(self , ctx):
        act_embed = discord.Embed(title="thumbsup" , description="hayla hayla !" , color=discord.Color.dark_blue())
        act_embed.set_image(url="https://imgur.com/pnhizZQ.png")
        await ctx.send(embed = act_embed )
    @thumbsup.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            err_msg = await ctx.send("u can't use this command again ! wait 5 seconds !")
            await asyncio.sleep(5)
            await err_msg.delete()


    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def sus(self , ctx):
        act_embed = discord.Embed(title="suuuuuuus" , description="hmmmmmmmm.." , color=discord.Color.dark_blue())
        act_embed.set_image(url="https://imgur.com/X7xr0LF.png")
        await ctx.send(embed = act_embed )
    @sus.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            err_msg = await ctx.send("u can't use this command again ! wait 5 seconds !")
            await asyncio.sleep(5)
            await err_msg.delete()

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def triggered(self , ctx):
        act_embed = discord.Embed(title="triggered" , description="yawdi roh @$&@&#$#&##" , color=discord.Color.dark_blue())
        act_embed.set_image(url="https://imgur.com/B2wEru0.png")
        await ctx.send(embed = act_embed )
    @triggered.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            err_msg = await ctx.send("u can't use this command again ! wait 5 seconds !")
            await asyncio.sleep(5)
            await err_msg.delete()

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["jesse"])
    async def police(self , ctx):
        act_embed = discord.Embed(title="STOP!" , description="no jesse around here!" , color=discord.Color.dark_blue())
        act_embed.set_image(url="https://imgur.com/WE7xxqI.png")
        await ctx.send(embed = act_embed )
    @police.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            err_msg = await ctx.send("u can't use this command again ! wait 5 seconds !")
            await asyncio.sleep(5)
            await err_msg.delete()

    #@commands.cooldown(1, 5, commands.BucketType.user)
    #@commands.command()
    async def frog(self , ctx):
        act_embed = discord.Embed(title="look at this fghog" , description="cute isn't he ?" , color=discord.Color.dark_blue())
        act_embed.set_image(url="https://imgur.com/PBpLJez.png")
        await ctx.send(embed = act_embed )
    







    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["wiz"])
    async def wizzard(self , ctx):

        
        try :
            
        
            act_embed = discord.Embed(title="the wizzard is here!" , description="de you accept his gift ?" , color=discord.Color.dark_blue())
            act_embed.set_image(url="https://imgur.com/CklqaZ9.png")

            wizard_view = wizzard_buttons()
            

            await ctx.send(embed = act_embed , view = wizard_view)
            await wizard_view.wait()

            if wizard_view.value == True:
                await ctx.send("u accepted the gift !")
                await self.frog(ctx)
                dm = await ctx.author.send("want another frog ? follow farouk on insta : f_merabtine_12")
                await asyncio.sleep(60)
                await dm.delete()
            else:
                await ctx.send("u didn't accept the gift !")
                await asyncio.sleep(2)
                await self.sus(ctx)
                await asyncio.sleep(2)
                await ctx.send("u will be cursed for eternity !")
                await asyncio.sleep(2)
                await ctx.send("FUCK YOU <3")
                dm = await ctx.author.send("t3yi 😒😒😒😒😒")
                await asyncio.sleep(20)
                await dm.delete()



        except Exception as e:
            await ctx.send(e) 
    @wizzard.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            err_msg = await ctx.send("u can't use this command again ! wait 5 seconds !")
            await asyncio.sleep(5)
            await err_msg.delete()


        

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def ta7iya(self , ctx):
        act_embed = discord.Embed(title="haw 7a9ak" , description="u a real one fr fr" , color=discord.Color.dark_blue())
        act_embed.set_image(url="https://imgur.com/1mFpeC0.png")
        await ctx.send(embed = act_embed )
    @ta7iya.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            err_msg = await ctx.send("u can't use this command again ! wait 5 seconds !")
            await asyncio.sleep(5)
            await err_msg.delete()


    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def f9tlk(self , ctx):
        act_embed = discord.Embed(title="wtf" , description="wtf is this ?" , color=discord.Color.dark_blue())
        act_embed.set_image(url="https://imgur.com/PhDBbZy.png")
        await ctx.send(embed = act_embed )
    @f9tlk.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            err_msg = await ctx.send("u can't use this command again ! wait 5 seconds !")
            await asyncio.sleep(5)
            await err_msg.delete()

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def lmblg(self , ctx):
        act_embed = discord.Embed(title="wtf" , description="wtf is this ?" , color=discord.Color.dark_blue())
        act_embed.set_image(url="https://imgur.com/HdfG6fI.png")
        await ctx.send(embed = act_embed )
    @lmblg.error
    async def on_error(self , ctx , error):
        if isinstance(error , commands.CommandOnCooldown):
            err_msg = await ctx.send("u can't use this command again ! wait 5 seconds !")
            await asyncio.sleep(5)
            await err_msg.delete()



        



async def setup(laymouna):
    await laymouna.add_cog(emotes(laymouna))