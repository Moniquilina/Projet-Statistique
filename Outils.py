
import random

def cree_fichier_alea(nb, nomfichier):
    fichier= nomfichier
    with open(nomfichier, "w") as fichier:
        for i in range (nb):
            nb1= random.random() #nb1 et nb2 =abscisses et ordonées
            nb2= random.random()
            fichier.write(str(nb1)+"") #Fonction qui écrit les nombres des abscisses et ordonées dans le fichier généré
            fichier.write(str(nb2)+ "\n")
    fichier.readlines()
    print(fichier)

cree_fichier_alea(5, "fichiertest.txt")

def lit_fichier(nomfic):
    fichier_nombres= cree_fichier_alea
    fichier_nombres.read()
    fichier_listes=nomfic
    with open(nomfic, "w") as fichier_listes:
        LX= []
        LY = []
        for i in range (fichier_nombres):
            while ligne:
                print(ligne.strip())
                ligne = fichier_listes.readline()
                
    print(fichier_listes)
lit_fichier("xxx.txt")
        



   



