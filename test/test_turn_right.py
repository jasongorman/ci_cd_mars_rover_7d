import unittest

from src.MarsRover import MarsRover


class rightturn(unittest.TestCase):
    def test_turn_right_facing_north(self):
        rover = MarsRover([4, 7], 'N')
        rover.rotate_right()
        self.assertEqual(rover.direction, 'E')

    def test_turn_right_facing_east(self):
        rover = MarsRover([4, 7], 'E')
        rover.rotate_right()
        self.assertEqual(rover.direction, 'S')

    def test_turn_right_facing_south(self):
        rover = MarsRover([4, 7], 'S')
        rover.rotate_right()
        self.assertEqual(rover.direction, 'W')

    def test_turn_right_facing_west(self):
        rover = MarsRover([4, 7], 'W')
        rover.rotate_right()
        self.assertEqual(rover.direction, 'N')

if __name__ == '__main__':
    unittest.main()
