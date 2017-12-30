import requests
from bs4 import BeautifulSoup

url = 'http://services.runescape.com/m=hiscore_oldschool/overall.ws'

#headers = {
#    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

#r = requests.get(url, headers=headers)

r = requests.get(url)

# make sure that the page exist

if r.status_code == 200:
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('h1')
    if title is not None:
        title_text = title.text.strip()
