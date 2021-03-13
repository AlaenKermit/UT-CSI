#ALLAN KERME // 03.12.2020
#LIIKLUSMÄRK
from tkinter import *
top = Tk()
top.title = ("Mingi liiklusmärk")
w = Canvas(width=600, height=600, bg='white')
###KÕIK TULEB SIIA ALLA
#w.create_rectangle(1,0,1205,225, fill='cyan', width=0)
#w.create_rectangle(1,225,1205,275, fill='yellow', width=0)
w.create_polygon(0,600,600,600,300,0, fill="white", outline="red", width=25)
w.create_polygon(250,150,350,150,300,50, fill="black", outline="black", width=0)
w.create_rectangle(250,150,350,550, fill='black', width=0)
w.create_rectangle(350,350,420,400, fill='black', width=0)
### SIIT EDASI EI PANE ENAM MIDAGI
w.pack()
top.mainloop()
#Added to GitHub on 13th of March, 2021