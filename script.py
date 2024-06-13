import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to fetch
url = 'https://en.wikipedia.org/wiki/List_of_cities_in_Nepal'

# Send GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the <span> element with class "mw-headline" and text "Municipality"
    municipality_heading = soup.find('span', id='Municipality', text='Municipality')
    
    # Check if the heading element was found
    if municipality_heading:
        # Find all <table> elements after the municipality_heading
        tables_after_heading = municipality_heading.find_all_next('table')
        
        # Find the first <table> that follows the heading
        for table in tables_after_heading:
            # Check if the table contains the class 'wikitable' as per your requirement
            if 'wikitable' in table.get('class', []):
                with open('table_content.txt', 'w', encoding='utf-8') as file:
                    file.write(table.prettify())
                print("Table content has been saved to 'table_content.txt'.")
                break# Stop after printing the first matching table
        else:
            print("No table found after the Municipality heading.")
    else:
        print("Municipality heading not found on the page.")
else:
    print(f"Failed to retrieve page: {response.status_code} - {response.reason}")
