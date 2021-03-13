from tkinter import *

raam = Tk()
raam.title("Tiitel")
# loome tahvli laiusega 600px
tahvel = Canvas(raam, width=600)
# üks horisontaalne sirglõik
#tahvel.create_line(50,50,100,50)
 
# horisontaalne sirglõik ja vertikaalne sirglõik
#tahvel.create_line(50,150,100,150,100,200)
 
# sirglõik paksusega 4px
#tahvel.create_line(50,100,100,250, width=4)
 
# rohelist värvi nool paksusega 4px
tahvel.create_line(350,50,350,100, width=4, fill="green", arrow=LAST)
# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()
# siseneme põhitsüklisse
raam.mainloop()