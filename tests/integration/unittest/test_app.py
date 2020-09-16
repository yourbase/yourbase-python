import unittest
import yourbase

class TestAThing(unittest.TestCase):
    def test_a_thing(self):
        print("If you are reading this, this test was not skipped")
        self.assertEqual(True, True)

    def test_another_thing(self):
        print("If you are reading this, this test was not skipped")
        self.assertEqual(False, False)

if __name__ == '__main__':
    unittest.main()
