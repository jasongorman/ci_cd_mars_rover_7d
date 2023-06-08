import unittest

from src.MarsRover import MarsRover


class TestMoveBack(unittest.TestCase):
    def test_move_backwards(self):
        self.assertEqual(rover.coordinates,[4,7])  # add assertion here


if __name__ == '__main__':
    unittest.main()
