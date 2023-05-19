# phorbal-image-bot

Small discord bot (using client) that either sends 1 image from the phorbalurl.txt when you mention "phorbal" in a server where the bot is added, or
if you mention p-stats it will give you the amount of files in the phorbalurl.txt. It's sending funny cat images which are grabbed from a tiktok user called 'phorbal'. That's why I called the bot phorbal. It is really easy to set up and use and it makes me smile everytime I use it :)

## Hosting on replit

If you want to host the bot on replit, then you can either import this repo from github (it's a feature in replit) or you can clone this repo and upload the 3 needed files (phorbal.py, phorbalurl.txt and replit_keep_alive.py). After that, rename phorbal.py to main.py, add your token and uncomment the line with the keep_alive function. Then you can run the bot, this will create a webserver which will keep the bot running. You can then add the link to the webserver to a ping service like [uptimerobot](https://uptimerobot.com/). Give that monitor a name, set it to monitor HTTP(S) and paste the link to the webserver in the URL field. Then you can create the monitor and the bot will be online 24/7.
