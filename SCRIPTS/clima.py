#_*_ coding: utf-8 _*_

import requests
import json
import sys

#Onde BRXX0033 corresponde ao código da Cidade
solicita = requests.get('https://api.hgbrasil.com/weather/?format=json&cid=BRXX0033')
clima = json.loads(solicita.text)

#Grava um txt 
sys.stdout = open('SCRIPTS/clima.txt', 'w')

#Define o que buscar na API do Clima Online
print('Condições Climáticas para', clima['results']['city_name'], '\n')
print('Data: ', clima['results']['date'])
print('Hora: ',clima['results']['time'])
print('Período: ',clima['results']['currently'])
print('Veloc. Vento: ', clima['results']['wind_speedy'])
print('Condições: ', clima['results']['description'])

#END
