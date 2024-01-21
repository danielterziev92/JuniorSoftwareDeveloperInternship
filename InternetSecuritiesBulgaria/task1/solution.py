import re


def get_all_date(patterns, text):
    matches = []

    for pattern in patterns.values():
        match = re.findall(pattern, text)
        if match:
            matches.extend(match)

    return set(matches)


def get_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read().replace('\n', '')
        return file_content


def main():
    file_path = 'text.txt'
    text = get_text_from_file(file_path)

    all_patterns = {
        'date_with_dashes': r'\b\d{4}-\d{2}-\d{2}\b',
        'date_with_backslashes': r'\b\d{4}/\d{2}/\d{2}\b',
        'date_with_months': r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b',
        'date_with_month_and_hour': r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:h)?\b',
        'date_with_month_name_and_year': r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?,\s+\d{4}\b'
    }

    print(get_all_date(all_patterns, text))


if __name__ == "__main__":
    main()
