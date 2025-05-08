import tkinter as tk
import random
import Outils
import projet_info

fenetre = tk.Tk()
fenetre.title("Projet Statistique")

# Définir la taille de la fenêtre
fenetre.geometry("800x600")  # S'assurer que la fenêtre est assez grande

# Canevas
canevas = tk.Canvas(fenetre, width=600, height=400, bg='white')
canevas.grid(row=0, column=0, columnspan=3, pady=10)

couleurs = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
couleur_actuelle = 'red'

# Pour stocker nos points (séries X et Y)
pointsX, pointsY = [], []

def effacer_canevas():
    try:
        canevas.delete("all")
        canevas.create_line(40, 560, 560, 560)  # axe X
        canevas.create_line(40, 560, 40, 40)    # axe Y
    except tk.TclError:
        print("Erreur : le canevas n'existe plus.")

def changer_couleur():
    global couleur_actuelle
    couleur_actuelle = random.choice(couleurs)
    print("Nouvelle couleur =", couleur_actuelle)

def tracer_ligne_de_test():
    try:
        canevas.create_line(40, 40, 560, 560, fill=couleur_actuelle, width=3)
    except tk.TclError:
        print("Erreur : impossible de tracer, canevas détruit.")

def generer_nuage():
    global pointsX, pointsY
    try:
        effacer_canevas()
        Outils.cree_fichier_alea(50, "nuage.txt")
        pointsX, pointsY = Outils.lit_fichier("nuage.txt")
        for x, y in zip(pointsX, pointsY):
            px = 40 + x * 520
            py = 560 - y * 520
            canevas.create_oval(px-3, py-3, px+3, py+3, fill="green")
    except Exception as e:
        print("Erreur lors de la génération du nuage :", e)

def charger_exemple():
    global pointsX, pointsY
    try:
        effacer_canevas()
        pointsX, pointsY = Outils.lit_fichier("exemple.txt")
        for x, y in zip(pointsX, pointsY):
            px = 40 + x * 520
            py = 560 - y * 520
            canevas.create_oval(px-3, py-3, px+3, py+3, fill="blue")
    except Exception as e:
        print("Erreur lors du chargement de l'exemple :", e)

def calcul_correlation_et_droite():
    if len(pointsX) < 2:
        print("Pas assez de points pour calculer la corrélation.")
        return
    try:
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
    except Exception as e:
        print("Erreur lors du calcul de la droite :", e)

# Boutons
btn_trace = tk.Button(fenetre, text="Tracer la ligne test", command=tracer_ligne_de_test)
btn_trace.grid(row=1, column=0, padx=10, pady=10)

btn_autre_couleur = tk.Button(fenetre, text="Autre couleur", command=changer_couleur)
btn_autre_couleur.grid(row=1, column=1, padx=10, pady=10)

btn_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.destroy)
btn_quitter.grid(row=1, column=2, padx=10, pady=10)

btn_nuage_alea = tk.Button(fenetre, text="Nuage aléatoire (50)", command=generer_nuage)
btn_nuage_alea.grid(row=2, column=0, padx=10, pady=10)

btn_charger_ex = tk.Button(fenetre, text="Charger exemple.txt", command=charger_exemple)
btn_charger_ex.grid(row=2, column=1, padx=10, pady=10)

btn_calcul_droite = tk.Button(fenetre, text="Droite Régression", command=calcul_correlation_et_droite)
btn_calcul_droite.grid(row=2, column=2, padx=10, pady=10)

btn_effacer = tk.Button(fenetre, text="Effacer", command=effacer_canevas)
btn_effacer.grid(row=3, column=1, padx=10, pady=10)

effacer_canevas()
fenetre.mainloop()
