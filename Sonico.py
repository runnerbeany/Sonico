import discord, asyncio, time, datetime, os, logging, sys, config
from cogs.mal import mal
from cogs.osu import osu
client = discord.Client()
token = config.token #Insert Discord Bot Token
adminID = config.admins #Insert your ID to access the Admin commands
version = "1.0"
build = "3"



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

print("")
print("Sonico: A Bot by Silverdroid. - v."+ str(version))
print("Eating Macarons while starting up")
print("")
@client.event
async def on_ready():
    print("Logged in to Discord as "+client.user.name+"#"+client.user.discriminator)
    print("User ID: "+str(client.user.id))
    print("")
    await client.change_presence(game=discord.Game(name=".help (*・ω・)ﾉ | v"+str(version)))
    print("Sonico is ready, nya~")
@client.event
async def on_message(message):
    if message.content.startswith(".help"):
        Embed = discord.Embed()
        Embed.color = discord.Color.green()
        Embed.set_author(name="Sonico Help", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(version))
        Embed.add_field(name="Hey! I'm Sonico ♡", value="I am a Bot developed by Silverdroid. Let me show you what I can do!")
        Embed.add_field(name="🎉 .invite", value="Invite me to another Server. (*・ω・)ﾉ")
        Embed.add_field(name="🎧 .about", value="Let me tell you a bit about me, nya~")
        Embed.add_field(name="🙂 .avatar", value="I will show you the avatar of the specified user (´｡• ᵕ •｡`)")
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
        Embed.set_footer(text="Sonico - v"+str(version))
        Embed.add_field(name="🎉 Invite me (´｡• ᵕ •｡`)", value="http://sonico.silverdroid.ga/invite.php   .")
        Embed.add_field(name="💾 View my code on Github!", value="http://sonico.silverdroid.ga/github.php")
        await client.send_message(message.channel, embed=Embed)
    if message.content.startswith(".about"):
        Embed = discord.Embed()
        Embed.color = discord.Color.green()
        Embed.set_author(name="About Sonico", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(version))
        Embed.add_field(name="🌺 Hello, I'm Sonico, nya~", value="I am a Bot developed by Silverdroid (*・ω・)ﾉ")
        Embed.add_field(name="🤖", value="Bot Version: v"+str(version))
        Embed.add_field(name="📌", value="Build Number: "+str(build))
        await client.send_message(message.channel, embed=Embed)

    #Misc. Commands
    if message.content.startswith(".avatar"):
        if message.mentions:
            mention = message.mentions[0]
        else:
            mention = message.author
        Embed = discord.Embed()
        Embed.color = discord.Color.blue()
        Embed.set_author(name=mention.name, icon_url=mention.avatar_url)
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
        Embed.set_author(name="Username: "+mention.name+"#"+mention.discriminator, icon_url=mention.avatar_url)
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
        embed.title = "Animu | {0}".format(query)
        dat = mal.animu(query)
        if dat == "serverError":
            embed.description = "Sorry! Something isn't right at the moment, I've let the developers know."
        elif dat == "credError":
            embed.description = "Sorry! Something isn't right at the moment, I've let the developers know."
        elif dat == "noResults":
            embed.description = "Awh shucks, I didn't find anything for that search query!"
        else:
            embed = discord.Embed()
            embed.title = "Animu | {0}".format(dat[0])
            embed.color = discord.Color.blue()
            embed.description = str(dat[1])
            embed.set_footer(text="https://myanimelist.net", icon_url='https://myanimelist.cdn-dena.com/images/faviconv5.ico')
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith(".osu"):
        query = message.content[3:]
        embed = discord.Embed()
        embed.title = "OSU | {0}".format(query)
        dat = osu.osuapi(query)
        if dat == 'serverError':
            embed.description = "Hmm. That didn't work. Try again later!"
        elif dat == "credError":
            embed.description = "Hmm... Something broke. Try again later! (devs notified!)"
        elif dat == "noResults":
            embed.description = "We've come up empty! Try a different query."
        else:
            embed = discord.Embed()
            embed.title = 'OSU | {0}'.format(query)
            embed.color = discord.Color.pink()
            embed.description = str(dat[1])
            embed.set_footer(text="https://osu.ppy.sh", icon_url='https://www.google.co.uk/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjql4Kqu7vSAhVB2BQKHZ1aAawQjRwIBw&url=https%3A%2F%2Ftwitter.com%2Fosugame&psig=AFQjCNHeijIEM3Li8yl682_Z9cHtEy2qEw&ust=1488669269628818')
            await client.send_message(message.channel, embed=Embed)
    #Admin Commands
    if message.content.startswith(".profileimage"):
        if message.author.id == adminID:
            print("Updating profile image, nya~")
            message_id = await client.send_message(message.channel, ":clock2: Updating profile image, nya~")
            if "default" in message.content.lower():
                file = "images/avatar.png"
            elif "macaron" in message.content.lower():
                file = "images/macaron.jpg"
            elif "music" in message.content.lower():
                file = "images/music.jpg"
            else:
                Embed = discord.Embed()
                Embed.color = discord.Color.red()
                Embed.add_field(name="Error.", value="Nani? That image doesn't exist, nya~ (´｡• ᵕ •｡`)")
                await client.send_message(message.channel, embed=Embed)
                return
            logo = open(file,"rb")
            await client.edit_profile(avatar=logo.read())
            await client.delete_message(message_id)
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
            Embed.color = discord.Color.green()
            Embed.add_field(name="✨ Shutting down.", value="Goodbye, nya~")
            print("Sonico is shutting down, nya~")
            await client.send_message(message.channel, embed=Embed)
            await client.logout()
        else:
            Embed = discord.Embed()
            Embed.color = discord.Color.red()
            Embed.add_field(name="Error.", value="You don't have Permission for that, nya~ (´｡• ᵕ •｡`)")
            await client.send_message(message.channel, embed=Embed)

@client.event
async def on_error(event, *args, **kwargs):
    #await client.send_message(discord.Object(id='280711593669558273'), "```Error Raised: " + str(sys.exc_info()) + "```" + "Event rasied on: " + event)
    print("Error Raised: " + str(sys.exc_info()) + "```" + "Event rasied on: " + event)

try:
    client.run(token)
except Exception as e:
    print("Something has gone wrong. Err: " + str(e) + " Check your log files.")
