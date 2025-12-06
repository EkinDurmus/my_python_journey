from datetime import datetime 
#print timestamps after each section of code
# see how long sections of code take to run

first_name = 'Ekin'
print('task completed')
print(datetime.now())
# print(datetime.datetime.now())
#if we had simply written 'import datetime', we would have to use 'datetime.datetime.now()
print()

for x in range(0,10):
    print(x)
print('task completed')
print(datetime.now())
print()

#************************************************************************************************
#By moving the code to a function, you reduce rework and
#the change of introducing bugs when you change the code you had copied

from datetime import datetime
def print_time():
    print('task completed')
    print(datetime.now())
    print()

first_name = 'Ekin'
print(first_name)
print_time()
# By defining a function (def), we can reuse the 'print_time' logic in multiple places.
# This prevents code repetition and makes updates easier


#************************************************************************************************
#parameters
from datetime import datetime
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()
#task_name is a parameter
#parameters act as variables/placeholder for functions

first_name = 'Ekin'
print_time('first name assigned')
#with the task_name parameter, we can easily customize the message for each call

for x in range(0,10):
    print(x)
print_time('loop completed')
#thanks to parameters, we can call the function again with different messages

#************************************************************************************************
#from the beginning we write code like this

# first_name = input('Enter your first name: ')
# first_name_initial = first_name[0:1]
# print('Your first name initial is: ' + first_name_initial)

#but we can make it better with functions

def get_initial(name):
    initial = name[0:1].upper()
    return initial

#More readable version
first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)
print('Your initials are: ' + first_name_initial + \
       last_name_initial)

#we might trade readability for less code repetition

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print('Your initials are: ' + \
      get_initial(first_name) + \
       get_initial(last_name))


#Functions make your code more readable and easier to maintain
#We need to always add comments to explain the purpose of functions
#and parameters if their purpose is not obvious
#Functions must be declared before the line of code where the function is called