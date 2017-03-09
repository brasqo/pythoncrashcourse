# --> 8-15 printing models.
import printing_functions as pf
#need to define before calling the functions via module.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#calling both functions(print_models & show_completed_models)
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
