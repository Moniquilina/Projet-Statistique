serie = [3,2,10]

def moyenne(serie) :
    moyenne = sum(serie)/len(serie)

    return moyenne

moyenne(serie)

def variance(serie) :
    m = moyenne(serie)
    somme_carres = sum( i - m ** 2 for i in serie) 
    variance = somme_carres/ len(serie) 

    return variance

variance(serie)

def covariance(serieX, serieY) :
    moyenneX = sum(serieX) / len(serieX)  #Calcul de la moyenne de serieX et serieY
    moyenneY = sum(serieY) / len(serieY)
    
    somme_produits = 0
    for i in range(len(serieX)):
        somme_produits += (serieX[i] - moyenneX) * (serieY[i] - moyenneY)  #Calcul de l'ecart de l'element de serieX par rapport à la moyenneX et moynneY
    
    return somme_produits / len(serieX)


def correlation(serieX, serieY):
    varX = variance(serieX)
    varY = variance(serieY)
    cov = covariance(serieX, serieY)
    
    return cov / (varX**0.5 * varY**0.5)