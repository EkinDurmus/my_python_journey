#if we want to calculate the tax
price = input("Please enter the price:")

#then we need to convert the string to a number
price = float(price)

#lets's we say anything purchased for more than $1.00 is charged a 7% tax
#so we need to check if the price is greater than 1.00
if price >= 1.00:
    # Everything over $1.00 is charged 7% tax
    tax = .07 
    print("The tax rate is:" + str(tax))

#python is a case sensitive language
country = input("Please enter the country you are in:")
#if country == "turkey":
#This is incorrect because of Python's case sensitivity
if country.lower() == "turkey":
    print("Merhaba!")
else:
    print("You're not from Turkey")

#code challenge - my mission is:
# Fix the mistakes in this code and test based on the description below
# If I enter 2.00 I should see the message "Tax rate is: 0.07" 
# If I enter 1.00 I should see the message "Tax rate is: 0.07" 
# If I enter 0.50 I should see the message "Tax rate is: 0" 

price = input('how much did you pay? ')
#We need to convert to float
price = float(price)

if price > 1.00:
#We need to see if we enter 1.00, so we need to use >=      
	tax = .07
	print('Tax rate is: ' + str(tax))
#this line is correct
else
#if we use condtionals we need to use colon at the end of the line
	tax = 0
print('Tax rate is: ' + str(tax))