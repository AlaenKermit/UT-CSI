#ALLAN KERME // 05.11.2020
#SPÄMM
kirja_suurus = float(input("Sisestage kirja suurus: "))
kirja_teema = input("Sisestage kirja teema pealkiri: ")
fail = input("Kas kirjaga on kaasas fail? ")
if kirja_suurus > 1 and fail == "jah":
    print("Kiri on spämm")
elif kirja_teema == "":
    print("Kiri on spämm")
    #elif fail == "jah":
    #    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")
#Added to GitHub on 13th of March, 2021