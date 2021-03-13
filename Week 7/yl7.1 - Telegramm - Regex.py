#ALLAN KERME // 10.12.2020
#TELEGRAMM - REGEX
import re
failinimi = str(input("Sisestage failinimi: "))
fail = open(failinimi, encoding = "UTF-8")
failisisu = fail.read()
asendaesimene = re.sub('Ä' and 'ä', 'ae', failisisu)
asendateine = re.sub('Õ' and 'õ', 'oe', asendaesimene)
asendakolmas = re.sub('Ö' and 'ö', 'oe', asendateine)
asendaneljas = re.sub('Ü' and 'ü', 'ue', asendakolmas)
print(asendaneljas.upper())