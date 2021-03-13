#ALLAN KERME // 05.11.2020
#ISTEKOHT
from random import randint #impordib random funktsiooni mooduli asja
main_questionne = input("Kas soovite istekohta ise valida (""ise"")"" või loosida (""loos"")""? ") #küsib kasutajalt
if main_questionne == "ise": #kui kasutaja valib "ise" siis
    asukoht = input("Kas soovite istuda akna ääres (""aken"")"" või mitte (""muu"")""? ") #küsib seda
    if asukoht == "aken": #kui kasutaja on valinud aken siis
        print("Valisite ise. Aknakoht") #väljund
    elif asukoht == "muu": #kui kasutaja on valinud muu siis
        print("Valisite ise. Vahekäigukoht") #muu
    else: #muidu
        print("Vigane sisend") #trikk!!!
elif main_questionne == "loos": #kui kasutaja valis loosi siis
    loosinumber = randint(1,3) # suvaline number
    if loosinumber == 1: #kui üks siis
        print("Istekoht loositi. Akna juures")
    else: #muidu
        print("Istekoht loositi. Vahekäigukoht")
else: #trikk
    print("Vigane sisend")
#Added to GitHub on 13th of March, 2021