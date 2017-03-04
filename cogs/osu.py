import requests
import json

print("osu! API v1.1\nBy runnerbeany & Nevexo\ngithub.com/runnerbeany github.com/nevexo\n")

class osu:
    def osuapi(query):
        r = requests.get('https://osu.ppy.sh/api/get_user?u={0}&k=dfc290ab0fca5d8e54b6eb28d9134407b4723b48'.format(query))
        dat = r.json()
        dat = dat[0]
        usr = dat['username']
        usrid = dat['user_id']
        count300 = dat['count300']
        playcount = dat['playcount']
        acc = dat['accuracy']
        country = dat['country']
        return usr,usrid,count300,playcount,acc,country

        print(r.status_code)
        if r.status_code == 200:
            print('Response Code OK. (200)')
        if r.status_code == 201:
            return noResults
        if r.text == "Invalid Credentials":
            return 'credError'

        if dat == '':
            return 'noResults'
