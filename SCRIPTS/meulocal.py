#_*_ coding: utf-8 _*_

import urllib.request
from bs4 import BeautifulSoup
import re

opener = urllib.request.build_opener()
opener.addheaders = [('USer-agent', 'Mozilla/5.0')]

#O Site Abaixo pode Ser alterado para outros resultados
url = 'https://geoiptool.com/pt/'
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl)

#title = soup.title.text

body = soup.find(text="Código do país:").findNext('')
body2 = soup.find(text="País:").findNext('')
body3 = soup.find(text="Latitude:").findNext('')
body4 = soup.find(text="Região:").findNext('')
body5 = soup.find(text="Cidade:").findNext('')

#TXT de I/O de Dados
outfile = open('meulocal.txt', 'w')


outfile.write("Onde o host está: ")
outfile.write(body.text)
outfile.write("\n\n")

outfile.write("No País: ")
outfile.write(body2.text)
outfile.write("\n\n")

outfile.write("A longitude é: ")
outfile.write(body3.text)
outfile.write("\n\n")

outfile.write("O Estado é: ")
outfile.write(body4.text)
outfile.write("\n\n")

outfile.write("A Cidade é( APROX ): ")
outfile.write(body5.text)
outfile.write("\n\n")

