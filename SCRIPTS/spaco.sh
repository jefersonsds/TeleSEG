#!/bin/bash
#BUSCA UMA LISTA DE ASTEROIDES DE ESTAO PROXIMOS DA TERRA

printf "Lista dos Asteroides nas proximidades da terra\n\n"
echo "http://www.astronoo.com/pt/artigos/asteroides-proximos-da-terra-mapa-do-ceu.html" |  #DEFINA O SITE A SER ANALISADO
   wget -O- -i- |
   hxnormalize -x |
   hxselect -i "table.tableEdition" |  #DEFINA A CLASS DA PAGINA HTML
   lynx -stdin -dump > spaco #ARQUIVO DE TEXTO COM OS DADOS
