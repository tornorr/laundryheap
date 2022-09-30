import discord
import random

from discord.ext import commands

class Remote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def remote(self, ctx, channel, *, remotemsg):
        channeldict = {"general":626180297993748499, "memes":626182840517918760, "dragonvale":626181797696503818, "mods":276384829593878529, "test":904179778758774824, "herald":946617550442213386, "oracle":818011940160405534}
        channel = self.bot.get_channel(channeldict[channel])
        if ctx.guild.id == 720120185289310229:
            await channel.send(remotemsg)
 
async def setup(bot):
    await bot.add_cog(Remote(bot))
