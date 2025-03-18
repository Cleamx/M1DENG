import unittest

class CompteBancaire:
    def __init__(self, solde_initial):
        self.solde = solde_initial
    
    def deposer(self, montant):
        self.solde += montant
    
    def retirer(self, montant):
        if self.solde - montant > 0:
            self.solde -= montant   
        else :
            self.solde = self.solde
    
    def afficher_solde(self):
        print('solde:', self.solde)

compte = CompteBancaire(100)
compte.retirer(50)
compte.retirer(60)
compte.afficher_solde()

class TestCompteBancaire(unittest.TestCase):
    def test_retrait_suffisant(self):
        compte = CompteBancaire(100)
        compte.retirer(50)
        self.assertEqual(compte.solde, 50)

    def test_retrait_insuffisant(self):
        compte = CompteBancaire(100)
        compte.retirer(150)
        self.assertEqual(compte.solde, 100)

unittest.main()