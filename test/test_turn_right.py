import unittest

from src.mars_rover import MarsRover


class rover(unittest.TestCase):
    def test_turn_right_facing_north(self):
        rover = MarsRover([4, 7], 'N')
        rover.rotate_right('R')
        self.assertEqual(rover.direction, 'E')


if __name__ == '__main__':
    unittest.main()
