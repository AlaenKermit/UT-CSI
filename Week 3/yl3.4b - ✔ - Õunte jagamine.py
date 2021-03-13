#ALLAN KERME // 25.11.2020
#ÕUNTE JAGAMINE
from random import randint
arv = 0
koguarv = 0
helbearv = 0
pöialpoisiarv = int(input("mitu pöialpoissi tahab õunu: "))

while pöialpoisiarv > arv:
    õunaarv = randint(1,2)
    arv = arv + 1
    print(õunaarv)
    koguarv+= õunaarv
    helbearv = 14 - koguarv
if pöialpoisiarv == 0:
    helbearv = 14
    
print("lumevalgekesele jääb alles", helbearv, "õuna")
#Added to GitHub on 13th of March, 2021