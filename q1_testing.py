from typing import Union
import unittest
import q1

class TestCase(unittest.TestCase):
    def test_reverseString(self):
        self.assertEqual(q1.reverseString("This is CS362 Course"), "Course CS362 is This")

    def test_reverseString(self):
        self.assertEqual(q1.reverseString("CS362 is good"), "doog si 263SC")

if __name__ == '__main__':
    unittest.main()