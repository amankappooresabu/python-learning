# Functions : Codes can be resued through functions

def hy(name):
    print(f"Hello {name}")

n = input('Enter your name : ')

hy(n)

def add(x,y):
    z = x + y
    return z

a  = int(input('Enter first number :'))
b  = int(input('Enter second number :'))

k = (add(a,b))
print(f"The number is {k}")

# ----Default arguments-----

def add(x,y=9):
    return x + y

print(add(7))

import time

def count_down(end,start=0):
    for i in range(start,end+1):
        time.sleep(0.25)
        print(i)

count_down(8)

# Arbitrary arguments 

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

n = int(input('How many numbers do you want to add ?'))
print('Enter the numbers to add:')
all_num = []
for num in range(n):
    num = int(input())
    all_num.append(num)

print(add(*all_num))

def hey(**kwargs):
    for value in kwargs.values():
        print(value)

hey(Name ='Aman')