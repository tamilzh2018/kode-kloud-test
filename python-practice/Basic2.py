#How to Find HCF(Highest Common Factor) or GCD – (Greatest Common Divisor) of a Number 
#Division Method (Euclid’s Method) Find HCF of 48 and 18 ==> high/low=remainder1 then low/remainder1=remainder2 then remainder1/remainder2 ...
""" high = int(input("Enter Hiogh value Number: "))
low = int(input("Enter Low value Number: "))
while low != 0:
    high, low = low, high%low
print(high) """
    
#How to Find LCM(least common multiplier) of a Number LCM(a,b)=a×b/GCD(a,b)
""" high = int(input("Enter Hiogh value Number: "))
low = int(input("Enter Low value Number: "))
mul=(high*low)
while low != 0:
    high, low = low, high%low
print("Greatest Common Divisor of given number: ",high)
lcm=mul/high
print("least common multiplier of given number: ",lcm) """
# How to Find Profit or Loss Calculation Cost Price (CP):Selling Price (SP) If SP > CP, then profit else loss
# Profit=SP−CP or Loss=CP−SP Profit%=(Profit/CP)*100, Loss%=(Loss/CP)*100
""" cp=int(input("Enter cost price of the things: "))
sp=int(input("Enter your selling price of the things: "))

if sp>cp:
    print("Profit from the product")
else:
    print("Loss from the product")
 """
# How to Find Factors of a Number: Numbers that divide by increasing numbers it exactly (without leaving a remainder).
""" factor = int(input("Enter the number to find factors: "))
factor_list = []
counter = 1

while counter <= factor:
    if factor % counter == 0:
        factor_list.append(counter)
    counter = counter + 1
#for loop
for i in range(1,factor+1):
        if factor % i == 0:
            factor_list.append(i)
print("Given number's factors are:", factor_list)
 """
# How to Find Simple Interest (SI)= (P-Principal×R-Rate of interest per year×T-Time (in years))/100, A(total)=P+SI
""" p=int(input("Prinicpal Amount: "))
r=float(input("Interest Rate: "))
t=float(input("Term of Years: : "))

si=(p*r*t)/100
a= p+si

print("Simple interest value: ",si)
print("Total amount with interest: ",a) """
# How to Find Compound Interest (CI)
# Formula: CI = A - P, where A = P * (1 + R/100) ** T

""" p = float(input("Principal Amount: "))
r = float(input("Interest Rate (%): "))
t = float(input("Term in Years: "))

n = r / 100
a = p * (1 + n) ** t
ci = a - p

print("Compound Interest Value:", ci)
print("Total Amount with Interest:", a) """

# How to Perform String Conversions lower to upper vice versa
""" string1="enter the number"
print(string1.upper())
string2="ENTER THE NUMBER"
print(string2.lower())
char=input("Enter a character: ")
if char.islower():
    print("the character is lower ")
elif char.isupper(): 
    print("the character is upper ")
else:
    print("it is not a character") """
# How to Randomly Select an Element and mulitple elements from a List 
""" import random
import secrets
list1=['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry', 4, 2, 9, 7, 8, 9, 3, 1]
print("Randomly selected an element from random module: ", random.choice(list1))
print("Randomly selected an element from secret module: ", secrets.choice(list1))
for mul in range(3):
    print("Randomly selected 3 elements from random module: ", random.choice(list1))
    print("Randomly selected 3 elements from secret module: ", secrets.choice(list1)) """

#How to Remove Duplicates From a List
""" points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
without_dupe= set(points)
print("No duplicate list: ",without_dupe) """
#How to Copy a File
""" import shutil
from shutil import copyfile, copyfileobj
#Copies the contents of the file  not metadata(permission,timestamps). syntax: shutil.copy("source.txt", "destination.txt")
shutil.copy("D:/Devops/kode-kloud-test/python-practice/create_new.txt","D:/Devops/kode-kloud-test/python-practice/create_copy.txt")
shutil.copy2() #Copies the file with metadata.
shutil.copytree("source_folder", "destination_folder") #to copy the entire folder
copyfile("source.txt", "destination.txt")
copyfileobj("source.txt", "destination.txt") """

#How to use List Methods
""" fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
points = [156, 4, 2, 99, 72, 8, 89, 3, 19]
#length
print("Length of the list: ",len(fruits))
 """
""" num_of_student=int(input("Enter number of student in the class: "))
student_list=[]

for marks in range(1,num_of_student+1):
    student_list.append(int(input(f"Enter student {marks} marks: ")))
print(f"Total students: {num_of_student} maximum marks secured: {max(student_list)} and Minimum marks secured: {min(student_list)}") """
    
#How To Find Anagram :-checking whether two words (or 2 strings) contain the same letters andsame length in any order(but letter arrangemnet varies). 
# ex: listen ↔ silent,night ↔ thing,evil ↔ vile,dusty ↔ study
""" word1 = input("Enter the first word: ")
word2 = input("Enter the Second word: ")
if sorted(word1.lower()) == sorted(word2.lower()): #sort in ascending order and compare
    print("Both words are Anagram")
else:
    print("Both words are not Anagram")

#another method: import counter
from collections import Counter
if Counter(word1.lower()) == Counter(word2.lower()):
     print("Both words are Anagram")
else:
    print("Both words are not Anagram")   """
# How To Find Valid Date(dd/mm/yyyy):-Day(1-31),Month(1-12),Year(>0),Leap year rules are applied for February
""" day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

# Check year
if year < 1:
    print("invalid year")

# Check month
elif month < 1 or month > 12:
    print("invalid month")

else:
    # Determine max days in month
    if month in (1, 3, 5, 7, 8, 10, 12):
        max_days = 31
    elif month in (4, 6, 9, 11):
        max_days = 30
    else:  # February
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_days = 29
        else:
            max_days = 28

    # Validate day
    if day < 1 or day > max_days:
        print("invalid day")
    else:
        print("valid date") """

# How to find second largest Number:Sort the list in descending order and Pick the second element.
""" nums = [100, 340, 50, 79, 28, 160, 412, 340, 120, 100, 340]
n = int(input("Enter the nth largest number to check: "))

unique_nums = sorted(set(nums), reverse=True)
nth_largest = unique_nums[n-1] #indexing

print(f"{n}th largest number is {nth_largest}") """

# How to Perform String Concatenation
str1= "valid date"
str2="or invalid date"
print("concatenation of strings:", str1+ " "+str2)
print(" ".join([str1,str2]))
# How to Replace a Character in a String
""" txt = "I like bananas"
print(txt.replace('an','on'))
 """
# How to Count Number of Words in a Sentence:Split the sentence by spaces and Count each separated part.
""" count_str="Enter the nth largest number to check"
print("Number of words: ", len(count_str.split()))
total=0
for count_words in count_str.split():
    total+=1
print("Number of words: ", total)
 """
# How to toggle(converting) Character Case
""" toggle="enter the nth largest number to check"
print("First letter in capital: ", toggle.capitalize())
print("Each words first latter in capital: ", toggle.title())
print("if string is in small letter then change to capital: ", toggle.swapcase()) """
# How to Perform List Concatenation 
# How to Access Index Value of List Elements
# How to Merge Dictionaries
# How to Access Dictionary Key and Values 
# How to convert List into Dictionary
# How to Flatten Nested List  