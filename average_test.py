import unittest
import average

class Testlist(unittest.TestCase):
    def test1(self):
        self.assertEqual(average.list([1,2,3]),2)
        self.assertEqual(average.list([-1,-2,-3]),-2)
    
    def test2(self):
        self.assertEqual(average.list([]),"Empty List")
        self.assertEqual(average.list([10]),10)

    def test3(self):
        self.assertEqual(average.list('/-*'),"Type Error")
        self.assertEqual(average.list('hjkho'),"Type Error")


if __name__ == '__main__':
    unittest.main(verbosity=2)