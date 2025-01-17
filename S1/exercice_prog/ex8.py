def somme_recursive(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return liste[0] + somme_recursive(liste[1:])

liste = [1, 2, 3, 4, 5]
resultat = somme_recursive(liste)
print("La somme de la liste est :", resultat)
