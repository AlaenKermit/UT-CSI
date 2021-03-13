#ALLAN KERME // 10.12.2020
#BÄNNER
def banner(x):
    return x.upper()
kordus = int(input("Mitu korda soovite reklaamlauset kuvada? "))
lause = str(input("Sisestage reklaamlause: "))
i = 1
while i <= kordus:
    i = i + 1
    print(banner(lause))