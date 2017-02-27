#4-10 


# copying a list
dots = "..."
myfoods=['pizza', 'falafel', 'carrot cake', ]
friendfoods = myfoods[:]

#adding diff foods to each list

myfoods.append('cannoli')
friendfoods.append('ice cream')


print("My favorite foods are:")
print(myfoods)

print("\nMy friend's favorite foods are:")
print(friendfoods)

print(dots)

#should be pizza, falafel, carrot cake
print("The first 3 items in the list are:")
print(myfoods[:3])

#should be falafel,carrot cake
print("\n2 items from the middle of the list are:")
print(myfoods[1:3])

#shoul be falafel, carrot cake, and cannoli

print("\nLast 3 items on the list are:")
print(myfoods[1:])

print(dots)





