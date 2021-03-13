#ALLAN KERME // 10.12.2020
#ÕUNAMAHLA TEGEMINE
trikk = float(input("Sisestage õunte kogus kilogrammides: "))
def mahlapakkide_arv(trikk):
    return round(trikk * 0.4/3)
mahlapakkide_arv(trikk)
print(float(mahlapakkide_arv(trikk)))