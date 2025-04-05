
import random

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
    LX= []
    LY =[]
    with open("fichiertest.txt", "r") as fichier:
        Cor = fichier.read().split("\t")
        #C =Cor.split(", ")      #cela va permettre d'ouvrir le fichier qui contient les coordonnées et de stocker les valeurs dans une liste
        print(Cor)
        for i in Cor :            
                            
            LX.append(Cor)
            #LY.append(C[1])

    print(LX, LY)
    
    with open(nomfic, "w") as fichier:
        
        fichier.write(str(LX))
        #fichier.write(str(LY))
    print(fichier)
            
    
    

def trace_Nuage(nomf):
    with open("coordonnées.txt", "r") as fichier:

    
    
    
cree_fichier_alea(5, "fichiertest.txt")

lit_fichier("coordonnées.txt")