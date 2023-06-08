import unittest


class DummyTest(unittest.TestCase):
    def test_anything(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
