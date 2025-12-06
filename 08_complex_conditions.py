#code challenge - my mission is:
# When you join a hockey team you get your name on the back of the jersey
# but the jersey may not be big enough to hold all the letters
# Ask the user for their first name
# Ask the user for their last name

# if first name is < 10 characters and last name is < 10 characters 
#       print first and last name on the jersey
# if first name >= 10 characters long and last name is < 10 characters
#       print first initial of first name and the entire last name
# if first name < 10 characters long and last name is >= 10 characters
#       print entire first name and first initial of last name
# if first name >= 10 characters long and last name is >= 10 characters
#       print last name only

# Test with the following values
# first name: Susan  last name: Ibach
# output: Susan Ibach
# first name: Susan  last name: ReallyLongLastName
# output: Susan R.
# first name: ReallyLongFirstName  last name: Ibach
# output: R. Ibach
# first name: ReallyLongFirstName  last name: ReallyLongLastName
# output: ReallyLongLastName

first_name = input ("Enter your first name: ").capitalize()
last_name = input ("Enter your last name:").capitalize()

# if len(first_name)< 10 and len(last_name) < 10:
#     print(first_name + " " + last_name)
# elif len(first_name) >= 10 and len(last_name) < 10:
#     print(first_name[0] + "." + last_name)
# elif len(first_name) < 10 and len(last_name) >= 10:
#     print(first_name + " " + last_name[0] + ".")
# elif len(first_name) >= 10 and len(last_name) >= 10:
#     print(last_name)
# else:
#     print("Unexpected input, please check the names entered.")

if len(first_name) >= 10:
    long_first_name = True
else:
    long_first_name = False

if len(last_name) >= 10:
    long_last_name = True
else:
    long_last_name = False

if not long_first_name and not long_last_name:
    print(first_name + " " + last_name)
elif long_first_name and not long_last_name:
    print(first_name[0] + ". " + last_name)
elif not long_first_name and long_last_name:
    print(first_name + " " + last_name[0] + ".")
elif long_first_name and long_last_name:
    print(last_name)