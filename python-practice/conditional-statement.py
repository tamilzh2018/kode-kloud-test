#If Condition met do this else do that
#1. Get user input for Variable mark, if mark> 35 then print Pass  else print Fail
""" mark = int(input("Enter your mark: "))

if (mark > 35):
    print("Pass")
else:
    print("Fail") """

#2. Get input for a number and check whether it is divisible by both 3 and 5 or not. If yes then print,
# the number is divisible by 3 and 5 else print the number is not divisible by 3 and 5.
""" number = int(input("Enter a Number: "))

if (number % 3 == 0 and number % 5 == 0):
    print("Given Number is Divisble by 3 and 5")
else:
    print("Given Number is not Divisible by 3 and 5") """

#3. Get input for a number and find it is even or odd
""" number = int(input("Enter a number: "))

if (number % 2 == 0):
    print("Even Number")
else: 
    print("Odd Number") """
#4. Get input for score out of 100, if score is <= 35 "Poor Student", if score > 35 but < 70 "Average Stundent"
# if score is > 70 "Good Student".
score = int(input("Enter your mark: "))

if (score <= 35):
    print("Poor Student")
elif (score > 35 and score <= 70):
    print("Average Student")
else:
    print("Good Student")