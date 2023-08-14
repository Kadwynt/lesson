def format_price (price):
    price = int(price)
    return "Цена: {} руб.".format(price)
aaa = format_price(56.24)
print(aaa)