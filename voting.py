#voting

age = raw_input('How old are you?: ')

if int(age) >= 18:
	print("You are " + str(age) + ", so you're old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("You're " + str(age) + ",so you're too young to vote. Sorry!")
	print("Make sure you register to vote when you're 18.")
