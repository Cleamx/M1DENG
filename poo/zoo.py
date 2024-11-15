from abc import ABC, abstractmethod

class Animal(ABC):
    nb_animaux = 0

    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age
        Animal.nb_animaux += 1

    @abstractmethod
    def parler(self):
        print("")

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

class Chien(Animal):
    def __init__(self, nom, age):
        Animal.__init__(self, nom, age)
    
    def parler(self):
        print("Ouaf")

class Chat(Animal):
    def __init__(self, nom, age):
        Animal.__init__(self, nom, age)
    
    def parler(self):
        print("Miaou")

class Lion(Animal):
    def __init__(self, nom, age):
        Animal.__init__(self, nom, age)
    
    def parler(self):
        print("Roaaar")

class Zoo():
    def __init__(self):
        self._animaux = []

    def ajouter_animal(self, animal):
        self._animaux.append(animal)

    def afficher_animaux(self):
        for animal in self._animaux:
            print(f"{animal.nom} ({animal.age} ans) dit :", end=" ")
            animal.parler()

    def nombre_animaux(self):
        return len(self._animaux)


if __name__ == "__main__":
    zoo = Zoo()
    chien = Chien("Milou", 3)
    chat = Chat("Minou", 5)
    lion = Lion("Simba", 2)
    zoo.ajouter_animal(chien)
    zoo.ajouter_animal(chat)
    zoo.ajouter_animal(lion)
    zoo.afficher_animaux()
    print(f"Il y a {zoo.nombre_animaux()} animaux dans le zoo.")