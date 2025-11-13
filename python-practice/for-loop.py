#1. Print 2 table using for loop
""" table_num = int(input("Enter a number to dispaly multiplication table"))

for i in range(1,table_num+1):
    #print(i," * 2 =",i*2)
    print(f"{i} * 2 = {i*2}") """

#2. Get input for number a and b. Print the number between a and b.
""" num_a = int(input("Enter Number1: "))
num_b = int(input("Enter Number2: "))
for i in range(num_a, num_b+1):
    print(f"Numbers between {num_a} and {num_b} are: {i}") """

#3. Print Even numbers between 1 to 10
""" for i in range(1, 11):
    if (i % 2 == 0):
        print(i) """

#4.Count the Number of odd numbers between 1 to 10
""" count = 0
for i in range(1,11):
    if (i % 2 != 0):
        count=count+1
print(count) """

#5. Count the number which are divisible by 3 and 5 between 1 to 100
""" count = 0
for i in range(1,101):
    if (i % 3 == 0) and (i % 5 ==0):
        count=count+1
print(count) """

#6. Write a program to compute the sum of the first 5 nautural numbers(positive integers beginning at 1)
""" nat_num = int(input("Naturals numbers: "))
sum = 0
for i in range(1, nat_num+1):
    sum = sum + i 
print(sum) """
#7. Write a program to read 10 numbers from the keyboard and their sum and Avg
""" empty_list = []
key_input = int(input("Enter the number of terms: "))
sum = 0
for i in range(1,key_input+1):
    num = int(input(f"Enter your number{i}: "))
    empty_list.append(num)
for j in empty_list:
    sum = sum + j
print("Sum of Entered values are ",sum)
avg = sum/key_input
print("Average of Entered values are",avg) """
#8. Write a program to display n terms of natural numbers and their sum 
# Program to display n terms of natural numbers and their sum

""" # Input: number of terms
n = int(input("Enter the number of terms: "))

# Initialize sum
total_sum = 0

print("The first", n, "natural numbers are:")

# Loop through natural numbers
for i in range(1, n + 1):
    print(i, end=" ")
    total_sum += i

# Print the sum
print("\nThe sum of the first", n, "natural numbers is:", total_sum) """

#9. Write a program to display the cube of the number up to an integer.
""" key_input = int(input("Enter numbers: "))
for i in range(1,key_input+1):
    print(f"cube of the {i} is {i**3}") """

# Write a program to display week and day with nested for loop
""" for i in range(1, 5):
    print(f"Week{i}:")
    for j in range(1,8):
        print(f"Day{j}:")
 """
#10 Write a program to display right angle triangle and inverted triangles using * symbol
""" for i in range (1,5+1):
    print()
    for j in range(1,i+1):
        print("*", end=" ")
 """

#11. Write a program to display Diamond-like triangle pattern

n = 5  # height of the top half

""" # Top half (increasing)
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Bottom half (decreasing)
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
 """

# Inverted Right-angled triangle
print("Inverted Right-angled triangle:")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()  # move to next line

# Inverted Left-angled triangle
print("\nInverted Left-angled triangle:")
for i in range(n, 0, -1):
    # print spaces first
    for j in range(n - i):
        print(" ", end=" ")
    # then print stars
    for k in range(i):
        print("*", end=" ")
    print()  # move to next line



