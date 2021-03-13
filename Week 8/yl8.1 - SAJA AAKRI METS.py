#ALLAN KERME // 14.12.2020
#SAJA AAKRI METS
def juurdekasv(pindalaaakrites, aastanejuurdekasv):
    return round(float(pindalaaakrites) * 0.4047 * float(aastanejuurdekasv), 2)
failinimi = str(input("Sisestage failinimi: "))
aastane_juurdekasv = float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: "))
metsasuurusepiir = float(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võetakse: "))
fail = open(failinimi, encoding="UTF-8")
lugeja = 0
suuremadkuipiir = []
for i in fail: # käime kõik read failis läbi
    if float(i) <= metsasuurusepiir: #kui failis on väiksem arv kui metsasuurusepiir siis 
        print("Metsatükki ei võeta arvesse") #väljastab et seda ei võeta arvesse
    else: # aga kui on suurem siis
        suuremadkuipiir.append(i) #paneme need siia listi

for i in suuremadkuipiir:
    print(juurdekasv(suuremadkuipiir[lugeja], aastane_juurdekasv))
    lugeja += 1
print("Arvutati", len(suuremadkuipiir), "metsatüki juurdekasv.")