
import random
import re
import matplotlib as plt

def cree_fichier_alea(nb, nomfichier):
    fichier = nomfichier    
    with open(nomfichier, "w") as fichier: 
        for i in range(nb):       
            nb1= random.random() #nb1 et nb2 =abscisses et ordonées
            nb2= random.random()
            fichier.write(str(nb1) + "\t") 
            fichier.write(str(nb2) + "\n") #Fonction qui écrit les nombres des abscisses et ordonées dans le fichier généré
            
            
    
    print(fichier)

def lit_fichier(nomfic):
    fichier = nomfic
    
    with open("fichiertest.txt", "r") as fichier:
        Cor = fichier.read()
        Cor_2= re.split(r"[\n, \t]", Cor)      #re.split() permet de separer les valeurs en fonctions des espaces ajoutés dans le fichier 
                   
        LX=Cor_2[0::2]
        LY = Cor_2[1::2]                      #Creation des deux listes contenant les coordonées
            
                

    
    with open(nomfic, "w") as fichier:
        
        fichier.write(str(LX)+"\n")
        fichier.write(str(LY))
    print(fichier)
            
    
    

def trace_Nuage(nomf):
    with open("coordonnées.txt", "r") as fichier:
        fichier.read()
    LX= [1,2,3]
    LY = [0,3,6]
    plt.plot(LX, LY, 'o')
    plt.show()





    
    
    


cree_fichier_alea(10, "fichiertest.txt")

lit_fichier("coordonnées.txt")