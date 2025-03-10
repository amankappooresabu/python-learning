something = {
    'Kannur': 'Thaliparamba',
    'Kozhikode' : 'Thamarassery',
    'Ernakulam' : 'Kochi'

}

# print(something.get('Kannur'))
# print(help(something))

# something.update({'Kannur' : 'Hey'})

# something.pop('Ernakulam')

# n = input('Give a key :')
# found = False
# for key in something:
#     if n == key:
#         print('Yes the key exists')
#         print(something.get(n))
#         break
# else:   
#      print('Such a key does not exist')

# Concession stand program

menu = {
    'Fries' : 80,
    'Burger' : 130,
    'Puffs' : 25,
    'Coke' : 50,
    'Popcorn' : 120
}
print('---------------------')
for keys, values in menu.items():
    print(f" {keys:10} : {values:.2f}")
print('---------------------')

cart = []
total = 0

while True :
    food = input(" Choose the items :" )
    if food == 'exit':
        break
    elif food is not None:
        cart.append(food)
        total = total + menu.get(food)
    else:
        print('Food is not in the menu')

print('---------------------')
for n in cart:
    print(n)
print('---------------------')

print(f'Total : {total}')

    




