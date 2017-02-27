#cars

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars1 = ['bmw', 'audi', 'toyota', 'subaru']
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
dots = "..."

cars.sort(reverse=True)
print(cars)
print(dots)

print("Here's the original list:")
print(cars1)

print("\nHere is the sorted list:")
print(sorted(cars1))

print("\nHere's the original list again:")
print(cars1)
print(dots)

print(cars2)
cars2.reverse()
print(cars2)
number = len(cars2)

print("There are " + str(number) + " cars on the list.")



