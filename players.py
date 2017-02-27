#players

dots = "..."

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(dots)

print(players[1:4])

print(dots)

print(players[:4])

print(dots)

print(players[2:])

print(dots)

print(players[-3:])

print(dots)

#looping thru a slice

print('Here are the first 3 players on my team:')
for player in players[:3]:
	print(player.title())
	


