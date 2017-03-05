#confirmed users

# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmedusers = ['alice', 'brian', 'candace']
confirmedusers = []

# verify each user until there are no more unconfirmed users.
# move each verified user into the list of confirmed users.

while unconfirmedusers:
	currentuser = unconfirmedusers.pop()

	print("Verifying user: " + currentuser.title())
	confirmedusers.append(currentuser)

#display all confimred users
print("\nThe following users have been confirmed:")
for confirmeduser in confirmedusers:
	print(confirmeduser.title())

