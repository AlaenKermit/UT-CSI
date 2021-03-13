#ALLAN KERME // 03.11.2020
#NÄDALA AJAKULU
ainepunktid = int(input("Sisestage ainepunktide arv: ")) # küsib kasutajalt ainepunktide arvu
ajakulu = ainepunktid * 26 # korrutab ainepunktide arvu kolmega, ülikooli 1 ainepunkt = 26 tundi
nädalaarv = int(input("Sisestage nädalate arv: ")) # küsib kasutajalt nädalate arvu
ajaasi2 = ajakulu / nädalaarv # jagab kaks muutujat
ümardatud = round(ajaasi2) # ümardab muutuja ajaasi2 tulemuse
print(ümardatud) # väljendab ümardatud vastuse tulemuse
#Added to GitHub on 13th of March, 2021