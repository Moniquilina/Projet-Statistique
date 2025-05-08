import tkinter as tk
import random
import Outils
import projet_info

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Projet Statistique")
fenetre.geometry("900x800")

# Canevas
canevas = tk.Canvas(fenetre, width=800, height=600, bg='white')
canevas.grid(row=0, column=0, columnspan=4, pady=10)

# Liste de couleurs et couleur par défaut
couleurs = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
couleur_actuelle = 'red'

# Données du nuage
pointsX, pointsY = [], []

def changer_couleur():
    global couleur_actuelle
    couleur_actuelle = random.choice(couleurs)
    print("Nouvelle couleur :", couleur_actuelle)

def generer_nuage():
    global pointsX, pointsY
    canevas.delete("all")
    
    # Génère fichier et lit les données
    Outils.cree_fichier_alea(50, "nuage.txt")
    pointsX, pointsY = Outils.lit_fichier("nuage.txt")
    
    for x, y in zip(pointsX, pointsY):
        px = 40 + x * 700
        py = 560 - y * 500
        canevas.create_oval(px-3, py-3, px+3, py+3, fill="black")

def tracer_droite_si_corr_forte():
    if len(pointsX) < 2:
        print("Pas de données à utiliser.")
        return

    r = projet_info.correlation(pointsX, pointsY)
    print("Corrélation :", round(r, 3))
    
    if projet_info.forteCorrelation(pointsX, pointsY):
        a, b = projet_info.droite_reg(pointsX, pointsY)
        # Tracer la droite y = ax + b de x=0 à x=1
        x1, y1 = 0, b
        x2, y2 = 1, a + b
        
        px1 = 40 + x1 * 700
        py1 = 560 - y1 * 500
        px2 = 40 + x2 * 700
        py2 = 560 - y2 * 500
        
        canevas.create_line(px1, py1, px2, py2, fill=couleur_actuelle, width=2)
        print("Droite tracée.")
    else:
        print("Corrélation faible : droite non tracée.")

def quitter():
    fenetre.destroy()

# Boutons
btn_tracer = tk.Button(fenetre, text="Tracer la droite", command=tracer_droite_si_corr_forte)
btn_tracer.grid(row=1, column=0, padx=10, pady=10)

btn_couleur = tk.Button(fenetre, text="Autre couleur", command=changer_couleur)
btn_couleur.grid(row=1, column=1, padx=10, pady=10)

btn_nuage = tk.Button(fenetre, text="Générer nuage", command=generer_nuage)
btn_nuage.grid(row=1, column=2, padx=10, pady=10)

btn_quitter = tk.Button(fenetre, text="Quitter", command=quitter)
btn_quitter.grid(row=1, column=3, padx=10, pady=10)

fenetre.mainloop()
