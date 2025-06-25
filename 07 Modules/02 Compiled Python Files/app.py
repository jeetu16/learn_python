from sales import calc_shipping, calc_tax
import sales  # another way to import the module
sales.calc_shipping()
# above both the way is same it has not performance issue. when we import one or more objects from the module it loads entire modules.

# from sales import *   # don't do this only import required data from the modules. because it can override the exiting methods and properties.

calc_shipping()
calc_tax()
