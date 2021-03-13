#ALLAN KERME // 10.12.2020
#KALKULAATOR
from easygui import *
tehted = ["+","-","*"]
arv1 = integerbox("Palun sisestage ESIMENE täisarv lõigus 1-10", lowerbound = 1, upperbound = 10)
arv2 = integerbox("Palun sisestage TEINE täisarv 1-10", lowerbound = 1, upperbound = 10)
tehevalik = buttonbox("Valige tehe:", choices = tehted)
if tehevalik == "+":
    summa = arv1 + arv2
elif tehevalik == "-":
    summa = arv1 - arv2
elif tehevalik == "*":
    summa = arv1 * arv2
msgbox(summa)
#Added to GitHub on 13th of March, 2021