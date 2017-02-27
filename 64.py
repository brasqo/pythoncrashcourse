# -- 6-4 Glossary 2
dots = "..."

words = {
	'apple': 'A fruit that grows on a tree.', 
	'hockey puck': 'A round black disc used in the game of hockey.',
	'bumble bee': 'A flying insect that produces honey.', 
	'Pac-Man': 'Wokka wokka wokka.', 
	'Mario': 'Itsa meeee, Mario!', 
	'2pac': 'Holla if ya hear me!', 
	'Biggie': 'A fat dead rapper.'
	}

## print("An apple is defined as: " + words['apple'])
## print("A hockey puck is defined as: " + words['hockey puck'])
## print("A bumble bee is defined as: " + words['bumble bee'])

for key, value in words.items():
	print("\nWord: " + key)
	print("Definition: " + value)

#--> 6-5 rivers
print(dots)

rivers = {
	'nile': 'egypt', 
	'wando': 'charleston', 
	'mississippi': 'southern USA'
	}

#-- 6-5 A
for key1, value1 in rivers.items():
	print("The " + key1.title() + " runs thru " + 
	value1.title() + ".")
#-- 6-5 B
for key2 in rivers.keys():
	print(key2.title())
#-- 6-5 C
for value2 in rivers.values():
	print(value2.title())

# 6-6 

print(dots)


favelanguage = {
	'jen':'python', 
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python', 
	'bill':'python',
	}

nopoll = ['bill','steve']

for name in favelanguage.keys():
	print("TY " + name.title() + " for taking the poll.")

for items in nopoll:
	if items not in favelanguage.keys():
		print("Hey " + str(items.title()) + ", please take the poll!")







