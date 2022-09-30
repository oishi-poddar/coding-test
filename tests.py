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

    def test_correct_lines_directory(self):
        '''
            Unit test case to check for correctness in finding
            the total number of files, number of lines and
            average number of lines from 1 level directory
        '''

        directory = os.path.dirname(__file__)
        directory = os.path.join(directory, 'test/test2')
        actual = Files.main(directory, ".py")
        expected = [2, 14, 7.0]
        self.assertEqual(actual, expected)
        actual = Files.main(directory, ".txt")
        expected = [1, 3, 3.0]
        self.assertEqual(actual, expected)


    def test_correct_lines_sub_directory(self):
        '''
            Unit test case to check for correctness in finding
            the total number of files, number of lines and
            average number of lines from 2 level directory
        '''

        directory = os.path.dirname(__file__)
        directory = os.path.join(directory, 'test')
        actual = Files.main(directory, ".py")
        expected = [4, 67, 16.75]
        self.assertEqual(actual, expected)
        actual = Files.main(directory, ".txt")
        expected = [2, 5, 2.5]
        self.assertEqual(actual, expected)

    def test_missing_directory(self):
        '''
            Unit test case to check exception thrown
            for incorrect directory path
        '''

        directory = os.path.dirname(__file__)
        directory = os.path.join(directory, 'test!')
        actual = Files.main(directory, ".py")
        self.assertRaises(Exception, actual)

    def test_missing_extensions(self):
        '''
            Unit test case to check exception thrown
            for missing files of provided extension
        '''

        directory = os.path.dirname(__file__)
        directory = os.path.join(directory, 'test')
        actual = Files.main(directory, ".pyt")
        self.assertRaises(Exception, actual)

    def test_empty_file(self):
        '''
            Unit test case to check correct value found
            for empty file
        '''

        directory = os.path.dirname(__file__)
        directory = os.path.join(directory, 'test')
        actual = Files.main(directory, ".html")
        expected = [1, 0, 0.0]
        self.assertEqual(actual, expected)



if __name__ == "__main__":

    # Run unit tests
    unittest.main()
