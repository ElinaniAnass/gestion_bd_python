from tkinter import *
from tkinter import ttk
from stagiaire import *
from groupe import *
from tkinter import messagebox

def ajouter():
    x= Stagiaire(a1.get(),a2.get(),a3.get(),cbx.get())
    x.ajouter(x)
    Stagiaire.afficher(table)

def modifier():
    Stagiaire.modifier(a1.get(),a2.get(),a3.get(),cbx.get())
    Stagiaire.afficher(table)

def Supprimer():
    Stagiaire.Supprimer(table)
    Stagiaire.afficher(table)

def rechercher():
    Stagiaire.rechercher(table,a1.get())

def enregistrer():
    Stagiaire.EnregistrerCSV()

def afficher():
    Stagiaire.afficher(table)

win=Tk()
win.geometry("800x480")
win.title('Gérer les étudiants')
win.configure(bg='grey')
win.resizable(False, False)
id=Label(win,text="Id :",bg="grey",font=('Arial', 12)).place(x=200,y=20)
name=Label(win,text="Nom complet :",bg="grey",font=('Arial', 12)).place(x=200,y=50)
email=Label(win,text="Email :",bg="grey",font=('Arial', 12)).place(x=200,y=80)
groupe=Label(win,text="Groupe :",bg="grey",font=('Arial', 12)).place(x=200,y=110)

a1=Entry(win,width=30,font=('Arial', 12))
a1.place(x=400,y=20)
a2=Entry(win,width=30,font=('Arial', 12))
a2.place(x=400,y=50)
a3=Entry(win,width=30,font=('Arial', 12))
a3.place(x=400,y=80)

n = StringVar()
n.set("Selectionner")
cbx = ttk.Combobox(win, width = 30,textvariable=n,font=('Arial', 12))
a=[]
for i in Groupe.lt :
    a.append(i.groupe)
cbx['values']=a
cbx.place(x=400,y=110)

ajouter= ttk.Button(win,command=ajouter,text='Ajouter')
ajouter.place(x=40,y =200 )
afficher= ttk.Button(win,command=afficher,text='Afficher')
afficher.place(x=160,y =200 )
modifer= ttk.Button(win,command=modifier,text='Modifier')
modifer.place(x=280,y =200 )
supprimer= ttk.Button(win,text='Supprimer',command=Supprimer)
supprimer.place(x=400,y =200 )
rechercher= ttk.Button(win,command=rechercher,text='Rechercher')
rechercher.place(x=520,y =200 )
enregistrer= ttk.Button(win,command=enregistrer,text='Enregistrer')
enregistrer.place(x=640,y =200 )

style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', padding=6, relief=' ', background='#ccc', foreground='#000')


ajouter.configure(style='TButton')
afficher.configure(style='TButton')
modifer.configure(style='TButton')
supprimer.configure(style='TButton')
rechercher.configure(style='TButton')
enregistrer.configure(style='TButton')


columns = ("Id", "Name", "Email", "Groupe")
table = ttk.Treeview(win, column=columns, show="headings")
for j in columns:
    table.heading(j, text=j)

table.place(x=0, y=260)


win.mainloop()
