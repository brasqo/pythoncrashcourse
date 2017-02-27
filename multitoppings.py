#multi lists

availtoppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requesttoppings = ['mushrooms', 'french fries', 'extra cheese']

for requesttopping in requesttoppings:
	if requesttopping in availtoppings:
		print("Adding " + requesttopping + ".")
	else:
		print("Sorry, we dont have " + requesttopping + ".")

print("\nFinished making your pizza!")
