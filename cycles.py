#cycles
dots = "..."

cycles = ['honda', 'yamaha', 'suzuki']
print(cycles)
print(dots)

cycles[0] = 'ducati'
print(cycles)
print(dots)

cycles[0] = 'honda'
print(cycles)

cycles.append('ducati')
print(cycles)
print(dots)

motolist = []
motolist.append('honda')
motolist.append('yamaha')
motolist.append('suzuki')
print(motolist)
print(dots)

cycles.insert(0, 'ninja')
print(cycles)
print(dots)

print(cycles)
del cycles[0]
print(cycles)
print(dots)

cycles.insert(0, 'ninja')
print(cycles)
del cycles[1]
print(cycles)
print(dots)

cycles.insert(1, 'honda')
print(cycles)

popped_cycles = cycles.pop()
print(cycles)
print(popped_cycles)
print(dots)

cycles2 = ['honda', 'yamaha', 'suzuki']
first_owned = cycles2.pop(0)
print("The 1st motocycle I owned was a " + first_owned.title() + ".")
print(dots)

cycles2.insert(0, 'honda')
print(cycles2)
cycles2.remove('honda')
print(cycles2)
print(dots)

cycles3 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(cycles3)

too_expensive = 'ducati'
cycles3.remove(too_expensive)
print(cycles3)
print("\nA " + too_expensive.title() + " is too expensive for me.")
print(dots)


