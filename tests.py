'''
This module is used to run unit tests on files.py
'''

import unittest
import os
from files import Files


class TestFileMethods(unittest.TestCase):
    '''
        Class for unit test cases
    '''

    def test_correct_lines(self):
        '''
            Unit test case to check for correctness in finding
            the total number of files, number of lines and
            average number of lines
        '''

        directory = os.path.dirname(__file__)
        directory = os.path.join(directory, 'test')
        actual = Files.main(directory, ".py")
        expected = [2, 53, 26.5]
        self.assertEqual(actual, expected)
        actual = Files.main(directory, ".txt")
        expected = [1, 2, 2.0]
        self.assertEqual(actual, expected)

if __name__ == "__main__":

    # Run unit tests
    unittest.main()
