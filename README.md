# Setting up a python discord bot on a Raspberry Pi (RasPi) zero 2 w

Hello, I've recently set up a very simple discord bot on my RasPi as a fun little project.
For the discord bot my RasPi will:
- automatically reboot once a day at a certain time
- start discord bot script on boot
- run a script to start the bot in detached screen mode

#### Installing Raspberry Pi OS

- Install the [RasPi imager](https://www.raspberrypi.com/software/), plug in your RasPi, ensuring that you already have a microSD card inserted.
- Choose your OS settings and click on the cog so you can set up SSH login details and WIFI and install.

#### Setting up RasPi
- login and enter the following:
```
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install screen
sudo apt-get install python3
pip install discord
pip install discord.py
```

#### Script to run bot in detached screen mode
```
#!/bin/bash
screen -d -m -S discordbot python3 /home/pi/discordbot.py
# starts bot in screen mode, gives it a name and detaches
```

#### Auto run detached screen script at boot
```
crontab -e
```
```
@reboot (sleep 60; /home/pi/sbot/sbot.sh) >> /home/pi/sbot/sbotlogfile.txt 2>&1
# reboots and starts after 60 seconds
```

#### Restart RasPi once a day
```
sudo crontab -e
```
```
59 07 * * * /sbin/shutdown -r now
# reboots at 07:59 / 7:59am 
```
### Discord bot features:
- Custom status
- Retrieve quotes from api [source link](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
- Bot sends message upon joining server
- Various commands to send embedded messages
- Send message at certain time every day
- Scan for specific words, responding in return
- Scan for specific user, responding in return