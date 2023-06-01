import unittest


def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return int(a) + int(b)
    else:
        raise Exception('Invalid arguments')


class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))
        self.assertEqual(15, add(-6, 21))
        self.assertRaises(Exception, add, 4.0, 5.0)


if __name__ == '__main__':
    unittest.main(argv=['firts-arg-is-ignored'], exit=False)