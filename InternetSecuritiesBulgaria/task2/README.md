## Developed a Python script utilizing requests and BeautifulSoup4 libraries to:

* Access the webpage 'https://bnb.bg/Statistics/StInterbankForexMarket/index.htm'
* Extract data_rows from the table named "Спот търговия на банките с чуждестранна валута срещу левове"
* Sort the extracted data in descending order based on values in the 'обем продадени' column
* Save the sorted data to a CSV file
* Implemented functionality to compare the latest downloaded table with the existing CSV file, updating it only if there
  are differences in the tables.