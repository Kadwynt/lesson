def format_price (price):
    price = int(price)
    return "Цена: {} руб.".format(price)
e = format_price(56.24)
print(e)