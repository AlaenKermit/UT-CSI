#ALLAN KERME // 03.12.2020
#MALELAUD
from tkinter import *
vahe = 50
#küsimus1_laud = int(input("Kas soovite laadida malelaua"))
top = Tk()
top.title = ("Mingi liiklusmärk")
w = Canvas(width=1300, height=700, bg='white')
###KÕIK TULEB SIIA ALLA
i = 10
while i <= 80:
    j = 0
    while j <= 80:
        print("i = " + str(i) + ", j = " + str(j))
        w.create_rectangle(j,i,j,i)
        j += 10
    i += 10
w.create_rectangle(i,j,i,j)
#w.create_rectangle(1,0,1205,225, fill='cyan', width=0)
#w.create_rectangle(1,225,1205,275, fill='yellow', width=0)
#w.create_polygon(0,600,600,600,300,0, fill="white", outline="red", width=25)
#w.create_rectangle(350,350,420,400, fill='black', width=0)
#w.create_rectangle(450,345,878,522, fill='yellow3', width=0) # peamine keha
#w.create_polygon(431,345,467,254,854,254,894,345, fill="black", outline="black", width=0) # katus
#w.create_polygon(754,322,754,282,793,252,831,282,831,322, fill="gold", outline="black", width=0) # katuse ülemine parempoolne akna framekatuseosa
#w.create_rectangle(760,328,878,522, fill='brown', width=0) # ülemine parempoolne aknaraam
#w.create_polygon(500,322,500,282,539,252,577,282,577,322, fill="gold", outline="black", width=0) # katuse ülemine vasakpoolne akna framekatuseosa
#w.create_rectangle(450,345,878,522, fill='brown', width=0) # ülemine vasakpoolne aknaraam
#w.create_rectangle(631,421,691,522, fill='brown', width=0) # UKS
### SIIT EDASI EI PANE ENAM MIDAGI
w.pack()
top.mainloop()
#Added to GitHub on 13th of March, 2021