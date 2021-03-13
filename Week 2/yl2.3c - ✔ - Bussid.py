#ALLAN KERME // 09.11.2020
#BUSSID
inimeste_arv = int(input("Inimeste arv: ")) #Kokku
kohtade_arv = int(input("Kohtade arv: ")) #Bussis
busside_arv = inimeste_arv // kohtade_arv
puudu = inimeste_arv % kohtade_arv
if puudu == 0:
    print("Kokku on vaja", busside_arv, "bussi!")
else:
    print("Kokku on vaja", busside_arv + 1, "bussi!")
if inimeste_arv == kohtade_arv * busside_arv:
    puudu = kohtade_arv
print("Kokku on viimases bussis:", puudu, "inimest.")