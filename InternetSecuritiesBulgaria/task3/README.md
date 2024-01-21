# Condition:

Using libraries by your choice (hint - requests & BeautifulSoup4 libraries should do the job) write a Python script
that:

* Opens the following webpage: 'https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population'

* Extracts the data_rows from the table named "List of European Union member states by population"

* Using values from columns 'Country' and 'Official figure' it should create a countries_dictionary variable with a
  structure:
  {country1:{'population': official figure1}, country2:{'population': official figure2}, etc.}

for example
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

* Sums country_population values for all countries in the dictionary to get the total_country_population and calculates
  for each country its country_population_percentage from the total_country_population;

then adds this country_population_percentage to the countries_dictionary;
finally prints the countries_dictionary and it should look similar to:
<pre>
{ 
    'Germany': {
        'country_population': 83237124,
        'country_population_percentage': 18.5
    },
    'France': {
        'country_population': 67874000,
        'country_population_percentage': 15
    },
    'Italy': {
        'country_population': 58906742,
        'country_population_percentage': 13.3 
    },
}
</pre>
