import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for pagination (replace 'page_num' with the actual URL structure)
base_url = 'https://example-college-sports-list.com/page/'  # Replace with actual base URL

# Initialize empty lists to store college names and website links
colleges = []
links = []

# Loop through multiple pages (adjust range according to number of pages)
for page_num in range(1, 5):  # Replace 5 with the total number of pages
    url = f'{base_url}{page_num}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Adjust this part based on how the table is structured
    for row in soup.find_all('tr'):  # Assuming each college is listed in a table row
        columns = row.find_all('td')
        if len(columns) > 1:
            college_name = columns[0].find('a').text.strip()  # Extract the college name
            athletic_link = columns[0].find('a')['href']  # Extract the link
            
            # Add 'https://example-college-sports-list.com' to complete relative URLs
            athletic_link = 'https://example-college-sports-list.com' + athletic_link
            
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
