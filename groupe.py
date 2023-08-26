import csv
class Groupe :
    lt=[]
    def __init__(self,id,groupe):
        self._id=id
        self.groupe=groupe

    def ajouter(self,obj):
        Groupe.lt.append(obj)

    def affich_gr(self):
        for i in Groupe.lt:
            print()

g1 = Groupe('1','DEV102')
g1.ajouter(g1)
g1.ajouter(Groupe('2','DEV107'))
g1.ajouter(Groupe('3','DEV109'))


