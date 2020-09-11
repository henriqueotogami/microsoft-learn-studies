#The type() function

#print(type('7'))
#print(type(7))
#print(type(7.1))

#The isinstance() function
print(isinstance('7', str))
print(isinstance(7, int))
print(isinstance(7.1, float))

print(isinstance(7, str))
print(isinstance('7', int))
print(isinstance('7.1', float))

#Can you create a Boolean expression by using the type() function?

print(type('7') == str)
print(type(7) == int)
print(type(7.1) == float)

print(type(7) == str)
print(type('7') == int)
print(type('7.1') == float)