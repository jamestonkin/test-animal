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
        self.my_dog = Dog("Fido")

    def test_animal_name(self):
        ''' Tests if the animal and dog has the correct name and species'''

        self.assertEqual(self.my_animal.name, "Winnie")
        self.assertEqual(self.my_animal.species, "Bear")
        self.assertEqual(self.my_dog.name, "Fido")
        self.assertEqual(self.my_dog.species, "Dog")

    def test_animal_speed(self):
        """ Sets Animal and Dog legs to 4 and tests speed at .4 for Animal and .8 for Dog """

        self.legs = 4
        self.my_animal.set_legs(self.legs)
        self.my_animal.walk()
        self.my_dog.set_legs(self.legs)
        self.my_dog.walk()

        self.assertEqual(self.my_animal.speed, .4)
        self.assertEqual(self.my_dog.speed, .8)

    def test_animal_object_is_instance_of_animal(self):
        """ Tests if animal object is an Animal class and dog object is a Dog class """

        self.assertIsInstance(self.my_animal, Animal)
        self.assertIsInstance(self.my_dog, Dog)
