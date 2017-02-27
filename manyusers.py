# many users

users = {
	'aeinstein': {
		'first': 'albert', 
		'last': 'einstein', 
		'locations': 'princeton',
		},

	'mcurie': {
		'first': 'marie', 
		'last': 'curie', 
		'locations': 'paris',
		},

	}

for username, userinfo in users.items():
	print("\nUsername: " + username)
	fullname = userinfo['first'] + "" + userinfo['last']
	location = userinfo['locations']

	print("\tFull name: " + fullname.title())
	print("\tLocation: " + location.title())

print("...")


#----> 6-7
people = {
	'wife': {
		'firstname': 'Tori', 
		'lastname': 'Johnson', 
		'age': 37, 
		'city': 'Omaha',
		},
	'son': {
		'firstname': 'John',
		'lastname': 'Johnson',
		'age': 4,
		'city': 'Omaha',
		},
	'pet': {
		'firstname': 'Ike',
		'lastname': 'Johnson',
		'age': 5,
		'city': 'Omaha',
		},
	}

for person, personinfo in people.items():
	print("\nMy " + person + "'s info is the following: ")
	fullname = personinfo['firstname'].title() + " " + personinfo['lastname'].title()
	age1 = personinfo['age']
	location1 = personinfo['city']

	print("\tFull Name: " + fullname.title())
	print("\t" + fullname.title() + " is " + str(age1) +
	 " years old, and lives in " + location1.title())


