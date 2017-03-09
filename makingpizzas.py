#--> making pizzas, importing pizza1
# 1st approach to importing - 
# module_name.function_name()

import pizza1

pizza1.make_pizza(16, 'pepperoni')
pizza1.make_pizza(12, 'mushrooms', 'green peppers', 'extracheese')

print("...")

# Import a specific function from a module - 
# from module_name import function_name, function_1, etc
# You can import as many functions as wanted.

from pizza1 import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extracheese')

print("...")

#--> Using 'as' to Give a Function an alias
# from module_name import function_name as fn
from pizza1 import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extracheese')


print("...")

#--> Using 'as' to give a module an alias
# import module_name as mn
import pizza1 as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extracheese')

print("...")

# importing all functions in a module.
from pizza1 import *

make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extracheese')
