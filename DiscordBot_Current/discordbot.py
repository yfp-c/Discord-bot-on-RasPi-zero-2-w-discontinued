import discord
import random
from time import time
# import aiocron
from discord.ext import commands, tasks
from discord.embeds import Embed
from discord import colour
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from datetime import datetime

intents = discord.Intents(messages=True, guilds=True)
intents = discord.Intents.all()
bot = commands.Bot(case_insensitive=True, command_prefix='!', intents=intents, help_command=None)

initial_extensions = []
async def load_extensions():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      initial_extensions.append("cogs." + filename[:-3])

  if __name__ == '__main__':
    for extension in initial_extensions:
      await bot.load_extension(extension)

  print(initial_extensions)

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send("Loaded cog!")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send("Unloaded cog!")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send("Reloaded cog!")   

@bot.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.CommandOnCooldown):

        time = round(exception.retry_after)

        hours = str(time // 3600)

        minutes_calc = int(time % 3600)
        minutes = str((time % 3600) // 60)

        # seconds = time

        if hours != "0":
          msg = f"Damn you'll be waiting a while... {ctx.author.mention} {hours} hours and {minutes} minutes before you can do that command again."
        elif hours == "0" and minutes_calc > 60:
          msg = f"Not long to go.. {ctx.author.mention} {minutes} minutes before you can do that command again."
        else:
          msg = ('Slow down!!! {:.2f} seconds until you can try that command again.'.format(exception.retry_after))
        await ctx.send(msg)
        await ctx.message.delete()
        


CHANNEL_TEST=963059358118346806
CHANNEL_JaLaLo=666030222717485076
CHANNEL_SPARTA=958316995156267068

async def test_channel_gm():
    role = "<@&992408786969038879>"
    good_morning = bot.get_channel(CHANNEL_TEST)
    timestamp = datetime.now()
    UK = pytz.timezone('Europe/London')
    reaction_thumbs_up = '👍'
    gm = await good_morning.send(f"Gooood morning {role}! Today is the {timestamp.astimezone(UK).strftime('%dth of %B, %Y')}. Don't forget your **timesheets!**")
    await gm.add_reaction(reaction_thumbs_up)

async def JaLaLo_gm():
    good_morning = bot.get_channel(CHANNEL_JaLaLo)
    reaction_thumbs_up = '👍'
    timestamp = datetime.now()
    MY = pytz.timezone('Asia/Kuala_Lumpur')
    msg = (f"\nThe time is {timestamp.astimezone(MY).strftime('%X')} and the date is {timestamp.astimezone(MY).strftime('%x')}.")
    message = await good_morning.send("Goooood moooooooorning!!!! How are we doing guys?" + msg)
    await message.add_reaction(reaction_thumbs_up)

async def sparta_channel_timesheets():
    role = "<@&992397131904192553>"
    channel = bot.get_channel(CHANNEL_SPARTA)
    timestamp = datetime.now()
    UK = pytz.timezone('Europe/London')
    reaction_thumbs_up = '👍'
    time_sheets = await channel.send(f"Gooood morning {role}! Today is Friday the {timestamp.astimezone(UK).strftime('%dth of %B, %Y')}. Don't forget your **timesheets!**")
    await time_sheets.add_reaction(reaction_thumbs_up)

async def sparta_channel_gm():
    channel = bot.get_channel(CHANNEL_SPARTA)
    reaction_thumbs_up = '👍'
    good_morning = await channel.send("Goooood moooooooorning!!!!  How are we doing guys?")
    await good_morning.add_reaction(reaction_thumbs_up)    

@bot.event
async def on_guild_join(guild):
    if guild.system_channel:
        await guild.system_channel.send("Goooood moooooooorning!!!! How are we doing guys? !helpme for more commands! Good luck! Brilliant!")

@bot.event
async def on_ready():
    scheduler = AsyncIOScheduler()   
    scheduler.add_job(test_channel_gm, CronTrigger(day_of_week="sat-sun", hour="12", minute="0"))     
    # scheduler.add_job(JaLaLo_gm, CronTrigger(day_of_week="mon-fri", hour="23", minute="30")) # malay time
    # scheduler.add_job(sparta_channel_gm, CronTrigger(day_of_week="mon-fri", hour="8", minute="0"))
    # scheduler.add_job(sparta_channel_timesheets, CronTrigger(day_of_week="fri", hour="09", minute="30"))
    scheduler.start()
    await load_extensions()

    print('Bot is ready to go above and beyond!')


bot.run()