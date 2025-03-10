phone = ['Iphone', 'Smasung', 'Xiaomi' , 'Pixel']
buds = ['Airpods', 'Nirvana', 'Pixel buds', 'Galaxy buds']

products = [phone, buds]

print(products)

for collection in products:
    for item in collection:
        print(item, end = " ")
    print()

