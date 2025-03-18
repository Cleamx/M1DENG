def somme_des_chiffres(a, b):
    if a <= b :
        somme = 0
        for i in range(a, b+1):
            str_i = str(i)
            somme = somme + int(str_i[0]) + int(str_i[1])
        return somme

    else:
        print("a doit être inférieur ou égal à b")

print(somme_des_chiffres(10, 30))
