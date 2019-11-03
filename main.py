import aux_module

# creating InvalidNames file
file = open('InvalidNames.csv', 'w')   
# creating CleanNames file
file = open('CleanNames.csv', 'w')     

# check if we called the right module
try:

    aux_module.main3()
    
except FileNotFoundError:
    print("File not found")
