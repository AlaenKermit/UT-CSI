#ALLAN KERME // 03.12.2020
#JÄNESEVANEMATE MURE VER.3
ringide_arv = int(input("sisestage ringide arv: "))
porgandite_koguarv = 0
#asi1 = ringide_arv - 2
tomat = []

if ringide_arv % 2 == 0:
    for i in range(ringide_arv, 0, -2):
        porgandite_koguarv = porgandite_koguarv+i
    print(porgandite_koguarv)
    
if ringide_arv % 2 != 0:
    ringide_arv = ringide_arv - 1
    for i in range(ringide_arv, 0, -2):
        porgandite_koguarv = porgandite_koguarv+i
    print(porgandite_koguarv)





#for ringide_arv in range(2,asi1):
#    ringide_arv = ringide_arv - 1
#    porgandite_koguarv = porgandite_koguarv + ringide_arv
#    print(porgandite_koguarv)

