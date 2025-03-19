
import random

def cree_fichier_alea(nb, nomfichier):
    fichier= nomfichier
    with open(nomfichier, "w") as fichier:
        for i in range (nb):
            nb1= random.random()
            nb2= random.random()
            fichier.write(str(nb1)+"")
            fichier.write(str(nb2)+ "\n")
    fichier.readlines()
    print(fichier)

cree_fichier_alea(2, "fichiertest.txt")

def lit_fichier(nomfic):
    fichier2=nomfic
    with open(nomfic, "w") as fichier:


