import unittest
from day02 import follow_basic_commands, follow_advanced_commands

class Test(unittest.TestCase):
    target = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    def test_follow_basic_commands(self):
        expected = 150
        actual = follow_basic_commands(self.target)

        assert expected == actual

    def test_follow_advanced_commands(self):
        expected = 900
        actual = follow_advanced_commands(self.target)

        assert expected == actual
