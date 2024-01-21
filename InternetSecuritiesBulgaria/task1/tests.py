from unittest import TestCase

from task1.solution import get_all_date, get_text_from_file


class TestTask1(TestCase):

    def setUp(self):
        test_text = '''
Hi,
my name is Jane and my phone number is 555-123-4567.
My email address is jane_doe@example.com.
I live on 123 Main St. Apt. #456, and I was born on January 11th, 1990.
I have an appointment on 2023-05-15 at 2:30pm at 789 Oak Ln. #3 and backup on 2023/05/21.
Please give me a call or send me an email to confirm. In case the dates are unavailable, please set up a meeting 
sometime in June. I would love June 19h.Thank you!
'''

        self.text = test_text.replace('\n', '')

    def test_date_with_dashes_pattern(self):
        patterns = {'date_with_dashes': r'\b\d{4}-\d{2}-\d{2}\b', }

        result = get_all_date(patterns, self.text)
        expected_result = '2023-05-15'

        self.assertIn(expected_result, result)

    def test_date_with_backslashes(self):
        patterns = {'date_with_backslashes': r'\b\d{4}/\d{2}/\d{2}\b', }

        result = get_all_date(patterns, self.text)
        expected_result = '2023/05/21'

        self.assertIn(expected_result, result)

    def test_date_with_month_name(self):
        patterns = {
            'date_with_months': r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b',
        }

        result = get_all_date(patterns, self.text)
        expected_results = ['June', 'January']

        for expected_result in expected_results:
            self.assertIn(expected_result, result)

    def test_date_with_month_and_hour(self):
        patterns = {
            'date_with_month_and_hour': r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:h)?\b',
        }

        result = get_all_date(patterns, self.text)
        expected_result = 'June 19h'

        self.assertIn(expected_result, result)

    def test_date_with_month_day_and_year(self):
        patterns = {
            'date_with_month_name_and_year': r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?,\s+\d{4}\b'
        }

        result = get_all_date(patterns, self.text)
        expected_result = 'January 11th, 1990'

        self.assertIn(expected_result, result)

    def test_get_text_from_file(self):
        file_path = 'text.txt'

        result = get_text_from_file(file_path)
        expected_result = self.text

        self.maxDiff = None

        self.assertEqual(expected_result, result)
