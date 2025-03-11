hey = ['Aman','Alan','Austin']

hey2 = [name.upper() for name in reversed(hey) if name not in hey]
print(hey2)

name = input('Enter the name')

if name in hey:
    print('The name is already in the list')
else:
    hey.append(name)
    print(hey)