import unittest


class Rover:
    def __init__(self, coordinates, direction):
        self.coordinates = coordinates
        self.direction = direction

    def rotate_right(self, rotate):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'

class rover(unittest.TestCase):
    def test_turn_right_facing_north(self):
        rover = Rover([4, 7], 'N')
        rover.rotate_right('R')
        self.assertEqual(rover.direction, 'E')


if __name__ == '__main__':
    unittest.main()
