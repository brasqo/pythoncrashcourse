#--> 7-4 pizza toppings
# prompt = "What topping(s) would you like?..."
# prompt += "\nEnter 'quit' when you're done..: "

# while True:
# 	topping = input(prompt)

# 	if topping == 'quit':
# 		break
# 	else:
# 		print("No prob, we'll add " + topping.title() + " to your pizza.")

#--> 7-5 movie tickets
# prompt = "How old are you?: "
# prompt += "\nType 'stop' to stop the program...:"

# while True:
# 	age = input(prompt)
	
# 	if age == 'stop':
# 		break

# 	elif int(age) >= 13:
# 		print("You pay $15")
# 	elif int(age) in range(3, 13):
# 		print ("You pay $10")
# 	elif int(age) < 3:
# 		print("You pay Nothing!")

#--> 7-6 Three Exits
prompt = "How old are you?: "
prompt += "\nType 'stop' to stop the program...:"

active = True
while active:
	age = input(prompt)
	
	if age == 'stop':
		active = False

	elif int(age) >= 13:
		print("You pay $15")
	elif int(age) in range(3, 13):
		print ("You pay $10")
	elif int(age) < 3:
		print("You pay Nothing!")

