#ALLAN KERME // 10.12.2020
#TELEGRAMM
failinimi = str(input("Sisestage failinimi: "))
fail = open(failinimi, encoding = "UTF-8")
failisisu = fail.read()
asendaesimene = failisisu.replace('Ä','ae')
asendateine = asendaesimene.replace('ä','ae')
asendakolmas = asendateine.replace('Õ', 'oe')
asendaneljas = asendakolmas.replace('õ', 'oe')
asendaviies = asendaneljas.replace('Ö', 'oe')
asendakuues = asendaviies.replace('ö', 'oe')
asendaseitsmes = asendakuues.replace('Ü', 'ue')
asendakaheksas = asendaseitsmes.replace('ü', 'ue')
print(asendakaheksas.upper())