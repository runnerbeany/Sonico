import discord, asyncio, time, datetime, os, logging, sys, json, random

#Command Extensions
from cogs.mal import mal
<<<<<<< HEAD
client = discord.Client()
token = '' #Insert Discord Bot Token
adminID = "" #Insert your ID to access the Admin commands
version = "1.0"
build = "4"
=======
from cogs.osu import osu
>>>>>>> dev

#Define the client function with discord.client.
client = discord.Client()
with open('config.json') as json_data_file: #tLoad up the config file (con    fig.json)
    config = json.load(json_data_file)
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
print("Session log file: ", logfile)

print("\nSonico: A Bot by Silverdroid. - "+ str(config['info']['version']))
print("Eating Macarons while starting up\n")
print("------------------------------------------")
print("NOTE: This is a DEVELOPER Build.\n")
print("Those builds still have issues and might not run properly.\n")
print("For a stable build of Sonico, head to the /master branch.")
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
    await client.change_presence(game=discord.Game(name="Developer Build |"+str(config['info']['version'])))
    print("\nSonico is ready, nya~")

@client.event
async def on_message(message):
    if message.content.startswith(".help"):
        Embed = discord.Embed()
        Embed.color = discord.Color.green()
        Embed.set_author(name="Sonico Help", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version']))
        Embed.add_field(name="Hey! I'm Sonico ♡", value="I am a Bot developed by Silverdroid. Let me show you what I can do!")
        Embed.add_field(name="🎉 .invite", value="Invite me to another Server. (*・ω・)ﾉ")
        Embed.add_field(name="🎧 .about", value="Let me tell you a bit about me, nya~")
        Embed.add_field(name="🌍 .website", value="I will give you a link to my website, where you can read more about me :3")
<<<<<<< HEAD
        Embed.add_field(name="🙂 .avatar", value="I will show you the avatar of the specified user (´｡• ᵕ •｡`)")
=======
        Embed.add_field(name="🤗 .cuddle", value="Cuddle your friends, nya~ ♡")
        Embed.add_field(name="💤 .nap", value="Take a nap with your friends!")
        Embed.add_field(name="🙂 .avatar", value="I will show you the avatar of the user you mentioned (´｡• ᵕ •｡`)")
        Embed.add_field(name="🌺 .anime", value="Search for your favorite **anime**, nya~")
        Embed.add_field(name="🎵 .osu", value="Search for an **osu! user**.") 
>>>>>>> dev
        Embed.add_field(name="ℹ️ .user", value="I will show you additional info about the user you tagged ヽ(*・ω・)ﾉ")
        Embed.add_field(name="🖼️ .profileimage", value="Changes my profile image to another one on the servers (´｡• ω •｡`) ♡")
        Embed.add_field(name="💬 .status", value="Changes the Status Message of the Bot. **Admins only.**")
        Embed.add_field(name="✨.shutdown", value="The Sonico Bot will shut down. **Admins only.**")
        await client.send_message(message.channel, embed=Embed)

    #Generic Commands
    if message.content.startswith(".invite"):
        Embed = discord.Embed()
        Embed.color = discord.Color.blue()
        Embed.set_author(name="Click here to invite me to another Server, nya~", url="http://sonico.silverdroid.ga/invite.php", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version']))
        Embed.add_field(name="🎉 Invite me (´｡• ᵕ •｡`)", value="http://sonico.silverdroid.ga/invite.php   .")
        Embed.add_field(name="💾 View my code on Github!", value="http://sonico.silverdroid.ga/github.php")
        await client.send_message(message.channel, embed=Embed)
    if message.content.startswith(".about"):
        Embed = discord.Embed()
        Embed.color = discord.Color.green()
        Embed.set_author(name="About Sonico", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
<<<<<<< HEAD
        Embed.set_footer(text="Sonico - v"+str(version))
        Embed.add_field(name="🌺 Hello, I'm Sonico, nya~", value="My name is Super Sonico, I am an 18 year old college student from Japan. Well, actually I am a Bot developed by Silverdroid, Nevexo and runnerbeany (*・ω・)ﾉ")
        Embed.add_field(name="🤖", value="Bot Version: v"+str(version))
        Embed.add_field(name="📌", value="Build Number: "+str(build))
=======
        Embed.set_footer(text="Sonico - v"+str(config['info']['version']))
        Embed.add_field(name="🌺 Hello, I'm Sonico, nya~", value="My name is Super Sonico, I am an 18 year old college student from Japan. Well, actually I am a Bot developed by Silverdroid, Nevexo and runnerbeany (*・ω・)ﾉ")
        Embed.add_field(name="🤖", value="Bot Version: v"+str(config['info']['version']))
        Embed.add_field(name="📌", value="Build Number: "+str(config['info']['build']))
        await client.send_message(message.channel, embed=Embed)
    if message.content.startswith(".website"):
        Embed.set_author(name="Check out my website, nya~", url="http://sonico.silverdroid.ga", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(config['info']['version']))
        Embed.add_field(name="🌍 Sonico on the Web:", value="http://sonico.silverdroid.ga")
>>>>>>> dev
        await client.send_message(message.channel, embed=Embed)
    if message.content.startswith(".website"):
        Embed = discord.Embed()
        Embed.color = discord.Color.blue()
        Embed.set_author(name="Check out my website, nya~", url="http://sonico.silverdroid.ga", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(version))
        Embed.add_field(name="🌍 Sonico on the Web:", value="http://sonico.silverdroid.ga")
        await client.send_message(message.channel, embed=Embed)

        
    #Fun Commands
    if message.content.startswith(".cuddle"):
        if message.mentions:
            cuddled = message.mentions[0]
        else:
            cuddled = message.author
        Embed = discord.Embed(color=0xE865A0)
        Embed.add_field(name="Cuddle time! Nya~", value=message.author.name+" cuddles with "+cuddled.name)
        Embed.set_image(url="http://sonico.silverdroid.ga/img/commands/cuddle.gif")
        await client.send_message(message.channel, embed=Embed)

    if message.content.startswith(".nap"):
        if message.mentions:
            napping = message.mentions[0]
        else:
            napping = message.author
        Embed = discord.Embed(color=0xE865A0)
        Embed.add_field(name="Time to take a nap, nya~", value=message.author.name+" takes a nap with "+napping.name)
        Embed.set_image(url="http://sonico.silverdroid.ga/img/commands/nap.gif")
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

    if message.content.startswith(".anime"):
        query = message.content[6:]
        embed = discord.Embed()
        embed.title = "🌺 Anime | {0}".format(query)
        dat = mal.animu(query)
        if dat == "serverError":
            embed.description = "Sorry! Something isn't right at the moment, I'll let the developers know."
            embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
        elif dat == "credError":
            embed.description = "Sorry! Something isn't right at the moment, I'll let the developers know."
            embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
        elif dat == "noResults":
            embed.description = "I couldn't find anything, nya~ (´｡• ᵕ •｡`)"
            embed.set_image(url="http://sonico.silverdroid.ga/img/uwu.jpg")
        else:
            embed = discord.Embed()
            embed.title = "🌺 Anime | {0}".format(dat[0])
            embed.color = discord.Color.blue()
            embed.description = str(dat[1])
            embed.set_footer(text="https://myanimelist.net", icon_url='https://myanimelist.cdn-dena.com/images/faviconv5.ico')
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith(".osu"):
        query = message.content[9:]
        embed = discord.Embed()
        embed.title = "osu! | {0}".format(query)
        dat = osu.osuapi(query)
        if dat == 'serverError':
            embed.description = "Hmm... That didn't work. Try again later, nya~"
            embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
        elif dat == "credError":
            embed.description = "Hmm... Something broke. Try again later, nya~)"
            embed.set_image(url="http://sonico.silverdroid.ga/img/owo.jpg")
        elif dat == "noResults":
            embed.description = "I couldn't find anything, nya~ (´｡• ᵕ •｡`)"
            embed.set_image(url="http://sonico.silverdroid.ga/img/uwu.jpg")
        else:

            data = osu.osuapi(message.content[5:])
            Embed = discord.Embed(color=0xE865A0)
            Embed.title = 'osu! | {0}'.format(query)
            Embed.description = 'User Information for {0}'.format(query)
            Embed.set_footer(text="https://osu.ppy.sh", icon_url='https://new.ppy.sh/images/layout/osu-logo.png')
            Embed.add_field(name='🆔 User ID', value=str(data[1]))
            Embed.add_field(name='🎮 Play Count:', value=str(data[2]))
            Embed.add_field(name='🏅 Accuracy:', value=str(data[4]))
            Embed.add_field(name='🌍 Country:', value=str(data[5]))
            Embed.add_field(name='🔶 Rank', value=str(data[6]))
            Embed.add_field(name='🚀 Level:', value=str(data[7]))
            Embed.set_thumbnail(url=data[8])


            await client.send_message(message.channel, embed=Embed)

#        if message.content.startswith(".sonico"):
##        Embed = discord.Embed()
#        embed.set_author(name='Sonico')
#        embed.title = 'Sonico'
#        embed.color = discord.Color.blue()
#        embed.description = "Hellow"
#        embed.set_footer(text="heh", icon_url='http://assets.silverdroid.ga/assets/sonico/avatar.png')
#        await client.send_message(message.channel, embed=Embed)

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
            Embed = discord.Embed()
            Embed.add_field(name="✨ Shutting down.", value="Good Night, nya~")
            Embed.set_image(url="http://sonico.silverdroid.ga/img/commands/shutdown.png")
            print("Good night, nya~ (Shutting down.)")
            await client.change_presence(game=None, status='dnd')
            await client.send_message(message.channel, embed=Embed)
            time.sleep(5)
            await client.logout()
        else:
            Embed = discord.Embed()
            Embed.color = discord.Color.red()
            Embed.add_field(name="Error.", value="You don't have Permission for that, nya~ (´｡• ᵕ •｡`)")
            await client.send_message(message.channel, embed=Embed)

#@client.event
#sync def on_error(event, *args, **kwargs):
    #await client.send_message(discord.Object(id='280711593669558273'), "```Error Raised: " + str(sys.exc_info()) + "```" + "Event raised on: " + event)
#    print("An Error occured, nya~: " + str(sys.exc_info()) + "```" + "Event raised on: " + event)

try:
    client.run(config['tokens']['token'])
except Exception as e:
    print("Something has gone wrong, nya~ Error: " + str(e) + " Check your log files.")
