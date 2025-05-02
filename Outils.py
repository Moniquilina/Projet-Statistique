
import random
import re
import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
l=40
root= tk.Tk()
canva = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
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
#
        LX=re.findall(r'[-+]?[0-9]*\.?[0-9]+', LX)
        LY=re.findall(r'[-+]?[0-9]*\.?[0-9]+', LY)              #re.findall permet d'extraire les nombres de la liste qui étaient sous forme de chaîne de caractères


        i=0
    
        while i < len(LX):
            LX[i] = float(LX[i])
            i += 1
        
        e=0
        while e < len(LY):
            LY[e] = float(LY[e])
            e += 1
        
    m= min(LX)
    ma = max(LX)       
    my= min(LY)
    may = max(LY)

    canva.create_line(l, CANVAS_HEIGHT - l, CANVAS_WIDTH - l, CANVAS_HEIGHT - l) 
    canva.create_line(l, l, l, CANVAS_HEIGHT - l)  
          
    for x1,y1 in zip(LX,LY):                                                    #conversion des coordonnées dans des pixels
                                             
        px= l+ (x1- m) / (ma - m) * (CANVAS_WIDTH-2*l)
        py = CANVAS_HEIGHT-(l+ (y1 - my) / (may - my) *(CANVAS_HEIGHT-2*l))
        
        
        canva.create_oval(px-3, py-3, px+3, py+3, fill ="green", outline="green")
        
            
   
    with open(nomf, "w") as fichier:
        fichier.write("Nombre de points:")
        fichier.write(str(len(LX)))
            
        
    print(fichier)

    
def trace_droite():
    
    with open("coordonnées.txt", "r") as fichier:
        X=fichier.readlines()
        x=X[0]
        x=re.findall(r'[-+]?[0-9]*\.?[0-9]+', x)
        
        print(x)
        i=random.randint(0,len(x))
        for j in range(len(x)):
            x1=x[i]
        a=20
        b=1
        x1=float(x1)
        y= a*x1+b
                      
        canva = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        px= l+ x1/l* (CANVAS_WIDTH-2*l)
        py = CANVAS_HEIGHT+(l+ y/l *(CANVAS_HEIGHT-2*l))
        print(px, py)
        canva.create_line(px, py, px + CANVAS_WIDTH, py-CANVAS_HEIGHT, fill="black")


cree_fichier_alea(100, "fichiertest.txt")
lit_fichier("coordonnées.txt")
trace_Nuage("points")
trace_droite()

root= tk.Tk()
bouton_droite= tk.Button(root, text ="Tracer droite", command= trace_droite)
bouton_droite.grid(row=3, column=0)
   

canva.grid()
root.mainloop() 
  
