#1. Get input for variable name, age and address.Print it.
""" name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
print(f"Name: {name}, Age: {age}, Address: {address}") """

#2. Get two numbers from user and print their sum, difference, product and division.
""" num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
def add(num1, num2):
    reterms num1 + num2

def sub(num1, num2):
    reterms num1 - num2

def mul(num1, num2):
    reterms num1 * num2

def div(num1, num2):
    reterms num1 / num2

def mod(num1, num2):
    reterms num1 % num2

def flor(num1, num2):
    reterms num1 // num2

add = add(num1, num2)
sub = sub(num1, num2)
mul = mul(num1, num2)
div = div(num1, num2)
mod = mod(num1, num2)
flor = flor(num1, num2)

print(f"Addition value: {add}, Subtraction value: {sub}, Mulitiplication vlaue: {mul}, Division value: {div}, Modulus value: {mod}, floor division value: {flor}") """

# Get Input for Variable name, score, department
# Get score for 100
# Divide 100/10
""" name = input("Enter your Name: ")
score = int(input("Enter your score: "))
department = input("Which Department from: ")

def div():
    reterms score/10
div = div()
print(f"Name: {name}, Score: {div}/10, Department: {department}")   """

#1. How to find a number is postive or not
""" num = int(input("Enter a number: "))
if num>0:
    print('Entered Number is Positve Number: ', num)
else:
    print("Entered Number is Negative Number: ", num) """

#2. Find Odd or Even Numbers in Range of Numbers
""" start=int(input("Enter the starting number: "))
stop=int(input("Enter the Ending Number: "))
for i in range(start, stop+1):
    if (i%2==0):
        print("Entered Number is Even: ",i)
    else:
        print("Entered Number is Odd: ",i) """
#3. Identifying Vowels
""" vowels='aeiouAEIOU'
identify = input("Enter an alphabet: ")

if not identify.isalpha():
    print("Numbers not allowed")      
elif len(identify) != 1:
    print("Please enter a single alphabet character.")
else:
    if identify in vowels:
        print("vowel character")
    else:
        print("consonant character")
 """

""" ch = input("Enter a char:")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print(ch, 'is vowels')
else:
    print(ch, 'is not vowels') """

# finding given character is alphabet or not
""" identify = input("Enter an alphabet: ")

if identify.isalpha():
    print(identify, "is an alphabet")
elif identify.isdigit():
    print("Numbers not allowed. Enter only alphabet.")
else:
    print("Symbols not allowed. Enter only alphabet.") """

#Finding Average of N Numbers
""" num = int(input('Enter the numbers to find avg: '))
list1 = []

for i in range(1, num + 1):
    list1.append(int(input(f"Enter your {i} number: ")))

avg = sum(list1) / num
print("Average:", avg) """

#print all numbers in a range that are divisible by given number
""" start = int(input("Enter the starting Number: "))
stop = int(input("Enter the ending Number: "))
division_num = int(input("Enter the Number to be Divided: "))
for i in range(start, stop+1):
    if (i%division_num)==0:
        print("Divisible numbers is: ", i) """
# Finding a Grade of a Student
""" subjects=int(input("Enter number of Subjects: "))
sub_list=[]

for sub in range(subjects):
    sub_list.append(int(input(f"Enter the subject {sub} marks: ")))

grade=sum(sub_list)/subjects
if grade<60:
    print("Grade 4 student")
elif grade>=60 and grade<70:
    print("Grade 3 student")
elif grade>=70 and grade<80:
    print("Grade 2 student")
else:
    print("grade 1 Student") """

#Swapping of Two numbers with and without temporary variable
""" num1 = int(input("Enter number x: "))
num2 = int(input("Enter number y: "))
#swap = num1
#num1 = num2
#num2 = swap
#print("With Swapping variable: ", num1, num2) 
num2,num1= num1, num2
print("Without swpapping variable: ", num1, num2) """

# Multiplication  Table
""" mul_tab=int(input("Enter Number: "))
for i in range(1,20+1):
    print(f"{i} * {mul_tab} =", i*mul_tab) """

# Conversions km to miles vicwe versa 1km = 0.6217 miles
""" kms=int(input("Enter your walked distance today in kilo-metres: "))
miles=kms*0.6217
#kms=miles/0.6217
print("Today you walked miles is: ", miles) """
# Celsius to Fahrenheit Conversion 1 faren=(cel*1.8)+32
""" faren = int(input("Enter farenheit value: "))
celsius=(faren-32)/1.8
print(celsius) """
# How to find Area of Triangle semi-perimeter=a+b+c/2 area=s(s-a)*(s-b)*(s-c)**0.5
""" a= int(input("Enter side a: "))
b= int(input("Enter side b: "))
c= int(input("Enter side c: "))
s= (a+b+c)/2
print("Semi-Perimeter value is: ", s)
area=s*(s-a)*(s-b)*(s-c)**0.5
print("Area of triangle is: ",area) """
# How to find Largest among three inputs
""" a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))

if a>=b and a>=c:
    print("Largest number is:",a)
elif b>=a and b>=c:
    print("Largest number is:",b)
else: 
    print("Largest number is:",c)

#altermethod: max()
d= max(a,b,c)
print("largets number is:", d) """
# Find sum of Natural numbers means if number  > 0 natural
""" num_terms=int(input("Enter numbers terms: "))
sum = 0
if num_terms>0:
    for sum_natural in range(1,num_terms+1):
        sum = sum+sum_natural
        #sum += sum_natural
print(f"Sum of this natural: {sum}") """

#Find Factorial of a Number Ex: 5! = 5*4*3*2*1 =120 logic here Start with the given number, multiply it by each whole number in descending order down to 1, and take the final product as the result.
""" fact_num=int(input("Enter numbers to find factorial: "))
factorial=1
for i in range(fact_num,0,-1):
    factorial=factorial*i
print(f"Factorial of {fact_num} is: {factorial}")
#while loop
while fact_num>0:
    factorial=factorial*fact_num 
    fact_num=fact_num-1
    
print(f"Factorial value is: {factorial}") """
    
#How to generate Fibonacci Series: sequence of numbers where each number after the first two is the sum of the two preceding ones. Ex:F(0) = 0, F(1) = 1 ,then F(2) = F(1) + F(0) = 1 + 0 = 1
""" fib_num = int(input("Enter number to find Fibnacci: "))
f0,f1 = 0,1
if fib_num<=0:
    print("Enter the postive numbers")
elif fib_num==1:
    print(f"Fibonacci Series of {fib_num} is :{f0}")
else:
    for i in range(fib_num):
        print(f0, end=",")
        f0,f1 = f1,f0+f1

# while
    counter=0
    while counter<fib_num:
        print(f0, end=",")
        f0,f1 = f1,f0+f1
        counter+=1 """