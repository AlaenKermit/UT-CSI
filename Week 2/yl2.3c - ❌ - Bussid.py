#ALLAN KERME // 05.11.2020
#BUSSID - vajab parandusi
inimeste_arv = int(input("Inimeste arv: ")) #Kokku
kohtade_arv = int(input("Kohtade arv: ")) #Bussis
mitu_bussi_vaja_veel = inimeste_arv // kohtade_arv #siiani on veel korras
if inimeste_arv > kohtade_arv: #korras
    print("Vaja busse: ", mitu_bussi_vaja_veel) #nopers mitte enam
    jääk = inimeste_arv % kohtade_arv #siit läheb kõik halvaks
    if inimeste_arv == kohtade_arv * mitu_bussi_vaja_veel: #palun eiiiii
        jääk = kohtade_arv #jääk on jääk
    print("Viimases bussis inimesi:", jääk) #jääk ei ole jääk
else: #trikk
    print("Vaja busse: ", mitu_bussi_vaja_veel) #oii see on väga halb
    jääk = inimeste_arv % kohtade_arv # see ei tohiks niimoodi olla
    print("Viimases bussis inimesi:", jääk) #ei ei ei ei ei einstein