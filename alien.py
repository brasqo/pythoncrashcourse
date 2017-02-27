#5-4 alien color2

# alienColor = 'blue'

# if 'yellow' in alienColor:
# 	score = 5
# else:
# 	score = 10

#print("You scored " + str(score) + " points!")

# if 'green' in alienColor:
# 	score2 = 5
# elif 'yellow' in alienColor:
# 	score2 = 10
# elif 'red' in alienColor:
# 	score2 = 15
# else:
# 	score2 = 0

# print("Congrats! You acored " + str(score2) + " points!")
# -----------------

#5-6 life stages

age = int(raw_input("How old is the person?: "))

if age < 2:
	label = 'BABY'
elif age <= 3:
	label = 'TODDLER'
elif age <= 12:
	label = 'KID'
elif age <= 19:
	label = 'TEEN'
elif age <= 64:
	label = 'ADULT'
else:
	label = 'ELDER'


print("This person is " + str(age) + ", " + str(label) + "!")
