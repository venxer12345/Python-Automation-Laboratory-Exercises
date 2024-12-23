import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the quote and author data
data = []
for quote in soup.find_all('div', class_='quote'):
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    data.append([text, author])

# Save the scraped data into a CSV file
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])  # Header row
    writer.writerows(data)  # Data rows

print("Data saved to data.csv")