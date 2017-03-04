import requests
import json

print("osu! API v1.0\nBy runnerbeany\ngithub.com/runnerbeany\n")

class osu:
    def osuapi(query):
        r = requests.get('https://osu.ppy.sh/api/get_user?u={0}&k=dfc290ab0fca5d8e54b6eb28d9134407b4723b48&u=username'.format(query))
        dat = json.loads(r.text)
        text = list[r.text]
        userid = dat['user_id']
        username = dat['username']
        count50 = dat['count50']
        country = dat['country']
        return userid,username,count50,country

        print(r.status_code)
        if r.status_code == 200:
            print('Response Code OK. (200)')
        if r.status_code == 201:
            return noResults
        if r.text == "Invalid Credentials":
            return 'credError'

        if dat == '':
            return 'noResults'
