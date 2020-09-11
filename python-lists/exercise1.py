print('Step 1')
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

print(colors)
print(type(colors))

print(f'0-based indexing into the list ... second item: {colors[1]}')

print(f'Last item of the list: {colors[-1]}')

print(f'Next to last item in the list: {colors[-2]}')

print('Step 2')
print('\nPrint a SLICE, starting at index 2 and excluding index 5:')
print(colors[2:5])
print(type(colors[2:5]))

print('Step 3')
print('\nPrint a slice, starting at index 0 to index 3:')
print(colors[:3])

print('Step 4')
print('\nPrint a slice, starting a index 4 to the end of the list:')
print(colors[4:])

print('Step 5')
print('\nPrint a slice, from the 4th from the end up until the last item:')
print(colors[-4:-1])

print('Step 6')
print('Reverse and sort the list')
colors.reverse()
print(colors)

colors.sort()
print(colors)

print('Step 7')
print('Treat the list like a queue')
color = colors.pop(0)
print('popped', color)

print(colors)

print('Step 8')
print('Add and remove elements from a list')
print(colors)

colors.append('black')
colors.append('white')

colors.remove('yellow')
colors.remove('orange')

print(colors)

print('Step 9')
print('Combine a new list with an existing list')
new_colors = ['lime', 'gray']
colors.extend(new_colors)
print(colors)

print('Step 10')
print('Clear all items from a list')
colors.clear()
print(colors)