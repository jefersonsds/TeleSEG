#encode:utf-8
#SCRIP DE BUSCA NO TWITTER

import requests
from bs4 import BeautifulSoup

url = u'https://twitter.com/search?q='
query = u'black mirror'

r = requests.get(url+query)
soup = BeautifulSoup(r.text, 'html.parser')

resultados = [p.text for p in soup.findAll('p', class_='tweet-text')]

print('ESTE É O RESULTADO OBTIDO PELO SCRIPT DE BUSCA NO TWITTER = ', query)
print('\n\n', resultados)

text_file = open("SCRIPTS/texto.txt", "w")

text_file.write("Nem tudo que não é verdade é mentira -Black Mirror \n")
text_file.write("BLACKMIRROR ON TW: %s" % resultados)
text_file.close()

#END
