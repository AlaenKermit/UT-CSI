#ALLAN KERME // 02.11.2020
#TRAHV
maksimaalmaar = 190 # määrame maksimaalmäära
nimi = str(input("Sisestage oma nimi: ")) # küsib kasutajalt nime
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): ")) # küsib lubatud kiirust
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): ")) # küsib tegelikku kiirust
esialgne_tulemus = tegelik_kiirus - lubatud_kiirus # lahutab tegelikust kiirusest lubatud kiiruse
trahvisumma = esialgne_tulemus * 3 # eelneva vastuse korrutab kolmega
maksimaalmaara_kontroll = min(maksimaalmaar, trahvisumma) # laseme läbi maksimaalkontrolliks et trahv ei ületaks 190€
print(nimi + ", kiiruse ületamise eest on teie trahv", maksimaalmaara_kontroll, "eurot.") # väljastame tulemuse