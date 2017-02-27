#-- > nests

# alien0 = {'color': 'green', 'points': 5}
# alien1 = {'color': 'yellow', 'points': 10}
# alien2 = {'color': 'red', 'points': 15}

# aliens = [alien0, alien1, alien2]

# for alien in aliens:
# 	print(alien)

#------

# make an empty list for storing aliens.
aliens = []

#make 30 green aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

#change the aspects of the first 3 aliens
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	#elif to turn aliens red if they're yellow
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

#show the first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")

# show how many aliens have been created
print("Total # of aliens: " + str(len(aliens)))

# a list in a dictionary

print("...")

# store info about a pizza being ordered.
pizza = {
	'crust': 'thick', 
	'toppings': ['mushrooms', 'extra cheese'],
	}

#Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
	"with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

#----

print("...")

favelanguages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward':['ruby', 'go'],
	'phil':['python', 'haskell'], 
	}

for name, languages in favelanguages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())
	



