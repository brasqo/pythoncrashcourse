# 7-8 Deli

sandwich_orders = ['tuna', 'BLT', 'meatball', 'egg salad', 'pastrami', 'pastrami', 'pastrami'] #(a)
finished_sandwichs = []

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')#(c)
	print("Sorry, but we ran out of pastrami.")#(b)

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()

	print("We're making your " + current_sandwich.title() + " sandwich.")
	finished_sandwichs.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwichs:
	print(finished_sandwich.title())

# --> 7-9 No pastrami
# (a) Adding pastrami to sandwich_orders 3x. 
# (b) Adding code near beginning saying "no more pastrami",
# and (c) removing all pastrami occurances.

print("...")
# --> 7-10 Dream vacation - poll users about their 
# dream vacation...

# created an empty list called 'responses'
responses = {}

#set a flag to True
poll_active = True

# started a wihle loop for when flag is True
while poll_active:
	# 2 input variables (name and vacation)
	name = input("\nWhat's your name?: ")
	vacation = input("Where would you like to vacation?: ")
	
	# Im still confused what this syntax is telling me. Maybe:
	# combining the key(name) with the value(vacation)? YES - see Dicts from lists
	responses[name] = vacation
	#input question with a way to turn off flag. Cuts prog off
	# when 'no' is entered. Continues if 'yes'.
	repeat = input("\nIs anyone else taking the poll?: yes/no ")
	if repeat == 'no':
		poll_active = False

# pulls and prints the results from the created dict.
print("\n--- Here Are The Results ---")
for name, vacation in responses.items():
	print(name.title() + " would like to vacation in " + vacation.title() + ".")

