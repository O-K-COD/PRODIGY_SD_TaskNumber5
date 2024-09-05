import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.example.com"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title of the page
    title = soup.find('title').text
    print("Title:", title)

    # Find all the links on the page
    links = soup.find_all('a')
    for link in links:
        print("Link:", link.get('href'))

    # Find all the images on the page
    images = soup.find_all('img')
    for image in images:
        print("Image:", image.get('src'))

    # Find all the paragraphs on the page
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        print("Paragraph:", paragraph.text)

else:
    print("Failed to retrieve page")