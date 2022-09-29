import discord, random
from discord.ext import commands

class sadboy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def sb(self, ctx):
        with open("./cogs/sad_boy_lyrics/sadboy.txt", "r", encoding=None, errors=None) as file:
            allText = file.readlines()
            words = list(map(str, allText))
            embed = discord.Embed(title=f"😥😔☹", description=f"🎵 {random.choice(words)}", color=discord.Colour.random())
            await ctx.reply(embed = embed)
            # await ctx.reply(random.choice(words))       



async def setup(bot):
    await bot.add_cog(sadboy(bot))