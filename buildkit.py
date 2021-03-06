import json, sys, os, time, platform, requests
version = 1.4
cont = requests.get("http://txrd.nevexo.space/Sonico/verCache")
global newVersion
if float(cont.text.rstrip()) > float(version):
    newVersion = cont.text.rstrip()
else:
    newVersion = False
class startup:
    def cold():
        global username
        print("$$$$$$$\  $$\   $$\ $$$$$$\ $$\       $$$$$$$\  $$\   $$\ $$$$$$\ $$$$$$$$\ ")
        print("$$  __$$\ $$ |  $$ |\_$$  _|$$ |      $$  __$$\ $$ | $$  |\_$$  _|\__$$  __|")
        print("$$ |  $$ |$$ |  $$ |  $$ |  $$ |      $$ |  $$ |$$ |$$  /   $$ |     $$ |   ")
        print("$$$$$$$\ |$$ |  $$ |  $$ |  $$ |      $$ |  $$ |$$$$$  /    $$ |     $$ |   ")
        print("$$  __$$\ $$ |  $$ |  $$ |  $$ |      $$ |  $$ |$$  $$<     $$ |     $$ |   ")
        print("$$ |  $$ |$$ |  $$ |  $$ |  $$ |      $$ |  $$ |$$ |\$$\    $$ |     $$ |   ")
        print("$$$$$$$  |\$$$$$$  |$$$$$$\ $$$$$$$$\ $$$$$$$  |$$ | \$$\ $$$$$$\    $$ |   ")
        print("\_______/  \______/ \______|\________|\_______/ \__|  \__|\______|   \__|   ")
        print("No idea what you're doing? Checkout our Wiki to learn how to use BuildKit!")
        print("PLATFORM: " + str(platform.system()))
        time.sleep(0.5)
        print("Welcome to Build Kit. V:{0}\nPlease wait, Build Kit is starting cold.".format(version))
        if os.path.isfile("config.json") == False:
            print("--Stop Startup--\nLooks like config.json isn't here, make sure build kit is in the correct directory.")
            input("Press enter to continue.")
            startup.warm()
        else:
            print("Fyi, if you see an option that takes a yes or no [y/n] which ever character is in caps (Eg: [Y/n]) that option will run by just pressing enter.")
            if os.path.isfile("username.txt") == False:
                username = str(input("Enter your username (For built by)> "))
                instance = open("username.txt", "w")
                instance.write(username)
                instance.close()
                print("I've put your username into a file called username.txt, keep this file, and you won't have to type your username again.")
                time.sleep(1)
            else:
                instance = open("username.txt", "r")
                username = instance.read()
                instance.close()
                print("Welcome, " + username)
            print("Startup complete. Taking you home!")
            time.sleep(0.5)
            main.home()
class tools:
    def loadNow():
        with open('config.json') as json_data_file:
            config = json.load(json_data_file)
        return config
    def dumpNow(configuration):
        with open('config.json', 'w') as fp:
            json.dump(configuration, fp)

class main:
    def clear():
        for i in range(50):
            print("")
    def home():
        global newVersion
        global username
        main.clear()
        print("Hi, " + username)
        if newVersion != False:
            print("NEW VERSION AVAILABLE. GET IT FROM http://github.com/xSilverdroid/Sonico or use built in updater.")
        print("OS Platform: " + str(platform.system()) + " | Release: " + str(platform.release()) + "\nPython Version: " + str(sys.version_info[0]) + "." + str(sys.version_info[1]) + " Suggested version: 3.5 - 3.6")
        print("====BuildKit====")
        print("1. Start bot and up build number")
        print("2. Change version number")
        print("3. Change build number")
        print("4. Remove tokens from config.json")
        print("5. Import tokens & Admins")
        print("6. Exit")
        config = tools.loadNow()
        if newVersion != False:
            print("0. Update buildkit.py")
        print("===============")
        if config['tokens']['token'] != "":
            print("Reminder: The tokens are still in config.json, do not push to Git.")
        print("Type the number of the command you want to execute and press enter.")
        answer = int(input(">"))
        if answer == 1:
            config = tools.loadNow()
            current = config['info']['build']
            new = int(current) + 1
            config['info']['build'] = str(new)
            config['info']['builtby'] = username
            config['info']['builtat'] = str(time.strftime("%d/%m/%Y")) + " " + str(time.strftime("%H:%M:%S"))
            print("Updated build number, was: " + str(current) + " now: " + str(new))
            tools.dumpNow(config)
            print("Done, starting bot. PRESS CTRL + C ONCE (AND WAIT) TO STOP THE BOT.\n\n=======================\n")
            if platform.system() == "Linux" or platform.system().lower() == "Darwin":
                if str(sys.version_info[0]) + "." + str(sys.version_info[1]) == "3.6":
                    os.system("python3.6 Sonico.py")
                else:
                    os.system("python3.5 Sonico.py")
            else:
                os.system("Sonico.py")
            print("=======================\nThe bot has crashed/stopped.\nPress enter to continue")
            input()
        elif answer == 2:
            config = tools.loadNow()
            print("====Version Changer====\nThe current version is {0} (config.json)".format(config['info']['version']))
            inp = str(input("New version> "))
            inp2 = input("Reset build number? [Y/n]> ").lower()
            config['info']['version'] = inp
            if inp2 == "" or inp2 == "y":
                config['info']['build'] = 0
                config['info']['builtby'] = username
            print("Updated. Writing to file...")
            tools.dumpNow(config)
        elif answer == 3:
            print("====Build Number Changer====\nUnless changing the version, you shouldn't really use this tool, only if the config was destroyed.")
            inp = input("Really edit the build number? [y/N]").lower()
            if inp == "y":
                inp2 = int(input("New Build Number> "))
                config = tools.loadNow()
                config['info']['build'] = inp2
                tools.dumpNow(config)
            else:
                main.home()
        elif answer == 4:
            print("Removing tokens from config file... Just a tick.")
            config = tools.loadNow()
            config['tokens']['token'] = ""
            print("Removing Admins")
            config['admins']['admins'] = ""
            tools.dumpNow(config)
            print("Done! Safe to commit and push to Github.")
        elif answer == 5:
            print("====Token & Admin import====")
            config = tools.loadNow()
            if os.path.isfile("details.txt"):
                inp = input("Detected details file (Should contain tokens, add them now?) [Y/n]> ").lower()
                if inp == "y" or inp == "":
                    instance = open("details.txt", "r")
                    arr = []
                    for i in instance.readlines():
                        arr.append(i)
                    inp = input("Use stable token or dev token? [DEV/stable]> ").lower()
                    if inp == "dev" or inp == "":
                        config['tokens']['token'] = arr[0].rstrip()
                    else:
                        config['tokens']['token'] = arr[1].rstrip()
                    admins = input("Enter admins (Seperate with commands)> ")
                    config['admins']['admins'] = admins
                else:
                    token = input("Enter the token here (NO SPACES BEFORE OR AFTER)> ")
                    config['tokens']['token'] = token
                    admins = input("Enter admins (Seperate with commands)> ")
                    config['admins']['admins'] = admins
                    print("Done. Writing to disk...")
            else:
                token = input("Enter the token here (NO SPACES BEFORE OR AFTER)> ")
                config['tokens']['token'] = token
                admins = input("Enter admins (Seperate with commands)> ")
                config['admins']['admins'] = admins
                print("Done. Writing to disk...")
            tools.dumpNow(config)
        elif answer == 6:
            sys.exit()
        elif answer == 0:
            print("Buildkit.py updater... Downloading the new version.")
            instance = open("buildkit.py", "w")
            temp = requests.get("https://raw.githubusercontent.com/xSilverdroid/Sonico/master/buildkit.py")
            instance.write(temp.text)
            instance.close()
            print("Finished updating from origin/master. Please restart buildkit.")
            sys.exit()
        else:
            print("Please enter a number...")
        time.sleep(1)
        main.home()

startup.cold()
