import unittest

def transformation(chaine):
    resultat = ''

    for i, char in enumerate(chaine):
        if i % 2 == 0:
            resultat += char.upper()
        else:
            resultat += char.lower()
    
    return resultat

class TestTransformation(unittest.TestCase):
    def test_transformation(self):
        self.assertEqual(transformation('bonjour'), 'BoNjOuR')
        self.assertEqual(transformation('BONJOUR'), 'BoNjOuR')

unittest.main()