
import random

def cree_fichier_alea(nb, nomfichier):
    fichier = nomfichier    
    with open(nomfichier, "w") as fichier:
        for i in range (nb):
            nb1= random.random() #nb1 et nb2 =abscisses et ordonées
            nb2= random.random()
            fichier.write(str(nb1)+ "") #Fonction qui écrit les nombres des abscisses et ordonées dans le fichier généré
            fichier.write(str(nb2)+ "\n")
    fichier.readlines()
    print(fichier)

cree_fichier_alea(5, "fichiertest.txt")

def lit_fichier(nomfic):
    fichier = nomfic
    LX= []
    LY = [] 
    with open("files/fichier.txt", "r") as fichier: 
        fichier.readlines()    #cela va permettre d'ouvrir le fichier qui contien les coordonnées et de stocker les valeurs
    with open(nomfic, "w") as fichier_c:
        while fichier == int:
            LX.append(int(fichier))
            fichier_c.write(LX)
    print(fichier_c)

#def trace_Nuage(nomf):

    
    
    
cree_fichier_alea(5, "fichiertest.txt")

#lit_fichier("coordonnées.txt")