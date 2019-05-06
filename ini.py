# -*- coding: utf-8 -*-
import telebot
from telebot import types
import os
import requests
import platform
import subprocess
import json
so = platform.system()

VER="0.1.1 | QTDE de CMDs = 09"

#DEFINIR SEU TOKEN ENTRE AS ' '
TOKEN = ' '
bot = telebot.TeleBot(TOKEN)

#====INÍCIO DOS COMANDOS====#

#==>Exibe o Menu de Comandos
@bot.message_handler(commands=['start'])
def comando_start(mensagem):
   chat_id = mensagem.chat.id
   start = open('start.txt', 'r').read()
   bot.send_message(chat_id, start)

#==> Easter EGG
@bot.message_handler(commands=['egg'])
def comando_egg(mensagem):
   chat_id = mensagem.chat.id
   os.system("SCRIPTS/execegg.sh")
   myegg = open('SCRIPTS/texto.txt', 'r').read()
   bot.send_message(chat_id, myegg)

#==> Realiza busca no Twitter do @CVEnew
@bot.message_handler(commands=['cve'])
def comando_cve(mensagem):
   chat_id = mensagem.chat.id
   os.system("SCRIPTS/execCVE.sh")
   cve = open('SCRIPTS/twitterCVE.txt', 'r').read()
   bot.send_message(chat_id, cve)

#==> Tempo de Dispositivo ligado
@bot.message_handler(commands=['uptime'])
def comando_uptime(mensagem):
    chat_id = mensagem.chat.id
    mensagemTmp = subprocess.check_output(["uptime"])
    bot.send_message(chat_id, mensagemTmp)

#==> Nome do Raspberry
@bot.message_handler(commands=['hostname'])
def comando_uptime(mensagem):
    chat_id = mensagem.chat.id
    mensagemHost = subprocess.check_output(["hostname"])
    bot.send_message(chat_id,  mensagemHost)

#==> Info sobre ip/provedor/etc
@bot.message_handler(commands=['ipx'])
def comando_ipx(mensagem):
   chat_id = mensagem.chat.id
   os.system("SCRIPTS/IP.sh")
   ipx = open('SCRIPTS/rede.txt', 'r').read()
   bot.send_message(chat_id, ipx)

#==> Lista de Câmeras púlicas em BH
@bot.message_handler(commands=['cameras'])
def comando_cameras(mensagem):
   chat_id = mensagem.chat.id
   os.system("SCRIPTS/cameras.sh")
   cam = open('SCRIPTS/cameras.txt', 'r').read()
   bot.send_message(chat_id, cam)

#==> Top notícias de Tecnologia G1
@bot.message_handler(commands=['news'])
def comando_news(mensagem):
   chat_id = mensagem.chat.id
   os.system("SCRIPTS/news.sh")
   news = open('news.txt', 'r').read()
   bot.send_message(chat_id, news)

#==> Lista de Asteroides
@bot.message_handler(commands=['spaco'])
def comando_spaco(mensagem):
   chat_id = mensagem.chat.id
   os.system("SCRIPTS/spaco.sh")
   spaco = open('spaco', 'r').read()
   bot.send_message(chat_id, spaco)

#==> Info sobre o clima da Região
@bot.message_handler(commands=['clima'])
def comando_clima(mensagem):
   chat_id = mensagem.chat.id
   os.system("SCRIPTS/clima.sh")
   clima = open('SCRIPTS/clima.txt', 'r').read()
   bot.send_message(chat_id, clima)

#====END OF COMMANDS====#

print('Esperando Comandos')
print('VERSÃO:', VER)
des = open('desenho.txt', 'r').read()
print(des)

#CRIA LOOP!
bot.polling(none_stop = True)

