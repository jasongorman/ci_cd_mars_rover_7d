import unittest

from src.mars_rover import MarsRover

class TestTurnLeft(unittest.TestCase):
    def test_turn_left_facing_north(self):
        rover = MarsRover([4, 7], 'N')
        rover.rotate_left('L')
        self.assertEqual(rover.direction, 'W')


if __name__ == '__main__':
    unittest.main()
