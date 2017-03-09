# --> 8-12 Sandwiches

def sandwich(*toppings):
	"""summarie the toppings wanted on a sandwich"""
	print("\nYou want the following on your sandwich:")
	for topping in toppings:
		print("- " + topping)

sandwich('ham', 'swiss')
sandwich('roast beef', 'mayo', 'provolone')
sandwich('pastrami', 'swiss', 'mustard', 'pickels')

print("...")

#--> 8-13 User profile.
def build_profile(first, last, **user_info):
	"""build a dictionary containing everything we 
	know about a user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('donnie', 'brasco', 
							location= 'new york', 
							gender= 'male', 
							phone= '555-555-5555',)

print(user_profile)

print("...")
#--> 8-14 cars
def cars(make, model, **other):
	car_list = {}
	car_list['make_name'] = make
	car_list['model_name'] = model
	for key, value in other.items():
		car_list[key] = value
	return car_list

car_info = cars('subaru', 'outback', 
				color= 'blue', interior= 'black')

print(car_info)
