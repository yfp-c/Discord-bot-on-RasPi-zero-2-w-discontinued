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

CHANNEL_TEST=963059358118346806
CHANNEL_JaLaLo=666030222717485076
CHANNEL_SPARTA=958316995156267068

# async def test_channel_gm():
#     role = "<@&992408786969038879>"
#     good_morning = bot.get_channel(CHANNEL_TEST)
#     timestamp = datetime.now()
#     UK = pytz.timezone('Europe/London')
#     reaction_thumbs_up = '👍'
#     gm = await good_morning.send(f"Gooood morning {role}! Today is the {timestamp.astimezone(UK).strftime('%dth of %B, %Y')}. Don't forget your **timesheets!**")
#     await gm.add_reaction(reaction_thumbs_up)

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
    # scheduler.add_job(test_channel_gm, CronTrigger.from_crontab("* * * * *"))     
    # scheduler.add_job(JaLaLo_gm, CronTrigger.from_crontab("00 23 * * *")) # malay time
    # scheduler.add_job(sparta_channel_gm, CronTrigger.from_crontab("00 08 * * 1-5"))
    # scheduler.add_job(sparta_channel_timesheets, CronTrigger.from_crontab("30 09 * * 5"))
    scheduler.start()
    await load_extensions()

    print('Bot is ready to go above and beyond!')


bot.run()