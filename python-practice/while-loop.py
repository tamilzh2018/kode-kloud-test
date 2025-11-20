#Use when number of iteration is unknown
#With the while loop we can execute a set of statements as long as a condition is true.
#Note: remember to increment/decrement counter ex:num, or else the loop will continue forever.
# Syntax: counter(initial value), while (runs until given condition is true), increment/decrement
#1. Print a number from 1 to 5 using while loop
""" num = 1
while (num <= 5):
    print(num)
    num= num+1
 """
#2. Write a loop statement to print the following series. 10, 20,30 ...200
""" num = 10
while (num <= 200):
    print(num, end=" ")
    num = num +10 """
#3. Write a program to print first 10 natural numbers in reverse order
""" nat_num = 10
while (nat_num > 0):
    print(nat_num)
    nat_num =nat_num -1 """

#4. Write a program to find the factorial of a number
""" i = 3
fact = 1
while i > 0:
    fact = fact * i
    i = i-1
print(fact) """

#With the 'break' statement we can stop the loop even if the while condition is true: 
#5. Exit the loop when i is 3:
""" i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 """

#6.With the continue statement we can stop the current iteration, and continue with the next:
#Continue to the next iteration if i is 3:
""" i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) """

#With the else statement we can run a block of code once when the condition no longer is true:
#Print a message once the condition is false:
""" i = 1
while i < 6:
  print(i) 
  i += 1
else:
  print("i is no longer less than 6") """

#Nested While
i = 1
j = 3
while i < 6:
  while j < 8:
    print(i,j)
    i += 1
    j = j+1
    