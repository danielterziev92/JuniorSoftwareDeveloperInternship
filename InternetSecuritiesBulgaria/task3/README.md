#### In this task, I created a Python script leveraging web scraping libraries, specifically utilizing requests to fetch the HTML content and BeautifulSoup to parse and extract data. The target webpage was 'https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population'.

Upon accessing the webpage, the script identified and extracted data from the table named "List of European Union member
states by population." This table contains information about European Union member states, including columns for '
Country' and 'Official figure.'

Upon accessing the webpage, the script identified and extracted data from the table named "List of European Union member
states by population." This table contains information about European Union member states, including columns for '
Country' and 'Official figure.'

<pre>
{
    'Germany': {
        'country_population': 83237124
    },
    'France': {
        'country_population': 67874000
    },
    'Italy': {
        'country_population': 58906742},
    etc.
}
</pre>

To enhance the dictionary, I calculated the total population across all countries and then determined the percentage of
each country's population relative to the total. These country population percentages were added to the corresponding
entries in the countries_dictionary under the key 'country_population_percentage.'

Finally, the script printed the resulting countries_dictionary, showcasing detailed information about each country,
including both population and population percentage.
