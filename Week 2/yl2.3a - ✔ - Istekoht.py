#ALLAN KERME // 05.11.2020
#PULSS
vanus = int(input("Sisestage enda vanus: ")) #küsib kasutajalt vanust
sugu = str(input("Sisestage enda sugu: ")) #küsib kasutaja sugu
print("Treeningu tüübid: 1 - tervisetreening; 2 - põhivastupidavuse treening; 3 - intensiivne aeroobne treening")
t_tüüp = int(input("Sisestage treeningu tüüp: ")) #küsib treeningu tüübi

#mehed
if sugu == 'M' or sugu == 'm': #kui sugu on MEES siis
    maksimaalne_pulsisagedus = 220 - vanus # maksimaalne pulsisageduse arvutus
    if t_tüüp == 1: #TERVISETREENING
        alumine_piir = maksimaalne_pulsisagedus * 0.50 #arvutab alumise piiri
        ülemine_piir = maksimaalne_pulsisagedus * 0.70 #arvutab ülemise piiri
        al = round(alumine_piir) #ümardab
        ül = round(ülemine_piir) #ümardab
        print("Pulsisagedus peaks olema vahemikus", int(al),  "kuni", int(ül)) #väljendab
    elif t_tüüp == 2: #PÕHIVASTUPIDAVUSE TREENING
        alumine_piir = maksimaalne_pulsisagedus * 0.70
        ülemine_piir = maksimaalne_pulsisagedus * 0.80
        al = round(alumine_piir)
        ül = round(ülemine_piir)
        print("Pulsisagedus peaks olema vahemikus", int(al),  "kuni", int(ül)) #väljendab
    elif t_tüüp == 3: #INTENSIIVNE AEROOBNE TREENING
        alumine_piir = maksimaalne_pulsisagedus * 0.80
        ülemine_piir = maksimaalne_pulsisagedus * 0.87
        al = round(alumine_piir)
        ül = round(ülemine_piir)
        print("Pulsisagedus peaks olema vahemikus", int(al),  "kuni", int(ül)) #väljendab

#naised
elif sugu == 'N' or sugu == 'n':
    maksimaalne_pulsisageduse_arvutus1 = vanus * 0.88
    maksimaalne_pulsisagedus = 206 - maksimaalne_pulsisageduse_arvutus1
    int(maksimaalne_pulsisagedus)
    #type(maksimaalne_pulsisagedus)
    #print(maksimaalne_pulsisagedus)
    if t_tüüp == 1: #TERVISETREENING
        alumine_piir = maksimaalne_pulsisagedus * 0.50
        ülemine_piir = maksimaalne_pulsisagedus * 0.70
        al = round(alumine_piir)
        ül = round(ülemine_piir)
        print("Pulsisagedus peaks olema vahemikus", int(al),  "kuni", int(ül)) #väljendab
    elif t_tüüp == 2: #PÕHIVASTUPIDAVUSE TREENING
        alumine_piir = maksimaalne_pulsisagedus * 0.70
        ülemine_piir = maksimaalne_pulsisagedus * 0.80
        al = round(alumine_piir)
        ül = round(ülemine_piir)
        print("Pulsisagedus peaks olema vahemikus", int(al),  "kuni", int(ül)) #väljendab
    elif t_tüüp == 3: #INTENSIIVNE AEROOBNE TREENING
        alumine_piir = maksimaalne_pulsisagedus * 0.80
        ülemine_piir = maksimaalne_pulsisagedus * 0.87
        al = round(alumine_piir)
        ül = round(ülemine_piir)
        print("Pulsisagedus peaks olema vahemikus", int(al),  "kuni", int(ül)) #väljendab
#Added to GitHub on 13th of March, 2021