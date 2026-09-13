# Basic Web Scraper with BeautifulSoup

A simple Python web scraper that retrieves HTML content from a website using the `requests` library and extracts key elements (page title, links, images, and text paragraphs) using `BeautifulSoup`.

## Features
- Sends HTTP GET requests to fetch webpage data
- Verifies HTTP status codes before parsing
- Extracts page title, hyperlinks (`<a>`), images (`<img>`), and text content (`<p>`)
