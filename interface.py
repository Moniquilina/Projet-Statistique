import tkinter as tk 
import random
import projet_info
import Outils

fenetre = tk.Tk()
fenetre.title("projet stat")
# Je crée le canvas
canevas = tk.Canvas(fenetre, width=800, height=800, bg='white')
canevas.grid(row=0, column=0, columnspan=3, pady=0)

couleurs = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']  # Liste des couleurs disponibles
couleur_actuelle = 'red'

# Initialisation des points (variables globales)
pointsX = []
pointsY = []

def changer_couleur():  # Définir la fonction pour le changement de couleur 
    global couleur_actuelle
    couleur_actuelle = random.choice(couleurs)

def effacer_canevas():
    canevas.delete("all")

def tracer_ligne():  # Fonction pour tracer une ligne
    canevas.create_line(10, 10, 200, 800, fill=couleur_actuelle, width=3)

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
    Outils.cree_fichier_alea(50, "exemple.txt")  # Génère un fichier avec 50 points du fichier
    pointsX, pointsY = Outils.lit_fichier("exemple.txt")  # Lit les points depuis le fichier
    for x, y in zip(pointsX, pointsY):
        px = 40 + x * 520
        py = 560 - y * 520
        canevas.create_oval(px-3, py-3, px+3, py+3, fill="green")

    

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

def activer_dessin():
    global dessiner_mode
    dessiner_mode = True
    print("Mode dessin active")  #amelioration mais c est bien de savoir

def desactiver_dessin():
    global dessiner_mode
    dessiner_mode = False
    print("Mode dessin desactive")#pareil

def ajouter_point(event):
    if dessiner_mode:
        x = (event.x - 40) / 520  # Calcul de la coordonnée X
        y = (560 - event.y) / 520  # Calcul de la coordonnée Y
        pointsX.append(x)
        pointsY.append(y)
        canevas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="blue")

# Création des boutons
bouton_nuage = tk.Button(fenetre, text="Nuage Aléatoire", command=generer_nuage)
bouton_nuage.grid(row=1, column=0, padx=5, pady=5)

bouton_exemple = tk.Button(fenetre, text="Charger Exemple", command=charger_exemple)
bouton_exemple.grid(row=1, column=1, padx=5, pady=5)

bouton_couleur = tk.Button(fenetre, text="Autre Couleur", command=changer_couleur)
bouton_couleur.grid(row=1, column=2, padx=5, pady=5)

# --- Boutons ligne 2 ---
bouton_tracer = tk.Button(fenetre, text="Tracer la droite", command=calcul_correlation_et_droite)
bouton_tracer.grid(row=2, column=0, padx=5, pady=5)

bouton_dessin_on = tk.Button(fenetre, text="Activer Dessin", command=activer_dessin)
bouton_dessin_on.grid(row=2, column=1, padx=5, pady=5)

bouton_dessin_off = tk.Button(fenetre, text="Désactiver Dessin", command=desactiver_dessin)
bouton_dessin_off.grid(row=2, column=2, padx=5, pady=5)

# --- Bouton ligne 3 ---
bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.grid(row=3, column=1, pady=10)


canevas.bind("<Button-1>", ajouter_point)
fenetre.mainloop()

