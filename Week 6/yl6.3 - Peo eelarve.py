#ALLAN KERME // 10.12.2020
#PEO EELARVE
kutsutud = int(input("Mitu inimest on kutsutud? "))
inimesi = int(input("Mitu inimest tuleb? "))
rent = 55
fpp = 10
def eelarve(y):
    return y * fpp + rent
print("Maksimaalne eelarve:", eelarve(kutsutud))
print("Minimaalne eelarve:", eelarve(inimesi))
#Added to GitHub on 13th of March, 2021