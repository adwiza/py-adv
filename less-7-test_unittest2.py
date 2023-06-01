import unittest


def to_perc(x, total):
    if x > total:
        raise ValueError('Nonsense!')
    return x * 100.0 / total


# IF TOTAL WILL BE 0 WE WILL HAVE AN ERROR, WITH A 100% TEST COVERAGE !!!

class Test(unittest.TestCase):
    def test_perc(self):
        self.assertEqual(0, to_perc(0, 100))
        self.assertEqual(100, to_perc(100, 100))
        self.assertEqual(50, to_perc(50, 100))
        self.assertRaises(Exception, to_perc, 101, 100)


if __name__ == '__main__':
    unittest.main(argv=['firts-arg-is-ignored'], exit=False)
