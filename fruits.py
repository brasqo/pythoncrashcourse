#fruits

fruits = ['apple', 'orange', 'lemon']
fruitinput = raw_input("What's your fave fruit?: ")

# if 'apple' in fruits:
# 	label = "You really like apples!"
# else:
# 	label = "You hate that shit!"

# print(label)

for fruitinput in fruits:
	if fruitinput == "apple":
		print ("You love apples!")
	elif fruitinput != "apple":
		print("OOPS!, you dont like that")


