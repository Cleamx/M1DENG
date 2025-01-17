def first_unique_character(mot):
    mot = mot.lower()
    for i in range(len(mot)):
        if mot[i] not in mot[i+1:] and mot[i] not in mot[:i] :
            return (mot[i], i)
    return None

print(first_unique_character('coronavirus'))
print(first_unique_character('Europe'))