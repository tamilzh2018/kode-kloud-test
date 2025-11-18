# We cannot set our own index value for list and tuple elements, but we can set our own index value for each element in a dictionary. That's "Key".
# Ordered, Changable(values can change), Duplicates not Allowed because accessing bu keys if its there it will overwrite the exisitng value, Index starts from zero.
# Dictionary are key:value pair,Accessing dict is Using keys, values, like .key(), .values(), .items(provide keys:value pair tuple), .get(key)-to access specific value without throw error
# Add new items: use dictname[key]=value, .update(update/add specified key:value), 
# Remove old Items: pop(removes specific key), popitem(removes last insreted pairs),del keyword,pop(), clear()
# empty_dict_define = {}
# count(), copy(), reverse(), sort()
# Dictionary looping: keys(), values(), items()
# Nested Dcit: ex:json file

"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary 

"""
# List as dictionary
""" food = ["idli", "dosai", "rice", "parota", "puri"]
numbers = [1,2,3,4,5,3,6,7,8,9,0] #even if u have extra values then "keys" dict will not assign keys for that values simply it ommits the values
print(dict(zip(food, numbers)))  """
# Tuple as dictionary
""" a = ('happy', 'learning', 'python')
b = (1, 2, 3, 4)
print(dict(zip(a, b))) """
# dict function
""" a = dict([('express', 'happy'), ('learning','book'), ('python','langauge')])  #convert list and tuple as dict
print(a) """
# Basic Operation in Dictionary
# 1.Find the length
""" a= {'express': 'happy', 'learning': 'book', 'python': 'langauge'}
print(len(a)) """
# 2.Concatenation (takes only two varaibles) : dict+dict not allowed
# 3.Repetition(takes one variable and integer)dict*int not allowed
# 4.Membership operator
""" a= {'express': 'happy', 'learning': 'book', 'python': 'langauge'}
print( 'express' in a) # Check with key
print( 'express' not in a) # Check with key """
# 5. Accessing dictionary elements
a = {'express': 'happy', 'learning': 'book', 'python': 'langauge'}
print(a ['express'])