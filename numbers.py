#numbers ch 4

dots = "..."

for value in range(1,6):
	print(value)

print(dots)

# range in a list

numbers = list(range(1,6))
print numbers

print(dots)

# even numbers

evennum = list(range(2,11,2))
print(evennum)

print(dots)

# squares

squares = []
for val in range(1,11):
	#square = val**2
	#squares.append(square)
	squares.append(val**2)

print(squares)

print(dots)

#min, max, sum

digits = range(0,10)
print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))

print(dots)

squares = [val**2 for val in range(1,11)]
print(squares)



