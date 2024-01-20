import re


def get_all_date(text):
    date_with_dashes = r'\b\d{4}-\d{2}-\d{2}\b'
    date_with_backslashes = r'\b\d{4}/\d{2}/\d{2}\b'
    date_with_month_name_and_year = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?,\s+\d{4}\b'
    date_with_months = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b'
    date_with_month_and_hour = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:h)?\b'

    all_pattern = [date_with_dashes, date_with_backslashes, date_with_months, date_with_month_name_and_year,
                   date_with_month_and_hour]

    matches = []

    for pattern in all_pattern:
        match = re.findall(pattern, text)
        if match:
            matches.extend(match)

    return set(matches)


def main():
    # Sample text
    text = """
    Hi, 
    my name is Jane and my phone number is 555-123-4567. 
    My email address is jane_doe@example.com. 
    I live on 123 Main St. Apt. #456, and I was born on January 11th, 1990. 
    I have an appointment on 2023-05-15 at 2:30pm at 789 Oak Ln. #3 and backup on 2023/05/21. 
    Please give me a call or send me an email to confirm. In case the dates are unavailable, please set up a meeting sometime in June. I would love June 19h.
    Thank you!
    """

    dates = get_all_date(text)
    print(dates)


if __name__ == "__main__":
    main()
