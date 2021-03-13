#ALLAN KERME // 26.11.2020
#EESTI HALDUSÜKSUSE LIPP - RAKVERE
from tkinter import *
top = Tk()
top.title = ("Mingi lipp")
w = Canvas(width=1200, height=500, bg='white')
###KÕIK TULEB SIIA ALLA
w.create_rectangle(1,0,1205,225, fill='cyan', width=0)
w.create_rectangle(1,225,1205,275, fill='yellow', width=0)
w.create_rectangle(1,275,1205,500, fill='cyan', width=0)
### SIIT EDASI EI PANE ENAM MIDAGI
w.pack()
top.mainloop()