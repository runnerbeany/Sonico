print("Starting up...\nSonico Discord Bot remote update harness\nNOTE: Updates rolled out take up to an hour to be applied across the network.\nDeveloper: Nevexo.\n\nChecking Dependencies... ", end="")
import requests, time, json, sys, os
print("[OK]")
print("\n\nChecking Github...", end="")
r = requests.get("https://raw.githubusercontent.com/xSilverdroid/Sonico/master/config.json")
if r.status_code == 200:
    print("[OK]")
else:
    print("[FAIL] " + str(r.status_code))
    sys.exit()
print("\n\nChecking local files... ", end="")
if os.path.exists("datastore.txt"):
    print("[OK]")
else:
    print("[FAIL] - Creating datastore.txt...")
    instance = open("datastore.txt", "w")
    instance.write("0")
    instance.close()
print("\n\nStartup complete. Monitoring will start now.")
while True:
    remote = requests.get("https://raw.githubusercontent.com/xSilverdroid/Sonico/master/config.json")
    remotedat = remote.json()
    print("Version in remote: " + remotedat['info']['version'])
    instance = open("datastore.txt", "r")
    localdat = instance.read()
    instance.close()
    print("Version on local: " + localdat)
    if float(remotedat['info']['version']) > float(localdat):
        print("---\nUpdate found, version " + remotedat['info']['version'] + " by: " + remotedat['info']['builtby'] + "\nThis version is in the release branch. I'm gonna deploy it.\n\nWriting Update to Disk...", end="")
        os.system("git clone https://github.com/xSilverdroid/Sonico.git")
        print("[OK]")
        print("\n\nWriting to datastore...", end="")
        instance = open("datastore.txt", "w")
        instance.write(remotedat['info']['version'])
        print("[OK]\n\nDisk writing complete, restarting run environment.", end="")
        print("[OK] - Update finished, going back into loop.")
    time.sleep(5)
