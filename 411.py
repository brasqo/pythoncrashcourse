#4-11

mypizza = ['pepperoni', 'cheese', 'pepper',
'sausage', 'spinach']

friendpizza = mypizza[:]

mypizza.append('squash')
friendpizza.append('pineapple')

print("My fave pizzas are:\n")
for pizza in mypizza:
	print(pizza.title())


print("My friends fave pizzas are:\n")
for pizza2 in friendpizza:
	print(pizza2.title())
