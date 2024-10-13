import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for the NCAA schools index (base for constructing page URLs)
base_url = "https://www.ncaa.com"

# Lists to store college names and their respective links
colleges = []
links = []

# Start with the first page (index page)
start_url = f"{base_url}/schools-index"

# Send the request to the first page
response = requests.get(start_url)

# Check if the response is OK
if response.status_code == 200:
    # Parse the first page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the pagination section
    pagination = soup.find('div', class_='school-pager')

    if pagination:
        # Find all pagination links (a tags with href)
        page_links = pagination.find_all('a')

        # Extract all unique hrefs for pagination (to get all page URLs)
        page_urls = [start_url]  # Add the first page manually
        for page_link in page_links:
            href = page_link.get('href')
            if href and href not in page_urls:
                page_urls.append(base_url + href)

        # Now, iterate over all pages and extract data from each one
        for page_url in page_urls:
            print(f"Processing: {page_url}")
            response = requests.get(page_url)
            
            # Check if the response is OK
            if response.status_code != 200:
                print(f"Failed to retrieve page {page_url}")
                continue  # Skip to the next page

            # Parse the page content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all rows in the table body that contain the school names and links
            table_rows = soup.select('tbody tr')

            # Extract the name and link for each school
            for row in table_rows:
                # Find the first <a> tag which contains the link
                link_tag = row.find('a')

                if link_tag:
                    college_link = base_url + link_tag['href']  # Construct the full link

                    # Find the college name in the second <td> element
                    name_td = row.find_all('td')[1]  # Access the second <td> element
                    college_name = name_td.text.strip()  # Get the text (college name)

                    # Append to lists
                    colleges.append(college_name)
                    links.append(college_link)

# Create a DataFrame to hold the data
df = pd.DataFrame({
    'College': colleges,
    'Link': links
})

# Save the DataFrame to a CSV file
df.to_csv('ncaa_colleges.csv', index=False)

print("CSV file 'ncaa_colleges.csv' created successfully!")
