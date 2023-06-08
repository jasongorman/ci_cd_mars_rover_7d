import unittest


from src.MarsRover import MarsRover


class turnright(unittest.TestCase):
    def test_forward_one_facing_north(self):
        rover = MarsRover([4, 7], 'N')
        rover.forwards()
        self.assertEqual(rover.coordinates, [4, 8])

if __name__ == '__main__':
    unittest.main()
