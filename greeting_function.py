# Greeting function
def greetusers(names):
	"""print a simple greeting to each user in the list"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']