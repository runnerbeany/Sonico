import requests
import json

print("\n--------------------------------------------------------------------")
print("Streams cog - version 0.1 [made with <3 by github.com/runnerbeany]")
print("--------------------------------------------------------------------\n")



class twitch:
    def twitchAPI(query):
        r = requests.get('https://api.twitch.tv/kraken/users/{0}?client_id=rebrts6nfuqhwkqzi5jt3b8yrtcl6o'.format(query))
        dat = r.json()
        dat = [0]
        data = []
        data.append(dat['name'])
        data.append(dat['display_name'])
        data.append(dat['logo'])
        data.append(dat['bio'])
        return data

data = twitch.twitchAPI('runnerbeany')
print(data)

class beam:
    def beamAPI(query):
        r = requests.get('https://beam.pro/api/v1/channels/{0}')
