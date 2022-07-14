from asyncio import events
from pydoc import describe
import discord
import random
from time import time
import datetime
from discord.ext import commands, tasks
from discord.embeds import Embed
from discord import colour
from os import getenv
import time 
import os 
import requests
import json

intents = discord.Intents(messages=True, guilds=True)
intents = discord.Intents.all()
bot = commands.Bot(case_insensitive=True, command_prefix='!', intents=intents)

# custom status
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status, activity=discord.Game('Ready!'))
  print('Bot is ready.')


@bot.event
async def on_guild_join(guild):
    if guild.system_channel:
        await guild.system_channel.send("Hello!")

# helpme command with good luck gif

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def helpme(ctx):
  embed = discord.Embed(
      colour=(discord.Colour.random()),
      description=f" **Hello {ctx.author.name}!** The commands are as follows: \n"
    ..."
  )
  embed.set_image(url=(random.choice(good_luck)))
  await ctx.reply(embed = embed)

# send message every x hours/minutes/seconds
@bot.event
async def on_ready():
   send_message.start()

@tasks.loop(hours = 24, minutes = 0, seconds=0) 
async def send_message():
   await bot.get_channel(9630593586518346800).send("Good morning!")

# retreive quotes from api
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def inspire(ctx):
    quote = get_quote()
    await ctx.reply(quote)

good_luck = ['https://c.tenor.com/nKE3fkQlJOMAAAAM/good-luck-fighting.gif', 'https://c.tenor.com/tTSmnRmlWjUAAAAC/good-luck-anime.gif',
'https://c.tenor.com/OKoyV34l5JQAAAAC/good-luck-sign-of-the-cross.gif', 'https://c.tenor.com/MZ6C4OO8HvcAAAAC/pikachu-good-luck.gif', 
'https://acegif.com/wp-content/gifs/good-luck-13.gif', 'https://c.tenor.com/P07pbQA_cjAAAAAC/good-luck-adventure-time.gif',
'https://c.tenor.com/kQLNIz-0FgkAAAAC/good-luck-taken.gif', 'https://c.tenor.com/cmqX6WK0oxQAAAAC/good-luck-captain-america.gif']


#  command saying good luck
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def gl(ctx, member:discord.Member):
  description = f"Good luck! {member.mention}" # tags the mentioned user but doesn't actually mention them
  embed = discord.Embed(
    colour=(discord.Colour.random()),
    description=description

  )
  embed.set_image(url=(random.choice(good_luck)))
  await ctx.reply(embed=embed)
  # await ctx.send(member.mention)



# command tagging someone and saying good morning
good_morning_gifs = ['https://media2.giphy.com/media/WaYIFw9ZiEn1fPcH8Y/giphy.gif?', 'https://i.pinimg.com/originals/0f/41/8a/0f418a807d4d1e40fb8428b04b86e72f.gif', 
'https://i.pinimg.com/originals/e5/8e/30/e58e300d3a2f068314db9c567a8b2772.gif', 'https://i.pinimg.com/originals/b9/36/b3/b936b3188601b9376c72ed358dac45d8.gif',
'https://www.gifcen.com/wp-content/uploads/2022/02/funny-good-morning-gif-3.gif', 'https://c.tenor.com/kAaTGOhxGLYAAAAC/inosuke-demon.gif',
'https://c.tenor.com/kDAyvJIaw7EAAAAd/poppyseedies.gif', 'https://c.tenor.com/CFuuZZSyQUkAAAAC/good-morning-wake-up.gif', 
'https://c.tenor.com/OH5Vd-yZHrUAAAAC/good-morning-skeleton-meme.gif', 'https://c.tenor.com/TZuZJYTomgwAAAAC/good-morning-morning.gif',
'https://c.tenor.com/_rp_yHj7Nn4AAAAd/good-morning.gif', 'https://c.tenor.com/yK-webGfL84AAAAC/good-morning-wishes.gif']

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def gm(ctx, member:discord.Member):
  description = f"{ctx.author.mention} says Good morning! {member.mention}" # tags the mentioned user but doesn't actually mention them
  embed = discord.Embed(
    colour=(discord.Colour.random()),
    description=description

  )
  embed.set_image(url=(random.choice(good_morning_gifs)))
  await ctx.reply(embed=embed)


@bot.command(pass_context = True , aliases=['tt', 'tradingtip', 'trading'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def tradingtips(ctx):
  tips = ['Spin around in a circle and say 5 Hail Mary’s',
  'stop exercising options and trying exorcizing your house instead',
  'Double down buy more',
  "It's different this time, buy more!",
  "Go Hard or Go Home!",
  "It takes years and years and years to learn how to trade and read charts. You're better off buying this software and allowing the artificial intelligence software to do all the work for you. All that you have to do is subscribe, pay your monthly fee, set your settings and walk away. You can't beat it!",
  "It's only a loss if you sell",
  "Pay to join my discord Server, chat room alerts will bring your small account to the moon!",
  "Bitcoin is going to Zero , SHORT BTC.",
  "Don't do demo; you want to be a real trader, start live",
  "it will go to the moon. Trust me.",
  "it will be an epic crash. Trust me.",
  "technical analysis is just astrology for traders",
  "Real men don't use stops",
  "trade against the trend",
  "Buy the dip!",
  "No, seriously. You should go ALL IN on Doge. Elon Musk is gonna be on SNL tomorrow night. It's gonna skyrocket.",
  "It can't go lower",
  "This one is free money",
  "use a mental stop loss",
  "be patient when you are in red it will turn green",
  "It's just a correction",
  "Just wait for it…it will come back up!",
  "The people that do best in the market buy and forget about it. Years later they are millionaires.",
  "you should try trading, I think you'd be good at it",
  "HODL!"
  "Follow your gut",
  "Buy shib"
  ]

  await ctx.reply(f"**My financial advice:** {random.choice(tips)}")



sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable']

harry = ['harry', 'harry!']

brilliant = ['brilliant', 'Brilliant', 'brilliant!', 'Brilliant!']

starter_encouragements = [
  'Cheer up!',
  'Hang in there.',
  'You are a great person!',
  'Believe in yourself man!'
]

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  # if not assert_cooldown():
  #     return
  # await bot.process_commands(message)     
  msg = message.content.lower()
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))
  await bot.process_commands(message)  

  if any(word in msg for word in brilliant):
    await message.channel.send("Brilliant!")
  await bot.process_commands(message)

  if any(word in msg for word in harry):
    await message.channel.send("Haaaarryyyyyyyy!!!")
  await bot.process_commands(message)  
  
  if message.author.id == 390000183657758725:
    await message.channel.send('Harryyyyyyyy!')
  await bot.process_commands(message)  




bot.run('TOKEN')