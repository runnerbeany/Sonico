import requests
import json

print("osu! API v1.3\nBy runnerbeany & Nevexo\ngithub.com/runnerbeany github.com/nevexo\n")

class osu:
    def osuapi(query):
        r = requests.get('https://osu.ppy.sh/api/get_user?u={0}&k=dfc290ab0fca5d8e54b6eb28d9134407b4723b48'.format(query))
        dat = r.json()
        dat = dat[0]
        avatar = "https://a.ppy.sh/{0}_120.png".format(dat['user_id'])
        data = []
        data.append(dat['username'])
        data.append(dat['user_id'])
        data.append(dat['count300'])
        data.append(dat['playcount'])
        data.append(dat['accuracy'])
        data.append(dat['country'])
        data.append(dat['pp_rank'])
        data.append(dat['level'])
        data.append(avatar)
        return data

        print(r.status_code)
        if r.status_code == 200:
            print('Response Code OK. (200)')
        if r.status_code == 201:
            return noResults
        if r.text == "Invalid Credentials":
            return 'credError'

        if dat == '':
            return 'noResults'

data = osu.osuapi('silverdroid')
print(str(data))
