import unittest
from day01 import count_successive_depth_increases, count_successive_3_window_depth_increases

class Test(unittest.TestCase):
    target = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_count_successive_depth_increases(self):
        expected = 7
        actual = count_successive_depth_increases(self.target)

        assert expected == actual

    def test_count_successive_3_window_depth_increases(self):
        expected = 5
        actual = count_successive_3_window_depth_increases(self.target)

        assert expected == actual
