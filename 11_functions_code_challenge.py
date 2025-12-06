#Code challenge -- My mission is:
# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function with the values 6,4, add 
# Should return 10
#
# Test your function with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received

def calculator(first_number, second_number, operation):
    if operation.upper() == 'ADD' or operation == '+':
        return first_number + second_number
    elif operation.upper() == 'SUBTRACT' or operation == '-':
        return first_number - second_number
    else:
        return "Error: Invalid operation. Please use 'add' or 'subtract'."
    
first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')
operation = input("Enter the operation ('add' or 'subtract'): ")
result = calculator(float(first_number), float(second_number), operation)
print("The result is:", result)