from bs4 import BeautifulSoup
import requests
import sys


def target(data):
    ''' Check target for availability '''
    data = data
    r = requests.post('https://brickseek.com/target-inventory-checker/',
                      data=data)

    soup = BeautifulSoup(r.text, 'html.parser')

    for avail in soup.find_all(class_='availability-2'):
        print('store-name: '+avail.parent.parent.parent.find('h4').text)
        print('address: ' +
              avail.parent.parent.parent.find(class_='store-address').text)
        print('price (if available) :' +
              avail.parent.parent.parent.find(class_='store-price').text.strip()) # NOQA
        print('---------')


def main(**kwargs):
    sku = kwargs['sku']
    zipcode = kwargs['zip']
    data = {
        'search_method': 'sku',
        'sku': sku,
        'upc': '',
        'zip': zipcode,
        'sort': 'distance'
    }
    target(data)


main(sku=sys.argv[1], zip=sys.argv[2])
