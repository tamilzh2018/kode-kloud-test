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