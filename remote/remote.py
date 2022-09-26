import discord
import random

from discord.ext import commands

class Remote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

    @commands.command()
    async def pet(self, ctx):
        petMod = random.Randint(1,100)
        if petMod <= 79:
            await ctx.send('YOOOOO! <:dv_pogberry:894740347698184232')
        elif petMod <= 94:
            await ctx.send('....wha? huh? <:dv_:dv_drowsysnooz:894740491453743115>')
        elif petMod <= 99:
            await ctx.send('uh- uhh- az]jmr7c_w9irp <:dv_blizzardderp:894740491453743115>')
        else:
            await ctx.send("It's aurorin' time <:dv_trollrora:894740491453743115>")
        

    @commands.command()
    async def remote(self, ctx, channel, *, remotemsg):
        channeldict = {"general":626180297993748499, "memes":626182840517918760, "dragonvale":626181797696503818, "mods":276384829593878529, "test":904179778758774824}
        channel = ctx.get_channel(channeldict[channel])
        if ctx.guild == 720120185289310229:
            await ctx.send(f'{remotemsg}')
 
def setup(bot):
    bot.add_cog(Remote(bot))