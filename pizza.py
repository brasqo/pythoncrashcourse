# --> pizza - passing arbitrary numberof arguments.

# def make_pizza(*toppings):
# 	"""print the list of toppings that have been requested."""
# 	print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

#-----
def make_pizza(*toppings):
	"""summarize the pizza we are about to make."""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print("...")

#--- Mixing positional and arbitrary arguments.
def make_pizza1(size, *toppings):
	"""summarize the pizza we are about to make."""
	print ("\nMaking a " + str(size) + 
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza1(16, 'pepperoni')
make_pizza1(12, 'mushrooms', 'green peppers', 'extra cheese')