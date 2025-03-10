#While loop

name = str(input('Enter your name: ')).strip()
while name == "":
    print('Name cannot be empty')
    name = (input('Enter your name: '))


number = int(input('Enter a number between 1 and 5'))
while number<1 or number>10 or "":
    print(f"{number} is not valid")
    number = int(input('Enter a number between 1 and 5'))
print(f"The number is {number} and hello {name}")




