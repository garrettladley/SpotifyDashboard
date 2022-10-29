import os
import unittest

import main
from main import Term


# unit tests for the limit_clamper function in main
class TestLimitClamper(unittest.TestCase):

    def test_neg1(self):
        self.assertEqual(1, main.limit_clamper(-1))

    def test_0(self):
        self.assertEqual(1, main.limit_clamper(0))

    def test_51(self):
        self.assertEqual(50, main.limit_clamper(51))

    def test_25(self):
        self.assertEqual(25, main.limit_clamper(25))


# unit tests for the titler function in main
class TestTitler(unittest.TestCase):

    def test_titler_t10_artists_oat(self):
        self.assertEqual('Your Top 10 Artists of All Time:', main.titler(10, 'Artists', Term.LONG))

    def test_titler_t10_artists_medium(self):
        self.assertEqual('Your Top 10 Artists of the Past 6 Months:', main.titler(10, 'Artists', Term.MEDIUM))

    def test_titler_top_artist_short(self):
        self.assertEqual('Your Top 10 Artists of the Past 4 Weeks:', main.titler(10, 'Artists', Term.SHORT))

    def test_titler_top_artist_oat(self):
        self.assertEqual('Your Top Artist of All Time:', main.titler(1, 'Artists', Term.LONG))


# unit tests for the list_formatter function in main
class TestListFormatter(unittest.TestCase):

    def test_typical_list(self):
        self.assertEqual('Your Top 10 Artists of All Time:' + os.linesep +
                         '1) John' + os.linesep +
                         '2) Jane' + os.linesep +
                         '3) Foo' + os.linesep +
                         '4) Bar' + os.linesep +
                         '5) Jack' + os.linesep +
                         '6) Johnson' + os.linesep +
                         '7) Garrett' + os.linesep +
                         '8) Mitchell' + os.linesep +
                         '9) Ladley' + os.linesep +
                         '10) Python' + os.linesep, main.list_formatter([['John',
                                                                          'Jane',
                                                                          'Foo',
                                                                          'Bar',
                                                                          'Jack',
                                                                          'Johnson',
                                                                          'Garrett',
                                                                          'Mitchell',
                                                                          'Ladley',
                                                                          'Python'],
                                                                         'Your Top 10 Artists of All Time:']))


if __name__ == '__main__':
    unittest.main()
