# copying a list

myfoods=['pizza', 'falafel', 'carrot cake']
friendfoods = myfoods[:]

#adding diff foods to each list

myfoods.append('cannoli')
friendfoods.append('ice cream')


print("My favorite foods are:")
for food1 in myfoods:
	print(food1.title())


print("\nMy friend's favorite foods are:")
for food2 in friendfoods:
	print(food2.title())
	


