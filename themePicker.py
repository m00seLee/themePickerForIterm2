import requests
from bs4 import BeautifulSoup
import re
import random

resp = requests.get('https://iterm2colorschemes.com/')
soup = BeautifulSoup(resp.text, 'lxml')
skipBS = 0
themes = []
for line in soup.find_all('p'):
	if skipBS > 2 and line.text != '':
		themes.append((line.text))
	skipBS += 1

randomIndex = random.randint(0, len(themes))
print(themes[randomIndex])
