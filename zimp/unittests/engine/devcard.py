"""
Coded by Claire.
"""

from zimp.engine.devcard import *
import unittest


class DevCardTest(unittest.TestCase):
    def setUp(self):
        self.test_object = DevCard(8, 2)

    def test_on_time_action(self):
        self.assertEqual(self.test_object.on_time_action(None),
                         "This is on_time_action")

    def test_text(self):
        self.assertEqual(self.test_object.text, '4 Zombies')

    def test_is_item(self):
        self.assertEqual(self.test_object.is_item, False)

    def test_is_attack(self):
        self.assertEqual(self.test_object.is_attack, True)

    def test_health_adjust(self):
        self.assertEqual(self.test_object.health_adjust, -4)

if __name__ == '__main__':
    unittest.main()
