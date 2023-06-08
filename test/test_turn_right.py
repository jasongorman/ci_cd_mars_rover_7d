import unittest

from src.MarsRover import MarsRover
from parameterized import parameterized


class rightturn(unittest.TestCase):

    @parameterized.expand([('N', 'E'), ('E', 'S'), ('S', 'W'), ('W', 'N')])
    def test_turn_right(self, start, end):
        rover = MarsRover([4, 7], start)
        rover.rotate_right()
        self.assertEqual(rover.direction, end)


if __name__ == '__main__':
    unittest.main()
