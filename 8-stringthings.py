# name = str(input('Enter your name: '))

# result = len(name.strip())

# print(f"The length of your name is {result}")

# result = name.find('a')
# result1 = name.count('a')
# result2 = name.replace('a','l')
# print(result1)

#Validate user input

username = (input('Enter your username: '))

if len(username) > 12:
    print('The username is too long')
elif username.find(' ')!= -1:
    print('The username should not have spaces')
elif username.isalpha() == False:
    print('The username should only contains alphabets')
else:
    print(f'Welcome {username}')


