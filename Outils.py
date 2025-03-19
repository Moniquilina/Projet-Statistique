
import random

def cree_fichier_alea(nb, nomfichier):
    fichier= nomfichier
    with open(nomfichier, "w") as fichier:
        nb1= random.random()
        nb2= random.random()
        for i in range (nb):            
            fichier.write(str(nb1))
            fichier.write(str(nb2)  + "\n")
    fichier.readlines()
    print(fichier)

cree_fichier_alea(2, "Ok.txt")


    
        
    
  

    

