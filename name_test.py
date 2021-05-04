import unittest
import name

class TestName(unittest.TestCase):
    def test1(self):
        self.assertEqual(name.input_name("Tom","Tim"), "Tom Tim")

    def test2(self):
        self.assertEqual(name.input_name("123","456"),"123 456")

    def test3(self):
        self.assertEqual(name.input_name('123/*-s4',1), "Type Error")

if __name__ == '__main__':
    unittest.main(verbosity=2)