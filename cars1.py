#if statements 
dots = "..."
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

print(dots)

requestedtopping = 'mushrooms'
if requestedtopping != 'anchovies':
	print("Hold the anchovies!")

if requestedtopping == 'mushrooms':
	print("Ding ding! You loves dat mushroom")
else:
	print("Mushrooms taste like dogshit, fuck that noise")

print(dots)

if 'lexus' in cars:
	print("Yes, audi is in the list")
else:
	print("Nooope, lexus is not listed.")

print(dots)
#banned users

bannedusers = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in bannedusers:
	print(user.title() + ", you can post a response.")
