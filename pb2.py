import unittest

class TestDateFormat(unittest.TestCase):
    def test_detect_date_format(self):
        self.assertEqual(detect_date_format('2023-09-14'), 'YYYY-MM-DD')
        self.assertEqual(detect_date_format('14-09-2023'), 'DD-MM-YYYY')
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
