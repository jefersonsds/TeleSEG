#!/bin/bash
#REALIZA UMA BUSCA NO SITE DO G1 no TOP Tecnologia

printf "TOP NOTÍCIAS G1 TECNOLOGIAa\n\n"
echo "http://g1.globo.com/tecnologia/" |  #DEFINA O SITE A SER ANALISADO
   wget -O- -i- |
   hxnormalize -x |
   hxselect -i "div.area-direita-a" |  #DEFINA A CLASS DA PAGINA HTML
   lynx -stdin -dump > news.txt #ARQUIVO DE TEXTO COM OS DADOS

