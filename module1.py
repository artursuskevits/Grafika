from tkinter import *
aken=Tk()
aken.geometry("800x400")
aken.title("Minu esimine aken")
def text_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END)
lbl=Label(aken,text="Решение квадратного уравнения",bg="yellow",fg="#7465b8",font="times_new_roman 20",height=2,width=40)
ent=Entry(aken,fg="blue",bg="lightblue",font="Arial 20", justify=CENTER,width=5)
lbl3=Label(aken,text="x**2+",font="times_new_roman 20",height=2,width=6)
ent2=Entry(aken,fg="blue",bg="lightblue",font="Arial 20", justify=CENTER,width=5)
lbl4=Label(aken,text="x+",font="times_new_roman 20",height=2,width=5)
ent3=Entry(aken,fg="blue",bg="lightblue",font="Arial 20", justify=CENTER,width=5)
lbl5=Label(aken,text="=0",font="times_new_roman 20",height=2,width=5)
btn=Button(aken, text="Vaata resultat",bg="Green", font="Arial 24",relief=RAISED)
lbl2=Label(aken,text="Решение",bg="White",fg="#8465b8",font="times_new_roman 20",height=2,width=40)
lbl.pack()
lbl2.pack(side=BOTTOM)
ent.pack(side=LEFT)
lbl3.pack(side=LEFT)
ent2.pack(side=LEFT)
lbl4.pack(side=LEFT)
ent3.pack(side=LEFT)
lbl5.pack(side=LEFT)
btn.pack(side=LEFT)
aken.mainloop()