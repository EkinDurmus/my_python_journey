country = input("What country do you live in? ")
if country.lower() == "canada":
    province = input("Which province/state do you live in? ").capitalize()
    if province in("Alberta", \
                   "Nunavut", "Yukon"):
#we can use nested if statements to handle multiple conditions
#and with using "IN" we can check for multiple values in a single condition 
                   tax = 0.05
    elif province == "Ontario":
            #elif means "else if"
            #elif statements are used to check for multiple conditions 
            tax = 0.13
    else:
            tax = 0.15
else:
    tax = 0.0
print(tax)   



# code challenge - my mission is:
# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z

first_name = input("What is your first name?")

if first_name[0].upper() in ("A", "B"):
    print("You should go to room AB")
elif first_name[0].upper() == "C":
    print("You should go to room C")
else:
    last_name = input("What is your last name?")
    if last_name[0].upper() == "Z":
        print("You should go to room Z")
    else:
    #if first_name[0].upper() not in ("A","B","C") or last_name[0].upper() == "Z" :
        print("You should go to room OTHER")  