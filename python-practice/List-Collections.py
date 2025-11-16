#collection of element
#Ordered(created list order will be maintained), Changable(Item elements can change),Allows Duplicates, List can have items that are of different data types
# count(elements-occuring),reverse(), sort(),copy(duplicate existing list and stres in different m/y address), index(element first occurence position)
# empty_list_define = []
# List Accesing- using index and negative index, slice(start:stop:step(jump))-split the list as small chunks. list_name(1,5,1) start from 1 end before 5, each element.reverse_slice(-5,-1,1)
# Add new items - use index, append(), insert(index-postion, element),
# Remove the old Items- pop(index-no or last-element),remove(removes specific value if index unknown), clear(to empty the list values),del keyword(remove complete list object)
# Looping in List - in , len(), range(index based), enumerate(index with values)
# Joining the lists: +,append(join as nested list),extend(merge-list), constructor(just provide values to initiate the object)
# List Comprehension(purithal): Syntax: Start-Expression(what operation) for-loop End-condition
#Nested list(Matrix):matrix1=[[0,1],[2,3]]
"""
append()	Adds an element at the end of the list #Syntax: list.append(elmnt)
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable[(list, set, tuple, etc.)]), to the end of the current list
index()	Returns the index of the first element with the specified value. #syntax: list.index(elmnt, start, end) #Note: The index() method only returns the first occurrence of the value.
insert()	Adds an element at the specified position #syntax: list.insert(index-position, elmnt)
pop()	Removes the element at the specified position #Note: The pop() method returns removed value.
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list 
sort()	Sorts the list  # syntax: list.sort(reverse=True|False, key=myFunc).sorts ascending by default.

"""
#1.Add an element to the fruits list:
""" fruits = ['apple', 'banana', 'cherry']
fruits.append('kiwi')
print(fruits)
 """
#2.Add a list to a list:
""" a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a) """

#3. Copy the fruits list:
""" fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x) """

#4.Add the elements of cars to the fruits list:
""" fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits) """

#5.What is the position of the value "cherry":
""" fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x) """

#6.ind the postion of 'cherry', but start the search at position 4:
""" fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
x = fruits.index("cherry", 4)
print(x) """

#7.Add the value "orange" as the second element of the fruit list:
""" fruits = ['apple', 'banana', 'cherry']
fruits.insert(1,'orange')
print(fruits) """

#8. Return the number of times the value 9 appears int the list:
""" points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x =points.count(9)
print(x) """

#9.Remove the second element of the fruit list:
""" fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
x = fruits.pop(2)
print(x)
print(fruits) """

#10. Remove the "banana" element of the fruit list without using index value:
""" fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits) """

#11.Reverse the order of the fruit list:
""" fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
print(fruits) """

#12.Sort the list alphabetically:
""" cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars) """
#cars.sort(reverse=True)

#13.Sort the list by the length of the values:
# A function that returns the length of the value:
""" def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
print(cars) """

#Sort a list of dictionaries based on the "year" value of the dictionaries:
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)