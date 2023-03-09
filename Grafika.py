from tkinter import *
k=0
k2=0
def klikker(event):
    global k
    k+=1
    btn.configure(text=k)
    if k> 20:
        k+=5
        if k >= 100:
            k=0
            btn2.pack()
            btn2.bind("<Button-1>",klikker3)

def klikker2(event):
    global k
    k-=5
    btn.configure(text=k)

def klikker3(event):
    global k2
    k2+=15
    btn2.configure(text=k2)

def text_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END)

aken=Tk()
aken.geometry("800x400")
aken.title("Minu esimine aken")
lbl=Label(aken,text="kliker",bg="yellow",fg="#7465b8",font="times_new_roman 20",height=2,width=40)
btn=Button(aken, text="Vajuta siia", font="Arial 24",relief=RAISED) #SUNKEN, RAISED, GROOVE
ent=Entry(aken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)

btn2=Button(aken, text=k, font="Arial 24",relief=RAISED)
btn.bind("<Button-1>",klikker)#lkm
btn.bind("<Button-3>",klikker2)#pkm)
ent.bind("<Return>",text_to_lbl)#Enter
lbl.pack()
btn.pack()
ent.pack()
aken.mainloop()
