# --> 8-16 imports

import greeting_function

usernames = ['hannah', 'ty', 'margot']

greeting_function.greetusers(usernames)

print("...")

#----
from greeting_function import greetusers

greetusers(usernames)

print("...")

#----
from greeting_function import greetusers as gu

gu(usernames)

print("...")

#---
import greeting_function as gf

gf.greetusers(usernames)

print("...")

#---
from greeting_function import *

greetusers(usernames)
