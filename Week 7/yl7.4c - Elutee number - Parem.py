#ALLAN KERME // 11.12.2020
#ELUTEE NUMBER
#argument s on sõne, esialgu see on kuupäev, edasi juba arvutatud arv
def elutee(s):
    #abimuutaja numbri arvutamiseks
    n = 0
    # tsükkel, mis vaatab iga sümboli sõnes
    for i in s:
        if i != "." and i != "":
            n += int(i) # arvutame summat
    # kui saadud arv on väiksem kui 10, siis ongi elutee number käes
    if n < 10:
        return n
    # kui saadud arv on 10 või suurem, siis on vaja uuesti arvutada,
    #selleks kasutame jälle sama funktsiooni
    else:
        return elutee(str(n))
#######################eluteenumberxfailitegemised
#counterelutee = 1
#while counterelutee < 10:
#    fail = open("eluteenumber" + str(counterelutee) + ".txt", "x")
#    counterelutee = counterelutee + 1
#fail.close()
###########nii nüüd kui meil on failid tehtud avame sunnikuupaevad.txt
failsunnikuupaevad = open("sunnikuupaevad.txt", "r")
read = failsunnikuupaevad.read().splitlines()
#cool cool cool cool cool okei nüüd tuleb mmm punktidest lahti saada ja eraldada numbrid ja ja ja liita nad kokku
#for i in read:
#    print(i)