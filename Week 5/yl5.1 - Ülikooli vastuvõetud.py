#ALLAN KERME // 03.12.2020
#ÜLIKOOLI VASTUVÕETUD
aastaarv = int(input("Palun sisestage, millise aasta andmeid vajate: "))
fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    
    vastuvõetud.append(int(rida))
    
fail.close()

if aastaarv == 2011:
    vastus = vastuvõetud[0]
    print(vastus)
elif aastaarv == 2012:
    vastus = vastuvõetud[1]
    print(vastus)
elif aastaarv == 2013:
    vastus = vastuvõetud[2]
    print(vastus)
elif aastaarv == 2014:
    vastus = vastuvõetud[3]
    print(vastus)
elif aastaarv == 2015:
    vastus = vastuvõetud[4]
    print(vastus)
elif aastaarv == 2016:
    vastus = vastuvõetud[5]
    print(vastus)
elif aastaarv == 2017:
    vastus = vastuvõetud[6]
    print(vastus)
elif aastaarv == 2018:
    vastus = vastuvõetud[7]
    print(vastus)
elif aastaarv == 2019:
    vastus = vastuvõetud[8]
    print(vastus)