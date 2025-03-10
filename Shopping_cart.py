foods = []
total = []
last = 0
while True:
    food = input("Enter your food item ")
    if food == "exit":
     break
    else:
          price = float(input("Enter the price of the item "))
          foods.append(food)
          total.append(price)

print(foods)
print(total)

for price in total:
    last += price

print(f"The total amount is {last}")

