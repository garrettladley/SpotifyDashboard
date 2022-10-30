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


if __name__ == '__main__':
    unittest.main()
