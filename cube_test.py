import unittest
import cube

class TestCube(unittest.TestCase):
    def test1(self):
        self.assertEqual(cube.cal_cube(2),8)
        self.assertEqual(cube.cal_cube(1),1)

    def test2(self):
        self.assertEqual(cube.cal_cube('ghjkug'),"TypeError")
        self.assertEqual(cube.cal_cube('/*-'),"TypeError")

    def test3(self):
        self.assertEqual(cube.cal_cube(1.1),1.331)
        self.assertEqual(cube.cal_cube(5.5),166.375)


if __name__ == '__main__':
    unittest.main(verbosity=2)