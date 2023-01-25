def lingerie(size):
    international_size = {'XXS': {'Russia': 42, 'Germany': 36, 'USA': 8, 'France': 38, 'Great Britan': 24},
'XS': {'Russia': 44, 'Germany': 38, 'USA': 10, 'France': 40, 'Great Britan': 26},
'S': {'Russia': 46, 'Germany': 40, 'USA': 12, 'France': 42, 'Great Britan': 28},
'M': {'Russia': 48, 'Germany': 42, 'USA': 14, 'France': 44, 'Great Britan': 30},
'L': {'Russia': 50, 'Germany': 44, 'USA': 16, 'France': 46, 'Great Britan': 32},
'XL': {'Russia': 52, 'Germany': 46, 'USA': 18, 'France': 48, 'Great Britan': 34},
'XXL': {'Russia': 54, 'Germany': 48, 'USA': 20, 'France': 50, 'Great Britan': 36},
'XXXL': {'Russia': 56, 'Germany': 50, 'USA': 22, 'France': 52, 'Great Britan': 38}}

    return international_size[size]
size = str(input("Wrtite your size: "))
try:
    print(f'"You size in all region: " {lingerie(size)}')
except KeyError:
    print(f' error, plese enter correct data: ')
    size = str(input("Wrtite your size: "))
    print(f'"You size in all region: " {lingerie(size)}')

