#-- > cities.py - using break to exit the loop.

prompt = "\nPlease enter the name of a city you visited:"
prompt += "\n(Enter 'quit' when you're done.) "

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")

