#buffet

buffet = ('apple', 'orange', 'sushi', 'pizza', 'burger')

print("Here are all the foods the restaurant offers:")
for food in buffet:
	print(food.title())

#intentional error below, comment it out after
#seeing the output error. Trying to replace a 
#value in a tuple.
# ---> buffet[0] = ('lemon')

#reconfigure the tuple, and print out the new
#result.
buffet = ('apple', 'mac n cheese', 'coffee', 'pizza', 'burger')

print("\nThe new menu is:")
for food2 in buffet:
	print(food2.title())


