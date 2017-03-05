#--> cities 6-11

cities = {
	'boston': {
		'fact': 'the red sox suck',
		},
	'ny': {
		'fact': 'the yankees own the sox',
		},
	}

for city, facts in cities.items():
	# print(city)
	# print(facts)
	fct = facts['fact']
	print("\nA fun fact about " + city.title() + " is that " + 
		fct.title() + ".")

#--> 6-12

print("...")

