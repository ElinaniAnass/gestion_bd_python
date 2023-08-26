import mysql.connector as mysql
db = mysql.connect(host = "localhost",database = "etudiants",user = "root",password = "")
cursor = db.cursor()

import csv
from tkinter import messagebox
class Stagiaire :
    def __init__(self,id,name,emai,groupe):
        self._id=id
        self._name = name
        self._emai = emai
        if groupe =="Selectionner" :
            self._groupe = "Groupe non séléctioné"
        else:
            self._groupe = groupe

    def setName(self,new):
        self._name = new

    def setEmail(self,new):
        self._emai = new

    def setGroupe(self,new):
        self._groupe = new

    def ajouter(self,obj):
        if obj._id == '' or  obj._name == '' or obj._emai == '' or obj._groupe == '' :
            messagebox.showwarning("Avertissement", "Tous les champs sont obligatoires.")
        else :
            cursor.execute("INSERT INTO stagiaire(id,name,email,groupe) VALUES(%s,%s,%s,%s)",
                           (obj._id, obj._name, obj._emai, obj._groupe))
            db.commit()
            messagebox.showinfo("Succes", "Stagiaire ajouté avec succé")


    @classmethod
    def afficher(cls, table):
        table.delete(*table.get_children())
        cursor.execute(f'SELECT * FROM stagiaire')
        etu = cursor.fetchall()
        for i in etu:
            table.insert('', "end", values=i)




    @classmethod
    def supprimer(cls, id):
        with open('stagiaire.csv', 'r+') as file:
            reader = csv.reader(file, delimiter=";")
            l = []
            for i in reader :
                l.append(i)
            for i in l :
                if i[0] == str(id):
                    l.remove(i)
        with open("stagiaire.csv", "w+", newline="") as f:
            file = csv.writer(f, delimiter=";")
            for i in l:
                file.writerow([i[0], i[1], i[2], i[3]])




    @classmethod
    def EnregistrerCSV(cls):
        with open("stagiaire.csv", "w+", newline="") as f:
            file = csv.writer(f, delimiter=";")
            cursor.execute(f'SELECT * FROM stagiaire')
            etu = cursor.fetchall()
            for i in etu:
                file.writerow([i[0], i[1], i[2], i[3]])
        messagebox.showinfo("Succes", "Données Enregistrés")
    @classmethod
    def rechercher(cls, table, id):
        table.delete(*table.get_children())
        found = False
        if id == '':
            messagebox.showwarning("Avertissement", "Svp remplir l'Id.")
        else:
            cursor.execute(f'SELECT * FROM stagiaire')
            etu = cursor.fetchall()
            for i in etu:
                if i[0] == int(id):
                    table.insert('', "end", values=(i[0], i[1], i[2], i[3]))
                    return messagebox.showinfo("Succes", "Stagiaire trouvé.")

            return messagebox.showwarning("Avertissement", "Stagiaire non trouvé.")


    @classmethod
    def modifier(cls, id,name,emai,groupe):
        if id == '' or  name == '' or emai == '' or groupe == '' :
            messagebox.showwarning("Avertissement", "Tous les champs sont obligatoires.")
        else :
            cursor.execute(f'SELECT id FROM stagiaire')
            etu = cursor.fetchall()
            for i in etu :
                if i[0] == int(id) :
                    cursor.execute(f'UPDATE stagiaire SET name = %s, email = %s , groupe = %s  WHERE id = %s',
                                   (name, emai, groupe, id))
                    return messagebox.showinfo("Succes", "Stagiaire modifié avec succé.")

            return messagebox.showwarning("Avertissement", "Stagiaire non trouvé.")






    @classmethod
    def Supprimer(cls,table):
        it = table.item(table.selection())
        value=it['values'][0]
        print(value)
        cursor.execute('DELETE FROM stagiaire WHERE id = %s', (value,))
        db.commit()
        messagebox.showinfo("Succes", "Stagiaire supprimé avec succé.")




