#Allan Kerme 04/03/2021
#TTL arvestustöö U arvuti(04.03)
#Tormi ülesanne
failinimi = str(input("Sisestage failinimi: ")) # küsib kasutajalt failinime
fail = open(failinimi, encoding = "UTF-8") # avab faili
failisisu = [] # teeb uue tühja listi
# tormi funktsioon mis saab argumendiks tuule kiiruse meetrites sekundis floatina
# teisendab selle kilomeetriteks tunnis (km/h = m/s * 3.6) ning tagastab
# kas tegu on tormiga või mitte
def torm(x):
    kilomeetritekstunnis = x * 3.6
    if kilomeetritekstunnis >= 63:
        global tormidearv
        tormidearv += 1
        print("Kui tuule kiirus on", x, "m/s, siis on torm")
    else:
        print("Kui tuule kiirus on", x, "m/s, siis pole tormi")

# võtab terve failisisu ja paneb need nimekirja ujukomaarvudena
for i in fail:
   failisisu.append(float(i))

fail.close
tormidearv = 0
for i in failisisu:
    torm(i)
print(tormidearv, "mõõtmist näitas tormi.")
#Added to GitHub on 13th of March, 2021