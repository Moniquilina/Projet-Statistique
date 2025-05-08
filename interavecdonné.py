import tkinter as tk
import random
import Outils
import projet_info

fenetre = tk.Tk()
fenetre.title("Projet Statistique")

# Canevas
canevas = tk.Canvas(fenetre, width=600, height=600, bg='white')
canevas.grid(row=0, column=0, columnspan=3, pady=10)

couleurs = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
couleur_actuelle = 'red'

# Pour stocker nos points (séries X et Y)
pointsX, pointsY = [], []

def effacer_canevas():
    canevas.delete("all")
    canevas.create_line(40, 560, 560, 560)  # axe X
    canevas.create_line(40, 560, 40, 40)    # axe Y

def changer_couleur():
    global couleur_actuelle
    couleur_actuelle = random.choice(couleurs)
    print("Nouvelle couleur =", couleur_actuelle)

def tracer_ligne_de_test():
    """Trace une ligne simple pour tester."""
    canevas.create_line(40, 40, 560, 560, fill=couleur_actuelle, width=3)

def generer_nuage():
    """Génère un nuage de points aléatoires et les affiche."""
    global pointsX, pointsY
    effacer_canevas()
    Outils.cree_fichier_alea(50, "nuage.txt")  # Génère un fichier avec 50 points
    pointsX, pointsY = Outils.lit_fichier("nuage.txt")  # Lit les points depuis le fichier
    for x, y in zip(pointsX, pointsY):
        px = 40 + x * 520
        py = 560 - y * 520
        canevas.create_oval(px-3, py-3, px+3, py+3, fill="green")

def charger_exemple():
    """Charge les points depuis le fichier exemple.txt et les affiche."""
    global pointsX, pointsY
    effacer_canevas()
    pointsX, pointsY = Outils.lit_fichier("exemple.txt")  # Lit les points depuis exemple.txt
    for x, y in zip(pointsX, pointsY):
        px = 40 + x * 520
        py = 560 - y * 520
        canevas.create_oval(px-3, py-3, px+3, py+3, fill="blue")

def calcul_correlation_et_droite():
    """Calcule la corrélation et trace la droite de régression si elle est pertinente."""
    if len(pointsX) < 2:
        print("Pas assez de points pour calculer la corrélation.")
        return
    r = projet_info.correlation(pointsX, pointsY)
    print("Corrélation =", r)
    if projet_info.forteCorrelation(pointsX, pointsY):
        a, b = projet_info.droite_reg(pointsX, pointsY)
        x1, y1 = 0, b
        x2, y2 = 1, a + b
        px1 = 40 + x1 * 520
        py1 = 560 - y1 * 520
        px2 = 40 + x2 * 520
        py2 = 560 - y2 * 520
        canevas.create_line(px1, py1, px2, py2, fill=couleur_actuelle, width=2)
    else:
        print("Corrélation faible, pas de droite tracée.")

# Boutons
btn_tracer = tk.Button(fenetre, text="Tracer la droite", command=tracer_ligne_de_test)
btn_tracer.grid(row=1, column=0, padx=5, pady=5)

btn_autre_couleur = tk.Button(fenetre, text="Autre couleur", command=changer_couleur)
btn_autre_couleur.grid(row=1, column=1, padx=5, pady=5)

btn_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
btn_quitter.grid(row=1, column=2, padx=5, pady=5)

btn_nuage_alea = tk.Button(fenetre, text="Nuage aléatoire (50)", command=generer_nuage)
btn_nuage_alea.grid(row=2, column=0, padx=5, pady=5)

btn_charger_ex = tk.Button(fenetre, text="Charger exemple.txt", command=charger_exemple)
btn_charger_ex.grid(row=2, column=1, padx=5, pady=5)

btn_calcul_droite = tk.Button(fenetre, text="Droite Régression", command=calcul_correlation_et_droite)
btn_calcul_droite.grid(row=2, column=2, padx=5, pady=5)

effacer_canevas()
fenetre.mainloop()