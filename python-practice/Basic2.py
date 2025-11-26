#How to Find HCF(Highest Common Factor) or GCD – (Greatest Common Divisor) of a Number 
#Division Method (Euclid’s Method) Find HCF of 48 and 18 ==> high/low=remainder1 then low/remainder1=remainder2 then remainder1/remainder2 ...
high = int(input("Enter Hiogh value Number: "))
low = int(input("Enter Low value Number: "))
while low != 0:
    high, low = low, high%low
print(high)
    