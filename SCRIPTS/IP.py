#_*_ coding: utf-8 _*_

import requests
import json
import sys
import socket
import os

####EXTERNAL####
solicita = requests.get('http://ip-api.com/json')
rede = json.loads(solicita.text)

#Grava um txt
sys.stdout = open('rede.txt', 'w')

#Define o que buscar na API IP-API.com
print('PROVEDOR: ', rede['as'], '\n')
print('CIDADE: ', rede['city'], '\n')
print('PAÍS: ', rede['country'], '\n')
print('ISP: ', rede['isp'], '\n')
print('IP EXTERNO: ', rede['query'], '\n')
print('ESTADO: ', rede['region'], '\n')
print('STATUS: ', rede['status'], '\n')

####INTERNAL####
gw = os.popen("ip -4 route show default").read().split()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw[2], 0))
ipaddr = s.getsockname()[0]
gateway = gw[2]
host = socket.gethostname()
print ("IP Interno:", ipaddr, "\n")
print("GW: ", gateway, "\n")
print("Hostname: ", host, "\n")

#END
