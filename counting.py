#--> counting - intro to while loops

# currentnum = 1
# while currentnum <= 5:
# 	print(currentnum)
# 	currentnum += 1

# Counting - using continue in loop

currentnumber = 0
while currentnumber < 10:
	currentnumber += 1
	if currentnumber % 2 == 0:
		continue

	print(currentnumber)


