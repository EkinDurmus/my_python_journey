from datetime import datetime, timedelta 

#today's date function
current_date = datetime.now()
print("Today is:" + str(current_date))

#yesterday's date function
one_day = timedelta(days=1)
yesterday = current_date - one_day
print("Yesterday was:" + str(yesterday))

#ask user for a date input
input_date = input("Please enter a date (DD/MM/YYYY):")
input_date = datetime.strptime(input_date, "%d/%m/%Y")
print("You entered: " + str(input_date))

#calculate date one week from current date input
one_week = timedelta(weeks=1)
week_after = input_date + one_week
print("The date after one week is:" + str(week_after))