import discord
import asyncio
client = discord.Client()
token = '' #Insert Discord Bot Token
adminID = "" #Insert your ID to access the Admin commands
version = "1.0"
build = "1"

print("")
print("Sonico: A Bot by Silverdroid. - v."+ str(version))
print("Eating Macarons while starting up (ﾉ◕ヮ◕)ﾉ*:･")
print("")

@client.event
async def on_ready():
    print("Logged in to Discord as "+client.user.name+"#"+client.user.discriminator)
    print("User ID: "+client.user.id)
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
        Embed.add_field(name=":tada: .invite", value="Invite me to another Server. (*・ω・)ﾉ")
        Embed.add_field(name=":headphones: .about", value="Let me tell you a bit about me, nya~")
        Embed.add_field(name=":slight_smile: .avatar", value="I will show you the avatar of the specified user (´｡• ᵕ •｡`)")
        Embed.add_field(name=":information_source: .user", value="I will show you additional info about the user you tagged ヽ(*・ω・)ﾉ")
        Embed.add_field(name=":frame_photo: .profileimage", value="Changes my profile image to another one on the servers (´｡• ω •｡`) ♡")
        Embed.add_field(name=":speech_balloon: .status", value="Changes the Status Message of the Bot. **Admins only.**")
        Embed.add_field(name=":sparkles: .shutdown", value="The Sonico Bot will shut down. **Admins only.**")
        await client.send_message(message.channel, embed=Embed)

    #Generic Commands
    if message.content.startswith(".invite"):
        Embed = discord.Embed()
        Embed.color = discord.Color.blue()
        Embed.set_author(name="Click here to invite me to another Server, nya~", url="http://sonico.silverdroid.ga/invite.php", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(version))
        Embed.add_field(name=":tada: Invite me (´｡• ᵕ •｡`)", value="http://sonico.silverdroid.ga/invite.php   .")
        Embed.add_field(name=":floppy_disk: View my code on Github!", value="http://sonico.silverdroid.ga/github.php")
        await client.send_message(message.channel, embed=Embed)
    if message.content.startswith(".about"):
        Embed = discord.Embed()
        Embed.color = discord.Color.green()
        Embed.set_author(name="About Sonico", icon_url="http://assets.silverdroid.ga/assets/sonico/avatar.png")
        Embed.set_footer(text="Sonico - v"+str(version))
        Embed.add_field(name=":hibiscus: Hello, I'm Sonico, nya~", value="I am a Bot developed by Silverdroid (*・ω・)ﾉ")
        Embed.add_field(name=":robot:", value="Bot Version: v"+str(version))
        Embed.add_field(name=":pushpin:", value="Build Number: "+str(build))
        await client.send_message(message.channel, embed=Embed)

    #Misc. Commands
    if message.content.startswith(".avatar"):
        if message.mentions:
            mention = message.mentions[0]
            Embed = discord.Embed()
            Embed.color = discord.Color.blue()
            Embed.set_author(name=mention.name, icon_url=mention.avatar_url)
            Embed.set_image(url=mention.avatar_url)
            await client.send_message(message.channel, embed=Embed)
        else:
            Embed = discord.Embed()
            Embed.color = discord.Color.red()
            Embed.add_field(name="Error.", value="You haven't specified a valid user, nya~")
            await client.send_message(message.channel, embed=Embed)
    if message.content.startswith(".user"):
        if message.mentions:
            mention = message.mentions[0]
            user = mention
            Embed = discord.Embed()
            Embed.color = discord.Color.blue()
            Embed.set_image(url=mention.avatar_url)
            Embed.set_author(name="Username: "+mention.name+"#"+mention.discriminator, icon_url=mention.avatar_url)
            Embed.add_field(name="Username", value=mention.name+"#"+mention.discriminator)
            Embed.add_field(name="ID", value=mention.id)
            Embed.add_field(name="Status", value=mention.status)
            Embed.add_field(name="Playing", value=mention.game)
            if mention.bot == True:
                Embed.add_field(name="Bot?", value=":white_check_mark:")
            else:
                Embed.add_field(name="Bot?", value=":x:")
            await client.send_message(message.channel, embed=Embed)
        else:
            Embed = discord.Embed()
            Embed.color = discord.Color.red()
            Embed.add_field(name="Error.", value="You haven't specified a valid user, nya~")
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
            Embed.add_field(name=":white_check_mark: Image updated.", value="Do I look pretty? Nya~")
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
            Embed.add_field(name=":white_check_mark: Success.", value="Status updated, nya~")
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
            Embed.add_field(name=":sparkles: Shutting down.", value="Goodbye, nya~")
            print("Sonico is shutting down, nya~")
            await client.send_message(message.channel, embed=Embed)
            await client.logout()
        else:
            Embed = discord.Embed()
            Embed.color = discord.Color.red()
            Embed.add_field(name="Error.", value="You don't have Permission for that, nya~ (´｡• ᵕ •｡`)")
            await client.send_message(message.channel, embed=Embed)

client.run(token)
