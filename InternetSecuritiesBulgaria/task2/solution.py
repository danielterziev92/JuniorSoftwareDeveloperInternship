import requests
from bs4 import BeautifulSoup
import csv
import os


def fetch_and_parse_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with class 'table'
    table = soup.find('table', class_='table')

    if table:
        # If the table is found, find the tbody inside the table
        tbody = table.find('tbody') or table  # If tbody is not present, use the table itself
    else:
        # If the table is not found, set tbody to None
        tbody = None

    data_cells = []
    if tbody:
        for row in tbody.find_all('tr'):
            cells = row.find_all(['th', 'td'])
            data_row = [cell.text.strip() for cell in cells]

            if data_row[0].startswith('* Обемът на сделките'):
                continue

            data_cells.extend([data_row])

    return data_cells


def sort_data(data, index: int):
    sorted_data = sorted(data, key=lambda x: float(x[index].replace(' ', '')), reverse=True)
    return sorted_data


def save_to_csv(data_rows, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        for row in data_rows:
            writer.writerow(row)

        print(f"Sorted data has been saved to {filename}")


def read_csv(filename):
    data_rows = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=':')
        for row in reader:
            data_rows.append(list(row[0].split(',')))
    return data_rows


def compare_and_rewrite_csv(data_rows, filename):
    # Check if the CSV file already exists
    file_exists = os.path.exists(filename)

    if file_exists:
        data_from_csv = read_csv(filename)

        # Compare the latest downloaded data with the one saved in the CSV file
        if data_rows != data_from_csv:
            # Rewrite the CSV file if the data is different
            save_to_csv(data_rows, filename)
            print("Table has changed. CSV file has been updated.")
        else:
            print("Table has not changed. CSV file remains the same.")
    else:
        # If CSV file doesn't exist, create and save the current data
        save_to_csv(data_rows, filename)
        print("CSV file created.")


def main():
    url = 'https://bnb.bg/Statistics/StInterbankForexMarket/index.htm'
    csv_filename = 'interbank_forex_data.csv'

    data_rows = fetch_and_parse_data(url)
    index_of_volume_sold = 7
    compare_and_rewrite_csv(sort_data(data_rows, index_of_volume_sold), csv_filename)


if __name__ == "__main__":
    main()
