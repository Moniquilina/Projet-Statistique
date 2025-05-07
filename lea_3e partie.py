import pandas as pd

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
print(info)
def extraire_nombres():
    # Lire le fichier villes_virgule.csv et afficher toutes les données
    info_villes=pd.read_csv("villes_virgule.csv")
    print(info_villes)
    # Le programme demande à l'utilisateur la valeur qu'il veut saisir
    nb=int(input("<= à combien?"))
    #Cette fonction permet d'extraire le nombre d'habitants inférieure ou égale à la valeur choisi par l'utilisateur
    nb_hab = info_villes.loc[info_villes["nb_hab_2010"]<=nb, ["nb_hab_2010","nb_hab_2012"] ]
    print(nb_hab)

extraire_nombres()