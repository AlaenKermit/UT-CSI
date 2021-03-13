#ALLAN KERME // 10.12.2020
#TAHVLI JUURDE
from datetime import *
nimekiri = []
failinimi_kysimus = str(input("Sisestage failinimi: "))
fail = open(failinimi_kysimus, encoding = "UTF-8")
for i in fail:
    nimekiri.append(i)
    #print(i)
#print(datetime.now().day)
number = datetime.now().day - 1
print(nimekiri[number])
#Added to GitHub on 13th of March, 2021