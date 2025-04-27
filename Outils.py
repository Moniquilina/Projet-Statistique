
import random
import re
import matplotlib.pyplot as plt
import tkinter as tk



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

        LX= sorted(LX)
        LY= sorted(LY)
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
        LY=re.findall(r'[-+]?[0-9]*\.?[0-9]+', LY)              #re.findall permet d'extraire les nombres de la liste qui était sous forme de chaîne de caractères

    print(LX)
    i=0
    
    while i < len(LX):
        LX[i] = float(LX[i])
        LX[i]= "%.2f" % LX[i]
        i += 1
    
    e=0
    while e < len(LY):
        LY[e] = float(LY[e])
        LY[e]= "%.2f" % LY[e]
        e += 1
   
    
    plt.plot(LX, LY,"o")                                        #la fonction plt permet de générer le graphique
    plt. grid(True)
    plt.show()

    with open(nomf, "w") as fichier:
        fichier.write("Nombre de points:")
        fichier.write(str(len(LX)))
        
    print(fichier)

def trace_droite(a, b):
    with open("coordonnées.txt", "r") as fichier:
        X=fichier.readlines()
        X= X[0]
        print(X)
        X=re.findall(r'[-+]?[0-9]*\.?[0-9]+', X)
        
        i=0    
        while i < len(X):
            X[i] = float(X[i])
            i += 1
        print(X)
        
        j = random.randint(0,100)
        for j in range(len(X)):
            X= X[j]
            
            y= a*x + b
    plt.plot(x, y)
    plt.show()
        
        
    











    
    
    


cree_fichier_alea(20, "fichiertest.txt")

lit_fichier("coordonnées.txt")
trace_Nuage("graph")
trace_droite(5,6)