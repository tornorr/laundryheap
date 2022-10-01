import discord
from datetime import date, time

from discord.ext import commands, tasks

class announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.announce.start()

    @tasks.loop(time=time(hour=16,minute=9))
    async def announce(self):
        channel = self.bot.get_channel(720120185729843273)
        await channel.send("hey1")
        spraw = open("AutoAnnounceSheet.csv", 'r')
        for line in spraw:
            splist = line.split(",")
            announcement = ""
            await channel.send("hey2")
            if (date.today())[:5] == splist[12]:
                drag = splist[0]
                caption = splist[2]
                gemtest = splist[9]
                if announcement != "":
                    announcement += "\n\n"
                if gemtest == "NA":
                    announcement += ("**LEFT:gem::", drag + "**\n" + caption)
                else:
                    announcement += ("**LEFT:dragon::", drag + "**\n" + caption)
            if (date.today())[:5] == splist[11]:
                await channel.send("hey3")
                drag = splist[0]
                caption = splist[1]
                timer = splist[6]
                redtimer = splist[7]
                base = splist[8]
                social = splist[9]
                price = splist[10]
                leave = splist[12]
                elemformatting = [splist[3],splist[4],splist[5]]
                accum = 0
                for value in elemformatting:
                    elmcount = 0
                    elemlist = value.split("-")
                    for val in elemlist:
                        if val == val.capitalize():
                            pass
                        else:
                            if val == "p":
                                val = ":dv_Elem_plant:"
                            elif val == "f":
                                val = ":dv_Elem_fire:"
                            elif val == "e":
                                val = ":dv_Elem_earth:"
                            elif val == "c":
                                val = ":dv_Elem_cold:"
                            elif val == "l":
                                val = ":dv_Elem_lightning:"
                            elif val == "w":
                                val = ":dv_Elem_water:"
                            elif val == "a":
                                val = ":dv_Elem_air:"
                            elif val == "m":
                                val = ":dv_Elem_metal:"
                            elif val == "i":
                                val = ":dv_Elem_light:"
                            elif val == "d":
                                val = ":dv_Elem_dark:"
                            elif val == "su":
                                val = ":dv_Elep_sun:"
                            elif val == "mu":
                                val = ":dv_Elep_moon:"
                            elif val == "sea":
                                val = ":dv_Elep_seasonal:"
                            elif val == "crys":
                                val = ":dv_Elep_crystalline:"
                            elif val == "gem":
                                val = ":dv_Elep_gemstone:"
                            else:
                                pass
                            elmcount += 1
                    if accum == 0:
                        if elmcount == 1:
                            elmtext = "Element:"
                        else:
                            elmtext = "Elements:"
                        for value in elemlist:
                            elements += value
                    elif accum == 1:
                        if "Elep" not in elemlist[0]:
                            pass
                        else:
                            for value in elemlist:
                                hiddens += value
                    elif accum == 2:
                        if "Elem" in elemlist[0]:
                            for value in elemlist:
                                templist += value
                            combo = ("Any combination with the following elements:", templist)
                        else:
                            combo = (elemlist[0],"x",elemlist[1])
                    accum += 1
                if "/" not in str(base):
                    odds = (str(base) + "%")
                elif str(base)[3] == "/":
                    odds = (str(base)[0] + "%", "if you don't own one,", str(base)[2] + "%", "if you own one,",
                    str(base)[4] + "%", "if you own 2 or more")
                else:
                    odds = (str(base)[0] + "%", "if you don't own one,", str(base)[2] + "%", "if you do")
                datedict = {"01":"January", "02":"February", "03":"March", "04":"April", "05":"May", "06":"June",
                "07":"July", "08":"August","09":"September","10":"October","11":"November","12":"December"}
                if leave[:3] == "01" or "21" or "31":
                    formdate = ("**" + datedict[leave[2:]], leave[:3] + "st**")
                elif leave[:3] == "02" or "22":
                    formdate = ("**" + datedict[leave[2:]], leave[:3] + "nd**")
                elif leave[:3] == "03" or "23":
                    formdate = ("**" + datedict[leave[2:]], leave[:3] + "rd**")
                else:
                    formdate = ("**" + datedict[leave[2:]], leave[:3] + "th**")
                if announcement != "":
                    announcement += "\n\n"
                if social == "NA":
                    announcement = ("**RETURNING:gem::", drag + "!**","\n"+ caption + "\n\n**" + elmtext + "**:" ,
                    elements + "\n**Timers**:", timer, "(" + redtimer, "reduced)\n**Combo**:",combo,"\n**Base Odds**:",
                    odds, "\n\n**" + drag + "** costs :dv_gem:", price, "and will expire on", formdate)
                elif "Elep" not in elements:
                    announcement = ("**RETURNING:gem::", drag + "!**","\n"+ caption + "\n\n**" + elmtext + "**:" ,
                    elements + "\n**Timers**:", timer, "(" + redtimer, "reduced)\n**Combo**:",combo,"\n**Base Odds**:",
                    odds, "\n**Social Clone Odds**:", social + "%", "\n\n**" + drag + "** costs :dv_gem:", price, 
                    "and will expire on", formdate)
                else:
                    announcement = ("**RETURNING:gem::", drag + "!**","\n"+ caption + "\n\n**" + elmtext + "**:" ,
                    elements, "\n**Hidden Elements**:", hiddens, "\n**Timers**:", timer, "(" + redtimer, "reduced)\n**Combo**:",
                    combo,"\n**Base Odds**:", odds, "\n**Social Clone Odds**:", social + "%", "\n\n**" + drag + 
                    "** costs :dv_gem:", price, "and will expire on", formdate)
                await channel.send(announcement)
                
async def setup(bot):
    await bot.add_cog(announce(bot))
