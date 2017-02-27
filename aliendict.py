# Dictionaries (collection of key-value pairs)

# alien_0 = {'color':'green', 'points':'5'}

# print(alien_0['color'])
# print(alien_0['points'])

# newPoints = alien_0['points']
# print("You just earned " + str(newPoints) + " points!")

# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

#------

# alien0 = {}

# alien0['color'] = 'green'
# alien0['points'] = 5

# print(alien0)

# alien0['color'] = 'yellow'
# print("Now the alien is " + alien0['color'] + ".")

#----changing value in dictionary

# alien1 = {'xposition':0, 'yposition':25, 'speed':'medium'}
# print("Original x-position: " + str(alien1['xposition']))

#Move the alien to the right.
#Determine how far to move the alien based on it's current
#speed...

# if alien1['speed'] == 'slow':
# 	x_increment = 1
# elif alien1['speed'] == 'medium':
# 	x_increment = 2
# else:
# 	# this must be a fast alien. 
# 	x_increment = 3

# the new position is the old position plus the increment.

# alien1['xposition'] = alien1['xposition'] + x_increment

# print("New x-position: " + str(alien1['xposition']))

#---- deleting key-value pair

alien2 = {'color':'blue', 'points': 5}
print(alien2)

del alien2['points']
print(alien2)




