#3-4

guests = ['Michael Jordan', 'Dale Earnhardt', 'Abe Vigoda']
msg = ", would you like to come to dinner?"
cant = " can't make it."
still = " is still coming."
confirmed = " is confirmed coming through."
dots = "..."

print('Hey ' + guests[0] + msg)
print('Hey ' + guests[1] + msg)
print('Hey ' + guests[2] + msg)
print(dots)

#3-5

print('Unfortunately, ' + guests[2] + cant)
notcoming = 'Abe Vigoda'
guests.remove(notcoming)
print(guests[0] + still)
print(guests[1] + still)
print(dots)

#3-6

print('Aw shit, more people are coming. Good thing we fond another table.')

guests.insert(0, 'Bill Pullman')
guests.insert(2, 'Dean Martin')
guests.append('Trevor Gillies')
print(guests[0] + confirmed)
print(guests[1] + confirmed)
print(guests[2] + confirmed)
print(guests[3] + confirmed)
print(guests[4] + confirmed)
print(dots)

#3-7

print("Looks like I'm only allowed to invite 2 people.")
firstuninvite = guests.pop(0)
beatit = ', you can beat it.'
print(firstuninvite + beatit)

seconduninvite = guests.pop(0)
print(seconduninvite + beatit)

thirduninvite = guests.pop(0)
print(thirduninvite + beatit)

invite1 = guests.pop(0)
print(invite1 + still)

invite2 = guests.pop(0)
print(invite2 + still)

print(guests)






