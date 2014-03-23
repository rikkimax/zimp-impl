"""
Coded by Claire.
"""

from zimp.engine.item import *
import unittest


class ItemTest(unittest.TestCase):
    def setUp(self):
        self.test_object = Item(0)

    def test_on_attack(self):
        self.assertEqual(self.test_object.on_attack(), "This is on_attack")

    def test_on_usage(self):
        self.assertEqual(self.test_object.on_usage(), "This is on_usage")

    def test_name(self):
        self.assertEqual(self.test_object.name, "Oil")

    def test_is_weapon(self):
        self.assertEqual(self.test_object.is_weapon, False)

    def test_is_consumable(self):
        self.assertEqual(self.test_object.is_consumable, True)

    def test_attack_value(self):
        self.assertEqual(self.test_object.attack_value, 0)

if __name__ == '__main__':
    unittest.main()
