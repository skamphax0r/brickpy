''' brickpy module. '''
import sys
import getopt
import requests
from bs4 import BeautifulSoup


def usage():
    print("-z [--zip=]   - Zipcode")
    print("-s [--sku=]   - SKU (or DCTI for Target)")
    print("-h [--help]   - print this message")


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


def main(argv):
    ''' main function. '''

    try:
        opts, args = getopt.getopt(argv, "hs:z:", ["help", "sku=", "zip="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-s", "--sku"):
            sku = arg
        elif opt in ("-z", "--zip"):
            zipcode = arg

    data = {
        'search_method': 'sku',
        'sku': sku,
        'upc': '',
        'zip': zipcode,
        'sort': 'distance'
    }
    target(data)


if __name__ == '__main__':
    main(sys.argv[1:])
