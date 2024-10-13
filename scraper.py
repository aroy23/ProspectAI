import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage containing the list of colleges and their athletic websites
url = 'https://www.ncaa.com/schools'  # Replace this with the actual URL you're scraping from

# Send a request to the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Empty lists to hold the scraped data
colleges = []
links = []

# Example: Scraping data from a table
for row in soup.find_all('tr'):  # Assuming each college is listed in a table row
    columns = row.find_all('td')
    if len(columns) > 1:
        college_name = columns[0].text.strip()
        athletic_link = columns[1].find('a')['href']
        
        colleges.append(college_name)
        links.append(athletic_link)

# Create a DataFrame with the scraped data
df = pd.DataFrame({
    'College': colleges,
    'Athletic Website': links
})

# Save the DataFrame to a CSV file
df.to_csv('colleges_athletic_websites.csv', index=False)

print("CSV file 'colleges_athletic_websites.csv' created successfully!")
