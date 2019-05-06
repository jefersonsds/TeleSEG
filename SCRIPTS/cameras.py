#_*_ coding: utf-8 _*_

import urllib.request
from bs4 import BeautifulSoup
import re

opener = urllib.request.build_opener()
opener.addheaders = [('USer-agent', 'Mozilla/5.0')]

#O Site Abaixo pode Ser alterado para outros resultados
url = 'http://aconteceunovale.com.br/portal/?p=38980'
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl)

#title = soup.title.text

body = soup.find(text="Outras Câmeras:").findNext('')

#TXT de I/O de Dados
outfile = open('cameras.txt', 'w')

outfile.write("Algumas das Câmeras Públicas de BH:\n")
outfile.write(body.text)
outfile.write("\n\n")

