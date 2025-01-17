liste =  [0, 3, 6, 1, 2, 4, 5]

def triplet_pythagoricien(liste):
    for i in range(len(liste)):
        for j in range(i+1, len(liste)):
            for k in range(j+1, len(liste)):
                if liste[i]**2 + liste[j]**2 == liste[k]**2:
                    return liste[i], liste[j], liste[k]
    return None

print(triplet_pythagoricien(liste))