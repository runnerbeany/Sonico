import requests
from xml.etree import ElementTree
print("\nMy Anime List APi collector\nBy Nevexo V:1.0\n")
class mal:
    def animu(query):
        r = requests.get('https://myanimelist.net/api/anime/search.xml?q={0}'.format(query), auth=('SonicoDiscord', 'oEDEqFaj0zYHfv8RR32cjfwCF9L8Bl'))
        if r.status_code == 201:
            return "noResults"
        if r.text == "Invalid credentials":
            return "credError"
        dat = r.text
        if dat == '':
            return "noResults"
        e = ElementTree.fromstring(dat)
        if len(e) == 0:
            return "noResults"
        else:
            entry = e[0]

        return entry[2].text, entry[10].text.replace("<br />", "")
