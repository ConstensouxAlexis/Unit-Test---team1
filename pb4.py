class TestDateConversion(unittest.TestCase):
    def test_detect_and_convert_to_date(self):
        self.assertEqual(detect_and_convert_to_date('2023-09-14').date(), datetime(2023, 9, 14).date())
        self.assertEqual(detect_and_convert_to_date('14-09-2023').date(), datetime(2023, 9, 14).date())
        # Add more test cases as needed
