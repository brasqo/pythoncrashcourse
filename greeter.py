# --> greeter...functions
# Simple use
def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

# -- > example 2 - passing info into a function
print("...")

def greetuser(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")

greetuser('jesse')


