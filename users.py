# users

# user0 = {
# 	'username': 'efermi', 
# 	'first': 'enrico', 
# 	'last': 'fermi', 
# 	}

# for key, value in user0.items():
# 	print("\nKey: " + key)
# 	print("Value: " + value)

#---

favelanguage = {
	'jen':'python', 
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python',
	}
#----
# for name, language in favelanguage.items():
# 	print(name.title()+ "'s favorite launguage is " + 
# 		language.title() + ".")

# for name1 in favelanguage.keys():
# 	print(name1.title())
#---

friends = ['phil', 'sarah']
for name2 in favelanguage.keys():
	print(name2.title())

	if name2 in friends:
		print(" Hi " + name2.title() + 
			", I see your favorite launguage is " + 
			favelanguage[name2].title() + "!")

if 'erin' not in favelanguage.keys():
	print("Erin, please take our poll!")

#-- looping thru dictionarys keys in order. 

for name3 in sorted(favelanguage.keys()):
	print(name3.title() + ", thank you for taking the poll.")

#-- looping thru all values in a dictionary

print("The following languages have been mentioned:")

#-- prints in a set (no duplicate values)
for language1 in set(favelanguage.values()):

# doesnt print as set)
# for language1 in favelanguage.values():
	
	print(language1.title())
