#ALLAN KERME // 05.11.2020
#SISSEASTUMINE TARTU ÜLIKOOLI INFORMAATIKA BAKALAUREUSEÕPPESSE
punktisumma = float(input("Sisestage punktisumma: ")) # Küsime kasutajalt punktisumma
if punktisumma >= 85 and punktisumma <= 100: # vaatame kas puntkisumma on 84st suurem ja 101st väiksem
    print("Vastuvõtt tagatud") # kui eelmised parameetrid vastavad tõele siis väljundiks see
elif punktisumma >= 66 and punktisumma < 85: # vaatame kas punktisumma on suurem ja võrdne 66ga ja väiksem kui 85
    print("Kandideerimine vastuvõtule") # kui jah siis väljendame selle
elif punktisumma < 66 and punktisumma >= 0: # vaatame kui punktisumma on väiksem kui 66 ja suurem ja võrdne 0iga
        print("Vähem kui kandideerimiseks vajalik") # kui jah siis väljendame
else:
        print("Vigane punktisumma") # annab väljundiks veateate
#Added to GitHub on 13th of March, 2021