#ALLAN KERME // 10.12.2020
#TERVITUSED MÕTISKLUSTEGA
def tervitus(x):
        print("Võõrustaja:","Tere!")
        print("Täna", number, "kord tervitada, mõtiskleb võõrustaja")
        print("Külaline:", "Tere, suur tänu kutse eest!")
võõrustaja_kordade_arv = 0
kordus = int(input("Sisestage külaliste arv: "))
i = 1
number = 0
while i <= kordus:
    i = i + 1
    number = number + 1
    tervitus(kordus)