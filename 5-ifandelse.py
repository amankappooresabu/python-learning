age = int(input('Enter your age :'))
if age > 18:
    print('You are eligible')
else:
    print('No')

#Exercise

operator = input('Enter the operator: ')
number1 = float(input('Enter the number 1: '))
number2 = float(input('Enter the number 2: '))

if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '/':
    print(number1/number2)
elif operator == '*':
    print(number1 * number2)
else:
    print('That is the wrong operator')

#Weight convertor program

weight = float(input('Enter your weight'))
unit = input('K or L').strip().upper()

if unit == 'K':
    weight = weight * 2.240 
    unit = 'klgs.'
    print(f"The weight in kilograms is {weight}{unit} ")
elif unit == 'L':
    weight = weight / 2.240
    unit = 'lbs.'
    print(f"The wight in pounds is {weight}{unit}")
else :
    print(f"{unit} is not a valid option")

#Temperature convertor

temp = float(input('Enter the temperature : '))
option = input('C or F').strip().upper()

if option == 'C':
    temp = (temp * 9/5) + 32
    unit = str('F')
    print(f"The temperature in farenhiet is {temp}{unit}")
elif option == 'F':
    temp = (temp - 32) * 5/9
    unit = ('C')
    print(f"The temperature in celsius is {temp}{unit}")
else :
    print(f"Not valid")





