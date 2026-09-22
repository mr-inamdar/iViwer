from tkinter import *
from PIL import ImageTk,Image,ImageOps
wn = Tk()
wn.title("Image Viwer AAP made by Zeeshan")

lst = []

for i in range(1,11):
    # path = "C:\\Users\\HP\\Pictures\\TK project's pic27\\Tkimg" + str(i) + ".jpg"
    path = f"img/{i}.jpg"
    photo = ImageTk.PhotoImage(ImageOps.expand((Image.open(path)).resize((360,470)),border=5,fill="#FE5BAC"))
    lst.append(photo)

Ef = Canvas(wn,height=2,width=31)
Ef.grid(row=0,column=0,columnspan=3)
label1 = Label(Ef,
    text = "writen by",
    foreground ='#008000',
    background = '#FF0000',
    relief = RAISED,
    bd  =3,
    padx = 2,
    pady = 2,
    font = ("Helvetica",14),
    height=1,width=31//3+2
).grid(row=0,column=1,columnspan=3,sticky = "w")
label2 = Label(Ef,
    text = "Code",
    foreground ='#000000',
    background = '#78E3CA',
    relief = RAISED,
    bd  =3,
    padx = 2,
    pady = 2,
    font = ("Helvetica",14),
    height=1,width=31//3+2
).grid(row=0,column=0,columnspan=3,sticky = "w")
label3 = Label(Ef,
    text = "Zeeshan",
    foreground ='#FFD700',
    background = '#0000FF',
    relief = RAISED,
    bd  =3,
    padx = 2,
    pady = 2,
    font = ("Helvetica",14),
    height=1,width=31//3+2
).grid(row=0,column=2,columnspan=3,sticky = "e")
l = Label(image = lst[0],bg='#AFEEEE',height=590,width=400,relief = RAISED,bd  =5,padx = 17,pady = 17).grid(row=1,column=0,columnspan=3)
def forward(inum):
    global l
    global bf
    global bk
    Ef = Canvas(wn,height=2,width=31).grid(row=0,column=0,columnspan=3)
    label1 = Label(Ef,
        text = "writen by",
        foreground ='#008000',
        background = '#FF0000',
        relief = RAISED,
        bd  =3,
        padx = 2,
        pady = 2,
        font = ("Helvetica",14),
        height=1,width=31//3+2
    ).grid(row=0,column=1,columnspan=3,sticky = "w")
    label2 = Label(Ef,
        text = "Code",
        foreground ='#000000',
        background = '#78E3CA',
        relief = RAISED,
        bd  =3,
        padx = 2,
        pady = 2,
        font = ("Helvetica",14),
        height=1,width=31//3+2
    ).grid(row=0,column=0,columnspan=3,sticky = "w")
    label3 = Label(Ef,
        text = "Zeeshan",
        foreground ='#FFD700',
        background = '#0000FF',
        relief = RAISED,
        bd  =3,
        padx = 2,
        pady = 2,
        font = ("Helvetica",14),
        height=1,width=31//3+2
    ).grid(row=0,column=2,columnspan=3,sticky = "e")
    l = Label(image = lst[inum],bg='#AFEEEE',height=590,width=400,relief = RAISED,bd  =5,padx = 17,pady = 17,).grid(row=1,column=0,columnspan=3)
    bk = Button(wn,text = "<<",bg='#C0C0C0',command=lambda : back(inum-1)).grid(row=2,column=0)
    if inum == len(lst)-1:
        bf = Button(wn,text = ">>",bg='#FFD700',state=DISABLED).grid(row=2,column=2)
    else:
        bf = Button(wn,text = ">>",bg='#C0C0C0',command=lambda: forward(inum+1)).grid(row=2,column=2)
def back(inum):
    global l
    global bf
    global bk 
    Ef = Canvas(wn,height=2,width=31).grid(row=0,column=0,columnspan=3)
    label1 = Label(Ef,
        text = "writen by",
        foreground ='#008000',
        background = '#FF0000',
        relief = RAISED,
        bd  =3,
        padx = 2,
        pady = 2,
        font = ("Helvetica",14),
        height=1,width=31//3+2
    ).grid(row=0,column=1,columnspan=3,sticky = "w")
    label2 = Label(Ef,
        text = "Code",
        foreground ='#000000',
        background = '#78E3CA',
        relief = RAISED,
        bd  =3,
        padx = 2,
        pady = 2,
        font = ("Helvetica",14),
        height=1,width=31//3+2
    ).grid(row=0,column=0,columnspan=3,sticky = "w")
    label3 = Label(Ef,
        text = "Zeeshan",
        foreground ='#FFD700',
        background = '#0000FF',
        relief = RAISED,
        bd  =3,
        padx = 2,
        pady = 2,
        font = ("Helvetica",14),
        height=1,width=31//3+2
    ).grid(row=0,column=2,columnspan=3,sticky = "e") 
    l = Label(image = lst[inum],bg='#AFEEEE',height=590,width=400,relief = RAISED,bd  =5,padx = 17,pady = 17).grid(row=1,column=0,columnspan=3)
    if inum == 0 :
        bk = Button(wn,text = "<<",bg='#FFD700',state=DISABLED).grid(row=2,column=0)
    else:
        bk = Button(wn,text = "<<",bg='#C0C0C0',command=lambda : back(inum-1)).grid(row=2,column=0)
    bf = Button(wn,text = ">>",bg='#C0C0C0',command=lambda: forward(inum+1)).grid(row=2,column=2)
bk = Button(wn,text = "<<",bg='#C0C0C0',command=back(0)).grid(row=2,column=0)
bex = Button(wn,text = "EXIT",command=wn.quit,bg='red').grid(row=2,column=1)
bf = Button(wn,text = ">>",bg='#C0C0C0',command=lambda: forward(1)).grid(row=2,column=2)
wn.mainloop()