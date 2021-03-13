#ALLAN KERME // 25.11.2020
#JÄNESEVANEMATE MURE VER.2
ringide_arv = int(input("sisestage ringide arv: "))
porgandite_koguarv = 0

if ringide_arv == 1:
    print(0)

if ringide_arv % 2 == 0:
    while ringide_arv in range(porgandite_koguarv, ringide_arv):
        porgandite_koguarv = porgandite_koguarv + ringide_arv
        ringide_arv = ringide_arv - 2
        if ringide_arv == 0:
            print(porgandite_koguarv)

if ringide_arv % 2 != 0:
    ringide_arv = ringide_arv - 1
    while ringide_arv:
        porgandite_koguarv = porgandite_koguarv + ringide_arv
        ringide_arv = ringide_arv - 2
        if ringide_arv == 0:
            print(porgandite_koguarv)
#Added to GitHub on 13th of March, 2021