import requests
from bs4 import BeautifulSoup

# URL of the GitHub profile
url = "https://github.com/khaouitiabdelhakim"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the span element with the specified class
    span_element = soup.find('span', class_='p-name vcard-fullname d-block overflow-hidden')
    
    # Extract the text content
    if span_element:
        full_name = span_element.text.strip()
        print("Full Name:", full_name)
    else:
        print("Span element not found.")
else:
    print("Failed to fetch page:", response.status_code)
