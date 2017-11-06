from bs4 import BeautifulSoup
import requests

data = {
    'search_method': 'sku',
    'sku': 'numbers',
    'upc': '',
    'zip': 'zip',
    'sort': 'distance'
}

r = requests.post('https://brickseek.com/target-inventory-checker/', data=data)

soup = BeautifulSoup(r.text, 'html.parser')

for avail in soup.find_all(class_='availability-2'):
    avail.parent.parent.parent.find('h4').text
    avail.parent.parent.parent.find(class_='store-address').text
    avail.parent.parent.parent.find(class_='store-price').text
