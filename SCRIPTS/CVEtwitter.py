#encode:utf-8
import requests
from bs4 import BeautifulSoup

#Caso for Usar o TW como buscador de determinada palavra, use a URL:https://twitter.com/search?q=
# E em query adicione a palavra desejada

url = u'https://twitter.com/CVEnew/'
#query = u'last'

r = requests.get(url) #acrescente url+query para ativar o modo busca
soup = BeautifulSoup(r.text, 'html.parser')

resultados = [p.text for p in soup.findAll('p', class_='tweet-text')]

print('RESULTADOS OBTIDOS VIA TWITTER DATABASE CVE EXPLOIT @CVEnew')
print('\n\n', resultados)

text_file = open("SCRIPTS/twitterCVE.txt", "w")
text_file.write("LISTA DE CVEs EXPLOIT-DB: %s" % resultados)
text_file.close()

#END
