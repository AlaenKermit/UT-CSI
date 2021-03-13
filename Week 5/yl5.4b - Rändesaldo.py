#ALLAN KERME // 08.12.2020
#RÄNDESALDO
sisseränne = []
väljaränne = []
erinevus = []
zip_objekt = zip(sisseränne, väljaränne)
sisserände_fail = open("sisseränne.txt", encoding = "UTF-8")
väljarände_fail = open("väljaränne.txt", encoding = "UTF-8")
#SISSERÄNNE
for i in sisserände_fail:
    sisseränne.append(int(i))
#VÄLJARÄNNE
for i in väljarände_fail:
    väljaränne.append(int(i))
#LAHUTAMINE
for sisseränne_i, väljaränne_i in zip_objekt:
    erinevus.append(sisseränne_i-väljaränne_i)
print(erinevus)
suurim = max(erinevus)
print("suurim number on: ", suurim)
#Added to GitHub on 13th of March, 2021