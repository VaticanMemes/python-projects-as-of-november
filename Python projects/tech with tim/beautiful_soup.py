import requests
from bs4 import BeautifulSoup

URL = "http://motherfuckingwebsite.com/"
r = requests.get(URL)
# print(r.content)

soup = BeautifulSoup(r.content, 'lxml')

for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))

"""
rows = soup.select('tbody tr')

for i in rows:
    name = i.select_one('.source-title').text.strip()
    print(name)
"""