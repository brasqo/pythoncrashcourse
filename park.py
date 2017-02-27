#park, if-elif-else

age = raw_input("How old are you?: ")
dots = "..."

if int(age) < 4:
	print("You're " + str(age) + " years old, you pay $0.")
elif int(age) < 18:
	print("You're " + str(age) + " years old, you pay $5.")
else:
	print("You're " + str(age) + " years old, you pay $10.")

print(dots)

#Different way of writing the above whwre of i wanted to change the 
#text/print output, I'd only have to edit one line instead of 3.
if int(age) < 4:
	price = 0
elif int(age) < 18:
	price = 5
else:
	price = 10

print("See below for your statement:")
print("You're " + str(age) + " years old, so you pay $" + str(price) + ".")

