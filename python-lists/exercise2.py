print('Step 1')
print('Test a value for inclusion in a list.')
numbers = [1, 3, 5]

print(5 in numbers)
print(8 in numbers)

print(5 not in numbers)
print(8 not in numbers)

print('Step 3')
print('Loop through a list')
cities = ["Chicago", "London", "Tokyo"]

for city in cities:
  print(city)

print('Step 4')
print('Break out of a for loop')

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
numbers.sort()

for number in numbers:
  if number > 42:
    break
  print(number)

print('Step 5')
print('Use an else statement')
import random
numbers = []

while len(numbers) < 5:
  numbers.append(random.randint(1, 100))

for number in numbers:
  print(number)
  if number >= 90:
    print('Found at least one number greater than 90')
    break
else:
  print('No numbers greater than 90')

print('Complete')

print('Step 6')
print('Use a continue statement')
values = ["laptop", 7, "phone", 3, "dslr", 5]
equipment = []

for value in values:
  if isinstance(value, str) == False:
    continue
  equipment.append(value)

print(equipment)

print('Step 7')
print('Create nested for loops')
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

for  suit in suits:
  for rank in ranks:
    print(f'{rank} of {suit}')

print('Step 8')
print('Choose randomly from a list')
import random

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
selected_number = random.choice(numbers)
print(selected_number)

selected_numbers = random.choices(numbers, k=3)
print(selected_numbers)