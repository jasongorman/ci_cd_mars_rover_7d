import unittest

from parameterized import parameterized

from src.MarsRover import MarsRover

class TestTurnLeft(unittest.TestCase):
    @parameterized.expand([('N', 'W'),('E', 'N'), ('S', 'E'), ('W', 'S')])
    def test_turn_left_facing_north(self, start, end):
        rover = MarsRover([4, 7], start)
        rover.rotate_left('L')
        self.assertEqual(rover.direction, end)


if __name__ == '__main__':
    unittest.main()
