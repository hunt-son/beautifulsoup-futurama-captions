from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.aeromental.net/2010/01/03/futurama-intros-all-opening-subtitles-tag-lines/")

# html.encode('utf8')

with open('futurama-captions.txt','w') as text:
 	soup = BeautifulSoup(html.text, 'html.parser')
 	soup = soup.find('body')
 	text.write(soup.prettify())


# for li in soup.find_all('li'):
# 	print(li)
# print (soup.prettify)
# text = open('futurama-captions.txt')
# text.write(soup)
# text.close()
