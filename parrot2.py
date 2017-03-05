#--> parrot.py (letting user determine when to quit)

# prompt = "\nTell me something and i'll repeat..."
# prompt += "\nEnter 'quit' to end the program...: "

# message = ""
# while message != 'quit':
# 	message = input(prompt)
	
# 	if message != 'quit':
# 		print(message)

#--> utilizing flags

prompt = "\nTell me something and i'll repeat..."
prompt += "\nEnter 'quit' to end the program...: "

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)
