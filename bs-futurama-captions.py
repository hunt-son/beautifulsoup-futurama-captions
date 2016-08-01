from bs4 import BeautifulSoup
soup = BeautifulSoup('http://www.aeromental.net/2010/01/03/futurama-intros-all-opening-subtitles-tag-lines/', 'html.parser').find('id=content').findall('em')

text = open('futurama-captions.txt')
text.write(soup)
text.close()
