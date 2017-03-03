import requests
import json

print("OSU Api v1.0\nBy runnerbeany\ngithub.com/runnerbeany\n")

class osu:
    def osuapi(query):
        r = requests.get('https://osu.ppy.sh/api/get_user/?u={0}&k=4f8f4a5f60a915d0077905f71b36919479ed4073'.format(query))
        dat == r.text
        dat = json.load(r.text)
        userid = dat['user_id']
        username = dat['username']
        count50 = dat['count50']
        country = dat['country']
        return userid,username,count50,country

        print(r.status_code)
        if r.status_code == 200:
            print('Response code was 200 OK.')
        if r.status_code == 201:
            return noResults
        if r.text == "Invalid Credientials":
            return 'credError'

        if dat == '':
            return 'noResults'
