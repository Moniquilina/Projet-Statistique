
import random
import re
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
            

    with open(nomfic, "w") as fichier:
        
        fichier.write(str(LX)+"\n")
        fichier.write(str(LY))
    print(fichier)
            

def trace_Nuage(nomf):
    with open("coordonnées.txt", "r") as fichier:
        Cor=fichier.readlines()
        
        
        LX= Cor[0]
        LY= Cor[1]

        LX=re.findall(r'[-+]?[0-9]*\.?[0-9]+', LX)
        LY=re.findall(r'[-+]?[0-9]*\.?[0-9]+', LY)              #re.findall permet d'extraire les nombres de la liste qui était sous forme de chaîne de caractères


        i=0
    
        while i < len(LX):
            LX[i] = float(LX[i])
            #LX[i]= "%.2f" % LX[i]
            i += 1
        
        e=0
        while e < len(LY):
            LY[e] = float(LY[e])
            #LY[e]= "%.2f" % LY[e]
            e += 1
        
    m= float(min(LX))
    ma = float(max(LX))       
    my= float(min(LY))
    may = float(max(LY))        
        

    CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
    x=100
    root = tk.Tk()        
    canva = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    
    canva.create_line(x, CANVAS_HEIGHT - x, CANVAS_WIDTH - x, CANVAS_HEIGHT - x) 
    canva.create_line(x, x, x, CANVAS_HEIGHT - x)

    print(LX, LY)  
    PX=[]
    for j in range(len(LX)):            
        X=((float(LX[j]) - m) / (ma - m))
        CX= x + X * (CANVAS_WIDTH*-2*x)
        PX.append(CX)
    PY=[]
    for z in range(len(LY)):
        
        Y =((float(LY[j]) - my) / (may - my))
        CY= CANVAS_HEIGHT - x - Y *(CANVAS_HEIGHT-2*x)
        PY.append(CY)
    
    
    
    canva.pack()
    root.mainloop()
            
   
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

        X=X[1]
        X= float(X)
        print(X)

        x=0    
        y= a*X + b
    
        
    











    
    
    


cree_fichier_alea(20, "fichiertest.txt")

lit_fichier("coordonnées.txt")
trace_Nuage("graph")
#trace_droite(10,60)