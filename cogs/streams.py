import requests
import json

print("\n--------------------------------------------------------------------")
print("Streams cog - version 1.0 [made with <3 by github.com/runnerbeany]")
print("--------------------------------------------------------------------\n")



class twitch:
    def twitchAPI(query):
        r = requests.get('https://api.twitch.tv/kraken/channels/{0}?client_id=rebrts6nfuqhwkqzi5jt3b8yrtcl6o'.format(query))
        dat = r.json()
        print(dat)
        #dat = dat[0]
            #    first_dat = dat[0]

        data = []
        data.append(dat['display_name'])
        data.append(dat['followers'])
        data.append(dat['game'])
        data.append(dat['logo'])
        data.append(dat['status'])
        data.append(dat['url'])
        return data


#data = twitch.twitchAPI('runnerbeany')
#print(str(data))

class beam:
    def beamAPI(query):
        r = requests.get('https://beam.pro/api/v1/channels/{0}')
