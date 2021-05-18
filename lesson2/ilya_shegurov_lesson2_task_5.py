prices = [57.8, 46.51, 97, 17.37, 78.6, 34.9, 12.98, 4.3]

for price in prices:
    price = int(round(price * 100))
    robles = price // 100
    cents = price % 100
    print(f'{robles} руб {cents} коп.')
print('-' * 100)

# сортировка по убыванию
prices.sort()
for price in prices:
    price = int(round(price * 100))
    robles = price // 100
    cents = price % 100
    print(f'{robles} руб {cents} коп.')

# сортировка в обратном порядке и  с созданием списка нового
price_bascet = sorted(prices, reverse=False)
print(price_bascet)

# вывести  цены 5 самых дорогих товаров
for price in prices[:5]:
    price = int(round(price * 100))
    robles = price // 100
    cents = price % 100
    print(f'{robles} руб {cents} коп.')
