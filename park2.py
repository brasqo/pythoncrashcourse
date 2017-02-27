#multi elif
#Anything over a certain value means you pay 5
#else is not required at end of if-elif chain. Can end
#with elif.

age = raw_input("How old are you?: ")

if int(age) < 4:
	price = 0
elif int(age) < 18:
	price = 5
elif int(age) < 65:
	price = 10
elif int(age) >= 65:
	price = 5

print("You're " + str(age) + ", so you have to pay $" + str(price) + ".00.")
