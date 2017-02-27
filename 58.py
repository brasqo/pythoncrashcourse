# 5-8 Hello admin

# usernames = ['danny', 'jacob', 'admin', 'billy', 'fran']

# for username in usernames:
# 	if username != 'admin':
# 		print("Welcome back " + username.title() + ".")
# 	else:
# 		print("Hello Admin!")

#------> 5-9 accomidating an else for an empty list

# usernames = []


# if usernames:
# 	for username in usernames:
# 		if username != 'admin':
# 			print("Welcome back " + username.title() + ".")
# 		elif username == 'admin':
# 			print("Hello Admin!")
# else:
# 	print("Oops!, The list is empty")


#---> 5-10

# currentusers = ['danny', 'jacob', 'rob', 'billy', 'fran']
# newusers = ['danny', 'jacob', 'ben', 'bob', 'neil', 'FRAN']

# for newuser in newusers:
# 	if newuser.lower() in currentusers:
# 		print("Sorry, " + newuser + " is taken. Pick a new name.")
# 	else:
# 		print("Good news! " + newuser + " is an available name.")

#---> 5-11 Ordinal numbers

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#print(nums)

for num in nums:
	if num == '1':
		print(str(num) + "st")
	elif num == '2':
		print(str(num) + "nd")
	elif num == '3':
		print(str(num) + "rd")
	else:
		print(str(num) + "th")


