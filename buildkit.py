import json, sys, os, time
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
        version = 1.0
        print("Welcome to Build Kit. V:{0}\nPlease wait, Build Kit is starting cold.".format(version))
        if os.path.isfile("config.json") == False:
            print("--Stop Startup--\nLooks like config.json isn't here, make sure build kit is in the correct directory.")
            input("Press enter to continue.")
            startup.warm()
        else:
            print("Fyi, if you see an option that takes a yes or no [y/n] which ever character is in caps (Eg: [Y/n]) that option will run by just pressing enter.")
            username = str(input("Enter your username (For built by)> "))
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
        global username
        main.clear()
        print("Hi, " + username)
        print("====BuildKit====")
        print("1. Start bot and up build number")
        print("2. Change version number")
        print("3. Change build number")
        print("4. Remove tokens from config.json")
        print("5. Import tokens & Admins")
        print("6. Exit")
        print("===============")
        print("Type the number of the command you want to execute and press enter.")
        answer = int(input(">"))
        if answer == 1:
            config = tools.loadNow()
            current = config['info']['build']
            new = int(current) + 1
            config['info']['build'] = str(new)
            config['info']['builtby'] = username
            print("Updated build number, was: " + str(current) + " now: " + str(new))
            tools.dumpNow(config)
            print("Done, starting bot. PRESS CTRL + C ONCE (AND WAIT) TO STOP THE BOT.\n\n=======================\n")
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
            token = input("Enter the token here (NO SPACES BEFORE OR AFTER)> ")
            config = tools.loadNow()
            config['tokens']['token'] = token
            admins = input("Enter admins (Seperate with commands)> ")
            config['admins']['admins'] = admins
            print("Done. Writing to disk...")
            tools.dumpNow(config)
        elif answer == 6:
            sys.exit()
        else:
            print("Please enter a number...")
        time.sleep(1)
        main.home()

startup.cold()
