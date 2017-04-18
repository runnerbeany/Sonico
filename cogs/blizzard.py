import requests, json
print("-------------------------------------------------------------------------------------------------------------\n")
print("Blizzard v0.1 API collector starting. github.com/runnerbeany | API by https://github.com/SunDwarf/OWAPI\n")
print("-------------------------------------------------------------------------------------------------------------\n")

class blizzard:
    def ow(query):
        r = requests.get('https://owapi.net/api/v3/u/runnerbeany/stats'.format(query))
        dat = r.json
        print(dat)
