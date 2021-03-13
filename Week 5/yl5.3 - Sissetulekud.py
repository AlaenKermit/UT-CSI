#ALLAN KERME // 03.12.2020
#SISSETULEKUD
fail = open("konto.txt", encoding="UTF-8")
arvud = []
for i in fail:
    if float(i) > 0:
        arvud.append(float(i))
fail.close()
for i in arvud:
    print(i)