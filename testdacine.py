
import random

def cree_fichier_alea(nb, nomfichier):
    with open("fichiertest.txt", "w") as fichier:
        nb1= random.random()
        nb2= random.random()
        for i in range (nb):
            fichier.write(nb1)
    print(fichier)
cree_fichier_alea(1, "n")

    
        
    
  

    

