names = ["Ekin ", "Berna ", "Deniz "]
scores = []
#this creates an empty list called scores
scores.append(85)
#when we use append method, it adds an element to the end of the list
scores.append(90)
scores.append(95)
print(names)
print(scores)

from array import array
#if you want to create an array, you need to import the array module
scores = array('d')
#'d' indicates that the array will hold double (floating point) values
#and 'i' would indicate integer values
#'d' can also be written as "d"; single or double quotes **are interchangeable
scores.append(93)
scores.append(94)
print(scores)
print(scores[1])
#normally indexes start from 0, so scores[1] will give you the second element in the array
#arrays have type code, so you cannot mix different types of data in the same array
#for example, you cannot add a string to an array of doubles

#differences between lists and arrays
#lists can store anything and store any type of data
#arrays are more efficient in terms of memory and performance when dealing with large amounts of numerical data
#but arrays are numerical data types only and must all be of the same type

#common operations
names = ["Ekin ", "Berna "]
print(len(names))
#len function gives you the number of elements in the list
names.insert(0, "Deniz ")
#insert method allows you to add an element at a specific position in the list
print(names)
names.sort()
#sort method sorts the elements of the list in ascending order
print(names)

#retrieving elements
names = ["Ekin ", "Berna ", "Deniz "]
learners = names[0:2]
#this function retrieves elements from index 0 to index 2 (excluding index 2)
print(learners)
#also this can be used like [:2]
#this means from the beginning to index 2 (excluding index 2)
#and [1:] means from index 1 to the end of the list

#dictionaries
person = {"first": "Ekin"}
person["last"] = "Durmuş"
print(person)
print(person["first"])
#dictionaries are collections of key-value pairs
#you can add new key-value pairs by assigning a value to a new key

#differences between lists and dictionaries
#lists are zero-based index collections and storage order guaranteed
#dictionaries are key-value pairs and storage order is not guaranteed (until Python 3.7)
#after Python 3.7, dictionaries maintain insertion order
#we can trust their order in modern Python versions
#but we must not forget the equality comparison
#lists are equal if their elements are equal and in the same order
#but if you change the order of lists, they are not equal anymore
#dictionaries are equal if they have the same key-value pairs, regardless of the order