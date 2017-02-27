#--> 7-1 rental car
# car = input("What kind of car would you like to rent?: ")
# print("Let me see if we have a " + car + " to rent.")

# -- > 7-2 restaurant seating
# group = input("How many people are in your group?: ")
# group = int(group)

# if group > 8:
# 	print("\nThat's alot of people, you need to wait a few.")
# else:
# 	print("\nNo problem, your table awaits.")

#-- > 7-3 multiples of ten
num = input("Enter a number and I'll tell you if it's a multiple of 10: ")

if int(num) % 10 == 0:
	print("\n" + str(num) + " is a multiple of 10!")
else:
	print("\nNOPE! " + str(num) + " is NOT a multiple of 10!")


