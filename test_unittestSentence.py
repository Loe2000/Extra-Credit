import sentence
import unittest

class TestSentenceReverse(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sentence.reverse("hello world"), "world hello")

    def test_2(self):
        self.assertEqual(sentence.reverse("wow very nice and cool"), "cool and nice very wow")

if __name__ == '__main__':
    unittest.main()