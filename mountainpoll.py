# --> mountain poll - Filling a dictionary w/ user input

responses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
	#Prompt for the persons name and responses
	name = input("\nWhats your name? ")
	response = input("Which mountain would you like to climb someday? ")

	#store the respose in the dictionary
	responses[name] = response

	#Find out if anyone else is going to take the poll
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

#Polling is complete. Show results.
print("\n---Poll Results---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")

