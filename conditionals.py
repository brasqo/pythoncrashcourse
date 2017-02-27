#Tests for equality and inequality with strings
#Tests using the lower() function
#Numerical tests involving equality and inequality, greater than and
#less than, greater than or equal to, and less than or equal to
#Tests using the and keyword and the or keyword
#Test whether an item is in a list
#Test whether an item is not in a list

people = ['Tracey', 'Jacob', 'Indy', 'Maga', 'Papa']
family = []
wife = 'tracey'


if 'Tracey' in people:
	print("Yes, they are in the family!")
else:
	print("No, they are not in the family")

if 'dopey' in people:
	print("Yes, they are in the family!")
else:
	print("No, they are not in the family")


x = 7
y = 13

if x >= y:
	print(str(x) + " is greater than or equal to " + str(y))
else:
	print("Nooooope, " + str(x) + " isnt greater than " + str(y))

if x == y:
	print(str(x) + " is equal to " + str(y))
else:
	print("Nooooope, " + str(x) + " isnt equal to " + str(y))


if x <= y:
	print(str(x) + " is less than or equal to " + str(y))
else:
	print("Nooooope, " + str(x) + " isnt less than or equal to " + str(y))

shopping = ['apple', 'cereal', 'drugs']
item1 = 'apple'
item2 = 'beer'

if item1 in shopping:
	print(item1.title() + " is on the list")
else:
	print(item1.title() + " is NOT on the list")

if item2 in shopping:
	print(item2.title() + " is on the list")
else:
	print(item2.title() + " is NOT on the list")



	
