''' brickpy module. '''
import sys
import requests
from bs4 import BeautifulSoup


def target(data):
    ''' Check target for availability. '''
    data = data
    lookup = requests.post('https://brickseek.com/target-inventory-checker/',
                           data=data)

    soup = BeautifulSoup(lookup.text, 'html.parser')

    for avail in soup.find_all(class_='availability-2'):
        print('store-name: '+avail.parent.parent.parent.find('h4').text)
        print('address: ' +
              avail.parent.parent.parent.find(class_='store-address').text)
        print('price (if available) :' +
              avail.parent.parent.parent.find(class_='store-price').text
              .strip())
        print('---------')


def main(**kwargs):
    ''' main function. '''
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


if __name__ == '__main__':
    main(sku=sys.argv[1], zip=sys.argv[2])
