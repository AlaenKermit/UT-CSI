#ALLAN KERME // 03.12.2020
#ÜLIKOOLI VASTUVÕETUD
hetkeneaasta = int(input("Palun sisestage, milline aasta on hetkel: "))
aastaarv = int(input("Palun sisestage, millise aasta andmeid vajate: "))
fail = open("rebased.txt", encoding="UTF-8")
number = hetkeneaasta - aastaarv
vastuvõetud = []
tulemus = 0


for rida in fail:
    
    if number > 2010:
        tulemus = number - 2011
    
    vastuvõetud.append(int(rida))
    
    if tulemus >= 0:
        print(vastuvõetud[tulemus])
    
fail.close()
#muuta midagi
#if aastaarv == 2011:
#    vastus = vastuvõetud[0]
#    print(vastus)
#elif aastaarv == 2012:
#    vastus = vastuvõetud[1]
#    print(vastus)
#elif aastaarv == 2013:
#    vastus = vastuvõetud[2]
#    print(vastus)
#elif aastaarv == 2014:
#    vastus = vastuvõetud[3]
#    print(vastus)
#elif aastaarv == 2015:
#    vastus = vastuvõetud[4]
#    print(vastus)
#elif aastaarv == 2016:
#    vastus = vastuvõetud[5]
#    print(vastus)
#elif aastaarv == 2017:
#    vastus = vastuvõetud[6]
#    print(vastus)
#elif aastaarv == 2018:
#    vastus = vastuvõetud[7]
#    print(vastus)
#elif aastaarv == 2019:
#    vastus = vastuvõetud[8]
#    print(vastus)