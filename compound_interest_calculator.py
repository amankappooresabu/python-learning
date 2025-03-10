#Compound interest calculator

principal=float(input('Enter the principal amount : '))
while principal < 0:
    print('The amount is invalid')
    principal=float(input('Enter the principal amount : '))

rate=float(input('Enter the rate of interest : '))
while rate < 0:
    print('The rate is invalid')
    rate=float(input('Enter the rate of interest : '))

time=float(input('Enter the time in years : '))
while time < 0:
    print('The time is invalid')
    time=float(input('Enter the time in years : '))

total = principal * pow((1 + rate/100),time)

print(f"The totl amount in {time} years is {total} ")
