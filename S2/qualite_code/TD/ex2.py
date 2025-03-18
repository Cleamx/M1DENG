import unittest

def somme_pairs(liste):
    somme = 0
    for i in liste:
        if i % 2 == 0:
            somme += i
    return somme

class TestSommePairs(unittest.TestCase):
    def test_somme_pairs(self):
        self.assertEqual(somme_pairs([]), 0)
        self.assertEqual(somme_pairs([1, 2, 3, 4]), 6)
        self.assertEqual(somme_pairs([1, 3, 5]), 0)

unittest.main()