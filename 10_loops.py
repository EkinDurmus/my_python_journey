for name in ['Ekin', 'Berna']:
	print(name)
	
for index in range(0, 2):
	print(index)
#range function is used for looping a specific number of times
#it generates a sequence of numbers
#we can also write it as [0,1]

names = ['Ekin', 'Berna']
index = 0
while index < len(names):
	print(names[index])
	#We must change the condition!!!!!
	#if we don't change the condition it will be an infinite loop
	index = index + 1
	
#The while loop example above is equivalent to the for loop example.
#but commonly we choose 'for loop' when we know how many times we want to loop
#and we use 'while loop' when we don't know how many times we want to loop
#for example when we want to loop until user types 'exit'
#like input validation
#the user might enter invalid inputs many times
#so we don't know how many times we will loop