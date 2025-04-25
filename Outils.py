
import random
import re
import matplotlib.pyplot as plt



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
        Cor= re.split(r"[\n, \t]", Cor)      #re.split() permet de separer les valeurs en fonctions des espaces ajoutés dans le fichier 

        i=0
        
        while i < len(Cor)-1:
               Cor[i] = float(Cor[i])
               i += 1
                
        LX=Cor[0::2]
        LX.pop()
        LY = Cor[1::2]                      #Creation des deux listes contenant les coordonées

        print(LX, LY)    
                

    
    with open(nomfic, "w") as fichier:
        
        fichier.write(str(LX)+"\n")
        fichier.write(str(LY))
    print(fichier)
            

def trace_Nuage(nomf):
    with open("coordonnées.txt", "r") as fichier:
        Cor=fichier.readlines()
        print(Cor)
        
        LX= Cor[0]
        LY= Cor[1]

        LX=re.findall(r'[-+]?[0-9]*\.?[0-9]+', LX)
        LY=re.findall(r'[-+]?[0-9]*\.?[0-9]+', LY)
        
          
        print(LX[0], LY)        
        
        
        
           
        
       
    plt.plot(LX,LY,"o")
    
    plt.show()

    with open(nomf, "w") as fichier:
        fichier.write("Nombre de points=")
        fichier.write(str(len(LX)))
        
    print(fichier)

#def trace_droite(a, b):








    
    
    


cree_fichier_alea(5, "fichiertest.txt")

lit_fichier("coordonnées.txt")
trace_Nuage("graph")