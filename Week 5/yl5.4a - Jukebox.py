#ALLAN KERME // 08.12.2020
#JUKEBOX



failinimi = str(input("Tere, Palun sisestage failinimi koos laiendiga .txt: "))
readfailist = open(failinimi, encoding = "UTF-8")
eighties = []
counter = 0
for i in readfailist:
    counter = counter + 1
    print(str(counter) + '.' , i)
    eighties.append(str(i))
lauluvalik = int(input("Valige laulu järjekorranumber"))
valik1 = lauluvalik - 1
print(eighties[valik1])