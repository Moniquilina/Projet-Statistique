# Fonction pour calculer la moyenne
def moyenne(serie):
    return sum(serie) / len(serie)

# Fonction pour calculer la variance
def variance(serie):
    m = moyenne(serie)  # Calcul de la moyenne
    somme_carres = sum((i - m) ** 2 for i in serie)  # Somme des écarts au carré
    return somme_carres / len(serie)  # Division par le nombre d'éléments

# Série d'essai
serie = [3, 2, 11]

# Appel des fonctions
print("variance :", variance(serie))
