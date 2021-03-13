#ALLAN KERME // 25.11.2020
#MALE
arv = int(input("Sisestage täisarv: "))
arv2 = 2
astendaja = 0
while arv:
    if arv <= 64:
        arv3 = arv2**astendaja
        arv = arv - 1
        astendaja = astendaja + 1
print("Leiutaja küsis", arv3, "nisutera")
#Added to GitHub on 13th of March, 2021