try:
    import mock
except ImportError:
    from unittest import mock

import unittest
from function import square, main


class TestNotMockedFunction(unittest.TestCase):

    @mock.patch('__main__.square', return_value=1)
    def test_function(self, mocked_square):
        mocked_square.return_value = 25
        # because you need to patch in exact place where function that has to be mocked is called
        self.assertEqual(square(5), 1)

    @mock.patch('function.square', return_value=1)
    @mock.patch('function.cube', return_value=1)
    def test_main_function(self, mocked_square, mocked_cube):
        # underling function are mocks so calling main(5) will return mock
        mocked_square.return_value = 1
        mocked_cube.return_value = 0
        self.assertEqual(main(5), 1)
        mocked_square.assert_called_once_with(5)
        mocked_cube.assert_called_once_with(5)


if __name__ == '__main__':
    unittest.main()
