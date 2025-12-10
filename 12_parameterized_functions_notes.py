def get_initial (name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

#we gave the function two parameters, name and force_uppercase

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name, False)

#we must list the parameters in the same order as the function definition
print('Your first name initial is:', first_name_initial)

#*******************************************************************************

#we could have written the code with using default parameters like this:
def get_initial (name, force_uppercase= True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

#the force_uppercase= True points to the default value of the parameter

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)
#we did not need to specify the second parameter since it has a default value

print('Your first name initial is:', first_name_initial)

#*******************************************************************************


# #You can also assign the values to parameters by name when you call the function
def get_initial (name, force_uppercase= True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(force_uppercase = True, \
                                 name = first_name) 
# #when you used named parameters, we can specify parameters in any order

print('Your first name initial is:', first_name_initial)



#*******************************************************************************

#working with multiple parameters and default values
#using named notation will make your code more readable

# Parameters:
#   error_code: Unique error code assigned to each type of error: e.g. 45 is datatype conversion error
#   error_severity: 0 - fatal error should never occur
#                   1 - severe error code cannot continue
#                   2 - warning code can continue but may be missing information in records
#   log_to_db: Should this error be logged to the database 
#   error_message: Error message to display to user and write to database
#   source_module: Name of the python module that generated the error

def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('It looks like an error occurred' + error_message)

first_number = 10
second_number = 5

# if first_number > second_number:
#     error_logger(45,1,True,'First number is greater than second number','adding_method')

#using like this is hard to read and understand what each parameter means
#we can use named parameters to make it more readable
#like this:

if first_number > second_number:
    error_logger(error_code=45, 
                 error_severity=1, 
                 log_to_db=True, 
                 error_message=' First number is greater than second number', 
                 source_module='adding_method')