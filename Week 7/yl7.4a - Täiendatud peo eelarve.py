#ALLAN KERME // 10.12.2020
#PEO EELARVE
failinimi = str(input("sisestage failinimi pls: "))
fail = open(failinimi, encoding = "UTF-8")
tulemas = 0
kutsutud = 0
for i in fail:
    if "+" in i:
        tulemas = tulemas + 1
    if "?" in i:
        kutsutud = kutsutud + 1
võimalik_kokku = tulemas + kutsutud
rent = 55
fpp = 10
def eelarve(y):
    return y * fpp + rent
print("Maksimaalne eelarve:", eelarve(võimalik_kokku))
print("Minimaalne eelarve:", eelarve(tulemas))
