#NOTE: WHEN MERGING, MAKE SURE SHUTDOWN AND BUILD DO NOT HAVE A .DEV PREFIX. THESE ARE HERE JUST TO CHECK IF THE BUILD HERE IS CORRECT.
#NOTE: ALWAYS USE THE BUILDKIT, IT AUTOMATICALLY SIGNS YOUR BUILDS FOR YOU. **ALWAYS** RUN '4' TO REMOVE TOKENS BEFORE COMMITING.
import discord, asyncio, time, datetime, os, logging, sys, json, random

#Command Extensions - Loads modules
from cogs.mal import mal
client = discord.Client()
from cogs.osu import osu
from cogs.yt import yt
from cogs.streams import twitch
#Finished imports, defines the discord client.
client = discord.Client()
with open('config.json') as json_data_file:
    config = json.load(json_data_file) #Load config into RAM (config.json)
confShipped = 10
#Command Extensions
client = discord.Client()
with open('config.json') as json_data_file: #Load up the config file (config.json)
    config = json.load(json_data_file)
#    if config['info']['configVer'] != confShipped:
#        answer = input("The config is incorrect. (Download it from Github.com/xSilverdroid/Sonico.) Continue starting? [y/N]").lower()
#        if answer == "" or answer == "n":
#            print("Exiting.")
##            sys.exit()
#        else:
#            print("Some features may not work. Continuing start of Sonico!")
print("Sonico v" + str(config['info']['version']))
from cogs.mal import mal
from cogs.osu import osu
from cogs.taiko import taiko
from cogs.ctb import ctb
from cogs.mania import mania
from cogs.yt import yt
from cogs.dict import define

#Set version, build and admins
info = config['info']['build']
adminID = config['admins']['admins']
#Logging
now = datetime.datetime.now()
if os.path.isdir("logs") == False: #Setting up logging:
    os.makedirs("logs/")
logfile = "logs/" + datetime.datetime.now().strftime('discordlog_%Y-%m-%d_%H-%M.log')
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename=logfile, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
print("Sonico Discord bot. Session log file: ", logfile)


print("\nSonico: A Bot by Silverdroid, Nevexo and Runnerbeany. - Version: "+ str(config['info']['version']))
print("Build information: " + str(config['info']['build']) + " Built by: " + str(config['info']['builtby']) + "\n")

print("\nSonico: A Bot by Silverdroid, Nevexo and runnerbeany - "+ str(config['info']['version']))
print("Build information: " + str(config['info']['build']) + " Built by: " + str(config['info']['builtby']) + " At: " + str(config['info']['builtat']) + "\n")

print("Eating Macarons while starting up\n")
print("------------------------------------------")

#EXPERIMENTAL: Shutdown bot through command window
def shutdown():
    shutdown = input('Shutdown?')
    if shutdown == True:
        print("Sonico is shutting down.")
        client.logout
    else:
        shutdown

@client.event
async def on_ready():

    print("\nLogged in to Discord as "+client.user.name+"#"+client.user.discriminator)
    print("User ID: "+str(client.user.id))
    await client.change_presence(game=discord.Game(name="Build "+str(config['info']['build'])+" v"+str(config['info']['version'])))
    print("\nSonico is ready, nya~")

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.content == ".help":
        Embed = discord.Embed(color=0xE865A0)
        Embed.set_author(name="Sonico Help", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version'])+' build '+str(config['info']['build']))
        Embed.add_field(name="Hey! I'm Sonico ♡", value="I am a Bot developed by Silverdroid. Let me show you what I can do!")
        Embed.add_field(name="🎀 Generic Commands", value=".help generic")
        Embed.add_field(name="📕 Utility Commands", value=".help utility")
        Embed.add_field(name="🙂 Fun Commands", value=".help fun")
        Embed.add_field(name="🔎 Search Commands", value=".help search")
        Embed.add_field(name="🎵 osu!commands", value=".help osu")
        Embed.add_field(name="🔒 Admin Commands", value=".help admin")
        await client.send_message(message.channel, embed=Embed)
        
    if message.content.startswith(".help generic"):
        Embed = discord.Embed(color=0xE865A0)
        Embed.set_author(name="Generic Commands", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version'])+' build '+str(config['info']['build']))
        Embed.add_field(name="❓ .help", value="I will show you a list of all commands.")
        Embed.add_field(name="🎉 .invite", value="Invite me to another Server. (*・ω・)ﾉ")
        Embed.add_field(name="🎧 .about", value="Let me tell you a bit about me, nya~")
        Embed.add_field(name="🌍 .website", value="I will give you a link to my website, where you can read more about me :3")
        Embed.add_field(name="🐛 .bug", value='Found an issue? This command will link you to our issues page on GitHub.')
        await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".help utility"):
        Embed = discord.Embed(color=0xE865A0)
        Embed.set_author(name="Utility Commands", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version'])+' build '+str(config['info']['build']))
        Embed.add_field(name="🙂 .avatar [user]", value="I will show you the avatar of the specified user (´｡• ᵕ •｡`)")
        Embed.add_field(name="ℹ️ .user [user]", value="I will show you additional info about the user you tagged ヽ(*・ω・)ﾉ")
        await client.send_message(message.channel, embed=Embed) 
        
    if message.content.startswith(".help fun"):
        Embed = discord.Embed(color=0xE865A0)
        Embed.set_author(name="Fun Commands", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version'])+' build '+str(config['info']['build']))
        Embed.add_field(name="🤗 .cuddle [user]", value="Cuddle your friends, nya~ ♡")
        Embed.add_field(name="💤 .nap [user]", value="Take a nap with your friends!")
        await client.send_message(message.channel, embed=Embed)
        
    if message.content.startswith(".help search"):
        Embed = discord.Embed(color=0xE865A0)
        Embed.set_author(name="Search Commands", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version'])+' build '+str(config['info']['build']))
        Embed.add_field(name="🌺 .anime [search term]", value="Search for your favorite **anime**, nya~")
        await client.send_message(message.channel, embed=Embed)
    
    if message.content.startswith(".help osu"):
        Embed = discord.Embed(color=0xE865A0)
        Embed.set_author(name="osu!commands", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version'])+' build '+str(config['info']['build']))
        Embed.add_field(name="🎵 .osu [user]", value="Shows the **osu!stats** of a player.")
        Embed.add_field(name="🎶 .taiko [user]", value="Shows the **Taiko stats** of a player.")
        Embed.add_field(name="🍎 .ctb [user]", value="Shows the **Catch The Beat stats** of a player.")
        Embed.add_field(name="🎹 .mania [user]", value="Shows the **osu!mania stats** of a player.")
        await client.send_message(message.channel, embed=Embed)
        
    if message.content.startswith(".help admin"):
        Embed = discord.Embed(color=0xE865A0)
        Embed.set_author(name="Admin Commands", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version'])+' build '+str(config['info']['build']))
        Embed.add_field(name="🖼️ .profileimage", value="Changes my profile image to another one on the servers (´｡• ω •｡`) ♡")
        Embed.add_field(name="💬 .status", value="Changes the Status Message of the Bot.")
        Embed.add_field(name="✨.shutdown", value="The Sonico Bot will shut down.")
        await client.send_message(message.channel, embed=Embed)
    
    
    #Generic Commands
    if message.content.startswith(".invite"):
        Embed = discord.Embed(color=0xE865A0)
        Embed.set_author(name="Click here to invite me to another Server, nya~", url="http://sonico.silverdroid.ga/invite.php", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version']))
        Embed.add_field(name="🎉 Invite me to your server (´｡• ᵕ •｡`)", value="http://sonico.silverdroid.ga/invite.php")
        Embed.add_field(name="💾 View my code on Github!", value="http://sonico.silverdroid.ga/github.php")
        await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".about"):
        Embed = discord.Embed(color=0xE865A0)
        Embed.set_author(name="About Sonico", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version']))
        Embed.add_field(name="🌺 Hello, I'm Sonico, nya~", value="My name is Super Sonico, I am an 18 year old college student from Japan. Well, actually I am a Bot developed by Silverdroid, Nevexo and runnerbeany (*・ω・)ﾉ")
        Embed.add_field(name="🤖", value="Bot Version: v"+str(config['info']['version']))
        Embed.add_field(name="📌", value="Build Number: "+str(config['info']['build']))
        await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".website"):
        Embed = discord.Embed(color=0xE865A0)

        Embed.set_author(name="Check out my website, nya~", url="http://sonico.silverdroid.ga", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version']))
        Embed.add_field(name="🌍 Sonico on the Web:", value="http://sonico.silverdroid.ga")
        await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".build"):
        Embed = discord.Embed(color=0xE865A0)
        Embed.title = 'Build Information'
        Embed.add_field(name='Build Number:', value=str(config['info']['build']))
        Embed.add_field(name='Built By:', value=str(config['info']['builtby']))
        Embed.add_field(name='Built at:', value=str(config['info']['builtat']))
        Embed.add_field(name='Version Number:', value=str(config['info']['version']))
        await client.send_message(message.channel, embed=Embed)

        
    #Fun Commands
    if message.content.startswith(".cuddle"):
        if message.mentions:
            cuddled = message.mentions[0]
        else:
            cuddled = message.author
        Embed = discord.Embed(color=0xE865A0)
        Embed.add_field(name="Cuddle time! Nya~", value=message.author.name+" cuddles with "+cuddled.name)
        Embed.set_image(url="http://sonico.silverdroid.ga/img/cmd/cuddle.gif")
        await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".nap"):
        if message.mentions:
            napping = message.mentions[0]
        else:
            napping = message.author
        Embed = discord.Embed(color=0xE865A0)
        Embed.add_field(name="Time to take a nap, nya~", value=message.author.name+" takes a nap with "+napping.name)
        Embed.set_image(url="http://sonico.silverdroid.ga/img/cmd/nap.gif")
        await client.send_message(message.channel, embed=Embed)


    #Misc. Commands
    if message.content.startswith(".avatar"):
        if message.mentions:
            mention = message.mentions[0]
        else:
            mention = message.author
        Embed = discord.Embed()
        Embed.color = discord.Color.blue()
        Embed.set_author(name=mention.name+"#"+mention.discriminator, icon_url=mention.avatar_url)
        Embed.set_image(url=mention.avatar_url)
        await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".user"):
        if message.mentions:
            mention = message.mentions[0]
        else:
            mention = message.author
        Embed = discord.Embed()
        Embed.color = discord.Color.blue()
        Embed.set_image(url=mention.avatar_url)
        Embed.set_author(name=mention.name+"#"+mention.discriminator, icon_url=mention.avatar_url)
        Embed.add_field(name="Username", value=mention.name+"#"+mention.discriminator)
        Embed.add_field(name="ID", value=mention.id)
        Embed.add_field(name="Status", value=mention.status)
        Embed.add_field(name="Playing", value=mention.game)
        if mention.bot == True:
            Embed.add_field(name="Bot?", value="✅")
        else:
            Embed.add_field(name="Bot?", value="❌")
        await client.send_message(message.channel, embed=Embed)

#Searching Commands

    if message.content.startswith(".anime"):
        query = message.content[6:]
        Embed = discord.Embed(color=0xE865A0)
        Embed.title = "🌺 Anime | {0}".format(query)
        dat = mal.animu(query)
        if dat == "serverError":
            Embed.description = "Sorry! Something isn't right at the moment, I'll let the developers know."
            Embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
        elif dat == "credError":
            Embed.description = "Sorry! Something isn't right at the moment, I'll let the developers know."
            Embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
        elif dat == "noResults":
            Embed.description = "I couldn't find anything, nya~ (´｡• ᵕ •｡`)"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/uwu.jpg")
        else:
            Embed = discord.Embed(color=0xE865A0)
            Embed.title = "🌺 Anime | {0}".format(dat[0])
            Embed.description = str(dat[1])
            Embed.set_footer(text="https://myanimelist.net", icon_url='https://myanimelist.cdn-dena.com/images/faviconv5.ico')
        await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".osu"):
        query = message.content[5:]
        Embed = discord.Embed()
        Embed.title = "osu! | {0}".format(query)
        dat = osu.osuapi(query)
        if dat == 'serverError':
            Embed.description = "Hmm... That didn't work. Try again later, nya~"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        elif dat == 'credError':
            Embed.description = "Hmm... Something broke. Try again later, nya~)"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        elif dat == 'noResults':
            Embed.description = "I couldn't find anything, nya~ (´｡• ᵕ •｡`)"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/uwu.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        else:
            data = osu.osuapi(message.content[5:])
            userid = data[1]
            accuracy = data[4]
            country = data[5]
            rank = data[6]
            level = data[7]
            Embed = discord.Embed(color=0xE865A0)
            Embed.title = 'osu! | {0}'.format(query)
            Embed.description = 'http://osu.ppy.sh/u/'+userid.format(query)
            Embed.set_footer(text='osu! | '+message.content[5:], icon_url='https://new.ppy.sh/images/layout/osu-logo.png')
            Embed.add_field(name='🆔 User ID:', value=data[1])
            Embed.add_field(name='🎮 Play Count:', value=data[3])
            if accuracy == None:
                Embed.add_field(name='🏅 Accuracy:', value='Never played.')
            else:
                Embed.add_field(name='🏅 Accuracy:', value=str(int(float(accuracy)))+'%')
            Embed.add_field(name='🌍 Country:', value=':flag_'+country.lower()+': '+country)
            if rank == '0':
                Embed.add_field(name='🔶 Rank:', value='None')
            else:
                Embed.add_field(name='🔶 Rank:', value=rank)
            if level == None:
                Embed.add_field(name='🚀 Level:', value='Never played.')
            else:
                Embed.add_field(name='🚀 Level:', value=str(int(float(level))))
            Embed.set_thumbnail(url=data[8])
            await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".taiko"):
        query = message.content[7:]
        Embed = discord.Embed()
        Embed.title = "osu!taiko | {0}".format(query)
        dat = taiko.taikoapi(query)
        if dat == 'serverError':
            Embed.description = "Hmm... That didn't work. Try again later, nya~"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        elif dat == 'credError':
            Embed.description = "Hmm... Something broke. Try again later, nya~)"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        elif dat == 'noResults':
            Embed.description = "I couldn't find anything, nya~ (´｡• ᵕ •｡`)"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/uwu.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        else:
            data = taiko.taikoapi(message.content[7:])
            userid = data[1]
            accuracy = data[4]
            country = data[5]
            rank = data[6]
            level = data[7]
            Embed = discord.Embed(color=0xE865A0)
            Embed.title = 'osu!taiko | {0}'.format(query)
            Embed.description = 'http://osu.ppy.sh/u/'+userid.format(query)
            Embed.set_footer(text='osu!taiko | '+message.content[7:], icon_url='https://new.ppy.sh/images/layout/osu-logo.png')
            Embed.add_field(name='🆔 User ID:', value=data[1])
            Embed.add_field(name='🎮 Play Count:', value=data[3])
            if accuracy == None:
                Embed.add_field(name='🏅 Accuracy:', value='Never played.')
            else:
                Embed.add_field(name='🏅 Accuracy:', value=str(int(float(accuracy)))+'%')
            Embed.add_field(name='🌍 Country:', value=':flag_'+country.lower()+': '+country)
            if rank == '0':
                Embed.add_field(name='🔶 Rank:', value='None')
            else:
                Embed.add_field(name='🔶 Rank:', value=rank)
            if level == None:
                Embed.add_field(name='🚀 Level:', value='Never played.')
            else:
                Embed.add_field(name='🚀 Level:', value=str(int(float(level))))
            Embed.set_thumbnail(url=data[8])
            await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".ctb"):
        query = message.content[5:]
        Embed = discord.Embed()
        Embed.title = "Catch the Beat | {0}".format(query)
        dat = ctb.ctbapi(query)
        if dat == 'serverError':
            Embed.description = "Hmm... That didn't work. Try again later, nya~"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        elif dat == 'credError':
            Embed.description = "Hmm... Something broke. Try again later, nya~)"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        elif dat == 'noResults':
            Embed.description = "I couldn't find anything, nya~ (´｡• ᵕ •｡`)"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/uwu.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        else:
            data = ctb.ctbapi(message.content[5:])
            userid = data[1]
            accuracy = data[4]
            country = data[5]
            rank = data[6]
            level = data[7]
            Embed = discord.Embed(color=0xE865A0)
            Embed.title = 'Catch The Beat | {0}'.format(query)
            Embed.description = 'http://osu.ppy.sh/u/'+userid.format(query)
            Embed.set_footer(text='Catch the Beat | '+message.content[5:], icon_url='https://new.ppy.sh/images/layout/osu-logo.png')
            Embed.add_field(name='🆔 User ID:', value=data[1])
            Embed.add_field(name='🎮 Play Count:', value=data[3])
            if accuracy == None:
                Embed.add_field(name='🏅 Accuracy:', value='Never played.')
            else:
                Embed.add_field(name='🏅 Accuracy:', value=str(int(float(accuracy)))+'%')
            Embed.add_field(name='🌍 Country:', value=':flag_'+country.lower()+': '+country)
            if rank == '0':
                Embed.add_field(name='🔶 Rank:', value='None')
            else:
                Embed.add_field(name='🔶 Rank:', value=rank)
            if level == None:
                Embed.add_field(name='🚀 Level:', value='Never played.')
            else:
                Embed.add_field(name='🚀 Level:', value=str(int(float(level))))
            Embed.set_thumbnail(url=data[8])
            await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".mania"):
        query = message.content[7:]
        Embed = discord.Embed()
        Embed.title = "osu!mania | {0}".format(query)
        dat = mania.maniaapi(query)
        if dat == 'serverError':
            Embed.description = "Hmm... That didn't work. Try again later, nya~"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        elif dat == 'credError':
            Embed.description = "Hmm... Something broke. Try again later, nya~)"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        elif dat == 'noResults':
            Embed.description = "I couldn't find anything, nya~ (´｡• ᵕ •｡`)"
            Embed.set_image(url="http://sonico.silverdroid.ga/img/uwu.jpg")
            await client.send_message(message.channel, embed=Embed)
            return
        else:
            data = mania.maniaapi(message.content[7:])
            userid = data[1]
            accuracy = data[4]
            country = data[5]
            rank = data[6]
            level = data[7]
            Embed = discord.Embed(color=0xE865A0)
            Embed.title = 'osu!mania | {0}'.format(query)
            Embed.description = 'http://osu.ppy.sh/u/'+userid.format(query)
            Embed.set_footer(text='osu!mania | '+message.content[7:], icon_url='https://new.ppy.sh/images/layout/osu-logo.png')
            Embed.add_field(name='🆔 User ID:', value=data[1])
            Embed.add_field(name='🎮 Play Count:', value=data[3])
            if accuracy == None:
                Embed.add_field(name='🏅 Accuracy:', value='Never played.')
            else:
                Embed.add_field(name='🏅 Accuracy:', value=str(int(float(accuracy)))+'%')
            Embed.add_field(name='🌍 Country:', value=':flag_'+country.lower()+': '+country)
            if rank == '0':
                Embed.add_field(name='🔶 Rank:', value='None')
            else:
                Embed.add_field(name='🔶 Rank:', value=rank)
            if level == None:
                Embed.add_field(name='🚀 Level:', value='Never played.')
            else:
                Embed.add_field(name='🚀 Level:', value=str(int(float(level))))
            Embed.set_thumbnail(url=data[8])
            await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".twitch"):
        query = message.content[8:]
        Embed = discord.Embed()
        Embed.title = "Twitch | {0}".format(query)
        data = twitch.twitchAPI(query)
        print(data)
        user = data[0]
        followers = data[1]
        playing = data[2]
        title = data[4]
        thumb = data[3]
        viewers = twitch.viewers(query)
        viewers = viewerData[0]
        Embed.title = 'Twitch | {0}'.format(query)
        #Embed.description = 'http://twitch.tv/{0}'.format(query)
        Embed.add_field(name='Title:', value=title)
        Embed.set_footer(text=data[5], icon_url='https://img.clipartfest.com/2cb1c9e088b87fc50c322884f46f8b7e_trisha-hershberg-image-twitch-logo-clipart_1920-1080.png')
        Embed.add_field(name='Name:', value=user)
        Embed.add_field(name='Playing:', value=playing)
        Embed.add_field(name='Followers:', value=followers)
        if viewers == None:
            Embed.add_field(name='Viewers:', value="None")
        else:
            Embed.add_field(name='Viewers:', value=Viewers)
        Embed.add_field(name='Viewers:', value=viewers)
        if thumb == None:
            Embed.set_thumbnail(url='http://sonico.silverdroid.ga/img/twitch_noicon.img')
        else:
            Embed.set_thumbnail(url=thumb)
            #Embed.set_thumbnail(url=thumb)
        await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".urban"):
        defi = define.urban(str(message.content[7:]))
        if defi == False:
            Embed = discord.Embed(color=0xE865A0)
            Embed.title = 'Urban Dictionary | {0}'.format(str(message.content[7:]))
            Embed.description = "I didn't find anything, nya~"
            Embed.color = discord.Color.red()
        else:
            Embed = discord.Embed(color=0xE865A0)
            Embed.title = 'Urban Dictionary | {0}'.format(str(message.content[7:]))
            Embed.description = (defi)
        await client.send_message(message.channel, embed=Embed)

    #Utility Commands
    if message.content.startswith(".bug"):
        Embed = discord.Embed(color=0xE865A0)
        Embed.title = '🐛 Eek! Is there a bug?'
        Embed.description = 'Report them on my GitHub page, nya~ https://github.com/xSilverdroid/Sonico/issues'
        Embed.set_footer(text='Sonico v'+str(config['info']['version'])+' | Build '+str(config['info']['build']))
        await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".sonico"):
        Embed = discord.Embed(color=0xE865A0)
        Embed.set_author(name="Sonico", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.add_field(name="Whoops. This command is still in development.", value="Check back again when we are finished, nya~")
        await client.send_message(message.channel, embed=Embed)


    #Admin Commands
    if message.content.startswith(".profileimage"):
        if message.author.id == adminID:
            print("\nUpdating profile image...")
            message_id = await client.send_message(message.channel, ":clock2: Updating profile image, nya~")
            if "default" in message.content.lower():
                file = "images/default.png"
            elif "macaron" in message.content.lower():
                file = "images/macaron.jpg"
            elif "music" in message.content.lower():
                file = "images/music.jpg"
            elif "cats" in message.content.lower():
                file = "images/cats.jpg"
            elif "guitar" in message.content.lower():
                file = "images/guitar.jpg"
            elif "opener" in message.content.lower():
                file = "images/opener.jpg"
            elif "owo" in message.content.lower():
                file = "images/owo.jpg"
            elif "uwu" in message.content.lower():
                file = "images/uwu.jpg"
            else:
                print("Error: That file does not exist, nya~")
                Embed = discord.Embed()
                Embed.color = discord.Color.red()
                Embed.add_field(name="Error.", value="Nani? That image doesn't exist, nya~ (´｡• ᵕ •｡`)")
                Embed.set_image(url="http://sonico.silverdroid.ga/img/uwu.jpg")
                await client.send_message(message.channel, embed=Embed)
                return
            logo = open(file,"rb")
            await client.edit_profile(avatar=logo.read())
            await client.delete_message(message_id)
            print("\nSuccessfully updated image, nya~")
            Embed = discord.Embed()
            Embed.color = discord.Color.green()
            Embed.add_field(name="✅ Image updated.", value="Do I look pretty? Nya~")
            await client.send_message(message.channel, embed=Embed)
        else:
            Embed = discord.Embed()
            Embed.color = discord.Color.red()
            Embed.add_field(name="Error.", value="You don't have Permission for that, nya~ (´｡• ᵕ •｡`)")
            await client.send_message(message.channel, embed=Embed)
    if message.content.startswith(".status"):
        if message.author.id == adminID:
            await client.change_presence(game=discord.Game(name=message.content[8:]))
            Embed = discord.Embed()
            Embed.color = discord.Color.green()
            Embed.add_field(name="✅ Success.", value="Status updated, nya~")
            await client.send_message(message.channel, embed=Embed)
        else:
            Embed = discord.Embed()
            Embed.color = discord.Color.red()
            Embed.add_field(name="Error.", value="You don't have Permission for that, nya~ (´｡• ᵕ •｡`)")
            await client.send_message(message.channel, embed=Embed)
    if message.content.startswith(".shutdown"):
        if message.author.id == adminID:
            Embed = discord.Embed(color=0xE865A0)
            Embed.set_image(url="http://sonico.silverdroid.ga/img/cmd/shutdown.png")
            Embed.add_field(name="✨ Shutting down.", value="Good Night, nya~")
            print("Shutting down.")
            await client.change_presence(game=None, status='dnd')
            await client.send_message(message.channel, embed=Embed)
            time.sleep(3)
            await client.logout()
        else:
            Embed = discord.Embed()
            Embed.color = discord.Color.red()
            Embed.add_field(name="Error.", value="You don't have Permission for that, nya~ (´｡• ᵕ •｡`)")
            await client.send_message(message.channel, embed=Embed)


@client.event
async def on_error(event, *args, **kwargs):
    await client.send_message(discord.Object(id='301742246083166211'), "```Error Raised: " + str(sys.exc_info()) + "```" + "Event raised on: " + event)
    print("An Error occured, nya~: " + str(sys.exc_info()) + "```" + "Event raised on: " + event)

try:
    client.run(config['tokens']['token'])
except Exception as e:
    print("Something has gone wrong, nya~ Error: " + str(e) + " Check your log files.")
