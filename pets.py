#---> 6-8 pets

pets = {
	'indy': {
		'type': 'dog',
		'owner': 'Danny',
		},
	'cecil': {
		'type': 'turtle',
		'owner': 'billy',
		},
	'tito': {
		'type': 'bird',
		'owner': 'betty',
		},
	'fluffy': {
		'type': 'fish',
		'owner': 'brian',
		},
	}

for pet, petinfo in pets.items():
	pettype = petinfo['type']
	petowner = petinfo['owner'].title()
	print("\n" + pet.title() + " is a " + pettype + ".")
	print(pet.title() + " is owned by " + petowner.title() + ".")


#--> fave places 6-9
print("...")

faveplaces = {
	'billy': {
		'tropic': 'bermuda',
		'usa': 'montana',
		},
	'faye': {
		'tropic': 'aruba',
		'usa': 'myrtle beach',
		},
	'lisa': {
		'tropic': 'jamaica',
		'usa': 'california',
		},
	}

for place, placeinfo in faveplaces.items():
	tropical = placeinfo['tropic']
	america = placeinfo['usa']
	print("\n" + place.title() + "'s favorite tropical area to visit is " + tropical.title() + ".")
	print(place.title() + "'s favorite place in the US is " + america.title() + ".")

#--> Fave numbers 6-10

print("...")

favenums = {
	'bill': {
		'numbers': [1, 3],
		},
	'bob': {
		'numbers': [2, 22], 
		},
	'jim': {
		'numbers': [27, 39],
		},
	'jake': {
		'numbers': [10, 44],
		},
	'rob': {
		'numbers': [34, 98],
		}, 
	}

for num, numinfo in favenums.items():
	print("\n" + num.title() + "'s fave #s are: ")
	numz = numinfo['numbers']

	for nums in numinfo:
		print(numz)

#-- > 6-11 cities

print("...")



