import unittest
from zimp.engine import gamestate, item
import os.path
import shutil
import os
import sys


TEST_TMP_DIR = "serialized_data/"


class GameStateTestSerialize(unittest.TestCase):
    """
    Tests the serialization and deserialization capabilities of the GameState.
    """

    def setUp(self):
        """
        Sets up the test case instance.
        """
        self.game_state = gamestate.GameState()

        # clean up temp directory
        if os.path.exists(TEST_TMP_DIR):
            shutil.rmtree(TEST_TMP_DIR)
        os.makedirs(TEST_TMP_DIR)

    def tearDown(self):
        if os.path.exists(TEST_TMP_DIR):
            shutil.rmtree(TEST_TMP_DIR)

    def test_basic(self):
        """
        Tests to make sure that the serialization process can save to file.
        Uses .dat file for checking because of the way shelve works.
        """
        self.assertFalse(os.path.exists(
            TEST_TMP_DIR + sys._getframe().f_code.co_name + ".dat"))
        self.game_state.serialize(
            TEST_TMP_DIR + sys._getframe().f_code.co_name)
        self.assertTrue(os.path.exists(
            TEST_TMP_DIR + sys._getframe().f_code.co_name + ".dat"))

    def test_basic_property(self):
        """
        Tests that a property value can be set.
        """
        self.game_state.has_totem = True
        self.game_state.serialize(
            TEST_TMP_DIR + sys._getframe().f_code.co_name)
        self.game_state = None
        self.assertEqual(self.game_state, None)

        self.game_state = gamestate.GameState.deserialize(
            TEST_TMP_DIR + sys._getframe().f_code.co_name)
        self.assertTrue(self.game_state.has_totem)

    def test_basic_object_property(self):
        """
        Tests that a property object can have its property set.
        """

        # forces creation of a new Item without calling constructor
        self.game_state.item1 = item.Item.__new__(item.Item)

        self.assertNotEqual(self.game_state.item1.name, "My cool item")
        self.game_state.item1.name = "My cool item"

        self.game_state.serialize(TEST_TMP_DIR +
                                  sys._getframe().f_code.co_name)
        self.game_state = None
        self.assertEqual(self.game_state, None)

        self.game_state = gamestate.GameState.deserialize(
            TEST_TMP_DIR + sys._getframe().f_code.co_name)

        self.assertNotEqual(self.game_state.item1, None)
        self.assertEqual(self.game_state.item1.name, "My cool item")
