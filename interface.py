import tkinter as tk 
import random
import projet_info
import Outils
import pandas as pd

fenetre = tk.Tk()
fenetre.title("projet stat")
# Je crée le canvas
canevas = tk.Canvas(fenetre, width=800, height=600, bg='white')
canevas.grid(row=0, column=0, columnspan=3, pady=0)
entry = tk.Entry(fenetre)

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
    #Génère un nuage de points aléatoires et les affiche.
    global pointsX, pointsY
    effacer_canevas()
    Outils.cree_fichier_alea(50, "nuage.txt")  # Génère un fichier avec 50 points
    pointsX, pointsY = Outils.lit_fichier("nuage.txt")  # Lit les points depuis le fichier
    for x, y in zip(pointsX, pointsY):
        px = 40 + x * 520
        py = 560 - y * 520
        canevas.create_oval(px-3, py-3, px+3, py+3, fill="green")


def charger_exemple():
    #Charge les points depuis le fichier exemple.txt et les affiche.
    global pointsX, pointsY
    effacer_canevas()
    Outils.cree_fichier_alea(50, "exemple.txt")  # Génère un fichier avec 50 points du fichier
    pointsX, pointsY = Outils.lit_fichier("exemple.txt")  # Lit les points depuis le fichier
    for x, y in zip(pointsX, pointsY):
        px = 40 + x * 520
        py = 560 - y * 520
        canevas.create_oval(px-3, py-3, px+3, py+3, fill="green")

    

def calcul_correlation_et_droite():
    #Calcule la corrélation et trace la droite de régression si elle est pertinente.
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






def extraire_nombre():
    # Lire le fichier ident_virgule.csv et afficher toutes les données
    iden = pd.read_csv("ident_virgule.csv")
    print(iden)

    # Récupérer une valeur spécifique (prénom de l'index 1)
    info = iden.loc[1, 'prenom']
    print(info)

    # Sélectionner une colonne spécifique (tous les noms)
    info = iden.loc[:, 'nom']
    print(info)

    # Récupérer toutes les données de l’index 2
    info = iden.loc[2, :]
    print(info)

    # Sélectionner certaines colonnes et lignes spécifiques
    info=iden.loc[[0,1],['nom','date_naissance']]
    info_villes=pd.read_csv("villes_virgule.csv")
    print(info_villes)
    
    
    # Le programme demande à l'utilisateur la valeur qu'il veut saisir
    nb=entry.get()
    nb =int(nb)
    #Cette fonction permet d'extraire le nombre d'habitants inférieure ou égale à la valeur choisi par l'utilisateur
    nb_hab_10 = info_villes.loc[info_villes["nb_hab_2010"]<=nb, ["nb_hab_2010"]]
    nb_hab_12 = info_villes.loc[info_villes["nb_hab_2012"]<=nb, ["nb_hab_2012"]]
    #.tolist permet de changer le format des données dans une liste pour transformer ces valeurs dans des coordonées
    nb_hab_10 = nb_hab_10["nb_hab_2010"].tolist()
    nb_hab_12 = nb_hab_12["nb_hab_2012"].tolist()
    print(nb_hab_10)
    print(nb_hab_12)
       
    effacer_canevas()    
    for x, y in zip(nb_hab_10, nb_hab_12):
        px = 40 + x * 5
        py = 520 - y * 5
        canevas.create_oval(px-3, py-3, px+3, py+3, fill="green")
    calcul_correlation_et_droite()

def donees_r():
    donnes= pd.read_csv("FD_DEC_2021.csv", sep=";", dtype={"JNAIS": int, "sexe":int}, low_memory = False)
    
    mort= donnes.loc[donnes["JNAIS"]<=30, ["JNAIS"]]
    mort_s= donnes.loc[donnes["sexe"]<=2, ["sexe"]]
    mort=mort["JNAIS"].tolist()
    mort_s = mort_s["sexe"].tolist()
        
    effacer_canevas()   
    
    for x, y in zip(mort, mort_s):
        px = 40 + x*100
        py = 520 - y * 100
        canevas.create_oval(px-3, py-3, px+3, py+3, fill="green")
    

       


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
bouton_quitter.grid(row=4, column=2, pady=10)

bouton_valider= tk.Button(fenetre, text= "Valider", command= extraire_nombre)
bouton_valider.grid(row= 3, column= 1, padx = 5, pady = 5)

bouton_valider= tk.Button(fenetre, text= "donées réeles", command= donees_r)
bouton_valider.grid(row= 3, column= 2, padx = 5, pady = 5)

entry.grid(row= 3, column= 0, padx = 1, pady = 1)

canevas.bind("<Button-1>", ajouter_point)
fenetre.mainloop()

