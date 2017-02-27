#4-3 
dots = "..."

numbers = range(1,21)
for number in numbers:
	print(number)

print(dots)

#4-4 4-5

numberS1 = list(range(1,1000001))
print(min(numberS1))
print(max(numberS1))
print(sum(numberS1))

print(dots)

#4-6

oddnums = list(range(1,21,2))

for oddnum in oddnums:
	print(oddnum)

print(dots)

#4-7

threes = list(range(3,31,3))
for three in threes:
	print(three)

print(dots)


#list comprehension (harder) 4-9
cubes = [cube**3 for cube in range(1,11)]
print(cubes)

print(dots)

#4-8 list
cubeS1 = list(range(1,11))
for cube1 in cubeS1:
	print(cube1**3)


