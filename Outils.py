import random
import re
import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
l = 40

root = tk.Tk()
canva = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canva.grid(row=0, column=0, columnspan=3)

def cree_fichier_alea(nb, nomfichier):
    """Crée un fichier avec nb points aléatoires."""
    with open(nomfichier, "w") as fichier:
        for i in range(nb):
            nb1 = random.random()  # abscisses
            nb2 = random.random()  # ordonnées
            fichier.write(str(nb1) + "\t" + str(nb2) + "\n")

def lit_fichier(nomfic):
    """Lit un fichier et retourne les coordonnées X et Y."""
    with open(nomfic, "r") as fichier:
        lines = fichier.readlines()
    LX = []
    LY = []
    for line in lines:
        x, y = map(float, line.split())
        LX.append(x)
        LY.append(y)
    return LX, LY

def trace_Nuage(nomf):
    """Affiche un nuage de points à partir d'un fichier."""
    LX, LY = lit_fichier(nomf)
    m = min(LX)
    ma = max(LX)
    my = min(LY)
    may = max(LY)

    # Tracer les axes
    canva.create_line(l, CANVAS_HEIGHT - l, CANVAS_WIDTH - l, CANVAS_HEIGHT - l) 
    canva.create_line(l, l, l, CANVAS_HEIGHT - l)

    # Tracer les points
    for x1, y1 in zip(LX, LY):
        px = l + (x1 - m) / (ma - m) * (CANVAS_WIDTH - 2 * l)
        py = CANVAS_HEIGHT - (l + (y1 - my) / (may - my) * (CANVAS_HEIGHT - 2 * l))
        canva.create_oval(px - 3, py - 3, px + 3, py + 3, fill="green", outline="green")

def trace_droite(a, b):
    """Trace une droite y = ax + b."""
    x1 = 0
    y1 = a * x1 + b
    x2 = 1
    y2 = a * x2 + b

    px1 = l + x1 * (CANVAS_WIDTH - 2 * l)
    py1 = CANVAS_HEIGHT - (l + y1 * (CANVAS_HEIGHT - 2 * l))
    px2 = l + x2 * (CANVAS_WIDTH - 2 * l)
    py2 = CANVAS_HEIGHT - (l + y2 * (CANVAS_HEIGHT - 2 * l))

    canva.create_line(px1, py1, px2, py2, fill="black", width=2)

# Création des boutons
def on_bouton_tracer_droite():
    """Fonction pour tracer la droite."""
    trace_droite(10, 2)

def on_bouton_nuage():
    """Fonction pour tracer le nuage de points."""
    trace_Nuage()

# Boutons pour l'interface graphique
bouton_nuage = tk.Button(root, text="Nuage Aléatoire", command=on_bouton_nuage)
bouton_nuage.grid(row=1, column=0, padx=5, pady=10)

bouton_tracer = tk.Button(root, text="Tracer la droite", command=on_bouton_tracer_droite)
bouton_tracer.grid(row=1, column=1, padx=5, pady=10)

# Lancement de la génération de points aléatoires
cree_fichier_alea(100, "fichiertest.txt")

root.mainloop()

