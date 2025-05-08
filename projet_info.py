

def moyenne(serie) :
    moyenne = sum(serie)/len(serie)

    return moyenne



def variance(serie) :

    m = moyenne(serie)
    somme_carres = sum((i - m) ** 2 for i in serie) 
    variance = somme_carres/ len(serie) 

    return variance


def covariance(serieX, serieY) :
    moyX = moyenne(serieX)  # Calcul de la moyenne de serieX et serieY
    moyY = moyenne(serieY)
    
    somme_produits = 0
    for i in range(len(serieX)):
        somme_produits += (serieX[i] - moyX) * (serieY[i] - moyY)  # Calcul de l'ecart de l'element de serieX 
    return somme_produits / len(serieX)                            # par rapport à la moyenne de X et la moyenne deY
    
    

def correlation(serieX, serieY):
    varX = variance(serieX)
    varY = variance(serieY)
    covXY = covariance(serieX, serieY)
    
    return covXY / (varX**0.5 * varY**0.5)


def forteCorrelation(serieX, serieY) :
    coef_corr = correlation(serieX, serieY)
    if coef_corr > 0.8 or coef_corr < 0.8 :    # On évalue si le coefficient est proche de 1 ou -1
        return True
    
    else:
        return False

def droite_reg(serieX, serieY) :
    moyX = moyenne(serieX)             
    moyY = moyenne(serieY)             
    covXY = covariance(serieX, serieY)  
    varX = variance(serieX)            
    
    # Calcul du coefficient directeur (a) et de l'ordonnée à l'origine (b)
    coeff_dir = covXY / varX
    ord_orig = moyY - coeff_dir * moyX

    return (coeff_dir, ord_orig)