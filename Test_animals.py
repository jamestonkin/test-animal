import unittest
from animals import *

class TestAnimalMethods(unittest.TestCase):
    ''' Class to test the animals.py Animal class and methods '''

    @classmethod
    def setUpClass(self):
        ''' Create an instance of an animal and a dog to test those classes '''

        self.name = "Winnie"
        self.species = "Bear"
        self.my_animal = Animal(self.name, self.species)

    def test_animal_name(self):
        ''' Tests if the animal has the correct name and species'''

        self.assertEqual(self.my_animal.name, "Winnie")
        self.assertEqual(self.my_animal.species, "Bear")

    def test_animal_speed(self):
        """ Sets legs to 4 and tests speed at .4 """
        self.legs = 4
        self.my_animal.set_legs(self.legs)
        self.my_animal.walk()

        self.assertEqual(self.my_animal.speed, .4)

    def test_animal_object_is_instance_of_animal(self):
        self.assertIsInstance(self.my_animal, Animal)
