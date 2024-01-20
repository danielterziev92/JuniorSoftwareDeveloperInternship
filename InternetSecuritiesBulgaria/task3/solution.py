import json

import requests
from bs4 import BeautifulSoup


def extract_population_data(source_url):
    response = requests.get(source_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with the specified name
    table = soup.find('table', class_='wikitable')

    all_countries = dict()

    for row in table.find_all('tr')[2:]:  # Skip the header rows
        columns = row.find_all(['td', 'th'])
        country_name = columns[1].contents[1].text
        country_population = int(''.join(columns[4].text.split(',')))

        if country_name not in all_countries:
            all_countries[country_name] = {'country_population': 0}

        all_countries[country_name]['country_population'] += country_population

    return all_countries


def get_total_country_population(countries_data):
    return sum(country_data['country_population'] for country_data in countries_data.values())


def calculate_percentage(countries_data, total_country_population):
    for country, country_data in countries_data.items():
        population = country_data['country_population']
        percentage = (population / total_country_population) * 100
        countries_data[country]['country_population_percentage'] = round(percentage, 1)


def write_in_json_file(countries_data, indent_space):
    with open('countries_data.json', 'w') as json_file:
        json.dump(countries_data, json_file, indent=indent_space)

    print("JSON data has been written to 'countries_data.json'")


def main():
    url = 'https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population'

    countries = extract_population_data(url)
    total_country_population = get_total_country_population(countries)
    calculate_percentage(countries, total_country_population)
    indent_space = 4
    write_in_json_file(countries, indent_space)


if __name__ == "__main__":
    main()
