#ALLAN KERME // 10.12.2020
#PÄEVIK
from datetime import datetime
sissekanne = str(input("Sisesta sissekande tekst: "))
kuupäev_kellaaeg = datetime.today()
päevik = open("paevik.txt", "a", encoding="UTF-8")
päevik.write(str(kuupäev_kellaaeg) + "\n")
päevik.write(sissekanne + "\n")
päevik.close()
#Added to GitHub on 13th of March, 2021