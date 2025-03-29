
import random

def cree_fichier_alea(nb, nomfichier):
    fichier = nomfichier    
    with open(nomfichier, "w") as fichier: 
        for i in range(nb):       
            nb1= random.random() #nb1 et nb2 =abscisses et ordonées
            nb2= random.random()
            fichier.write(str(nb1) +str(";")) #Fonction qui écrit les nombres des abscisses et ordonées dans le fichier généré
            fichier.write(str(nb2)+ "\n")
        
    
    print(fichier)

def lit_fichier(nomfic):
    fichier = nomfic
    LX= []
    LY =[] 
    with open("fichiertest.txt", "r") as fichier: 
        C =fichier.readlines()        #cela va permettre d'ouvrir le fichier qui contient les coordonnées et de stocker les valeurs
        
        for i in C :
            
            LX.append(C)
            #LY.append(C)

    print(LX)
    
    with open(nomfic, "w") as fichier:
        fichier.write(str(LX))
        fichier.write(str(LY))
    print(fichier)
            
    
    

#def trace_Nuage(nomf):

    
    
    
cree_fichier_alea(5, "fichiertest.txt")

lit_fichier("coordonnées.txt")