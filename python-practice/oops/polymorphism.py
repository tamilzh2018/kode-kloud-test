#Poly+morphism:- many+forms Ex: when Man/Women in office their roles is employee if they are in home there roles is father/mother or if they are in play ground their roles is player form.  
#Polymorphism in '+' operator
""" num1=10
num2=20
print("'+' operator with integer form is addition: ", num1+num2)
num3= 'hai'
num4='all'
print("'+' operator with string form is concatenation: ", num3+num4) """
#Polymorphism in '*' operator
""" num1=10
num2=20
print("'*' operator with integer form is Multiplication: ", num1*num2)
num3= 'hai'
num4=2
print("'*' operator mix of string and integer form is repeat  : ", num3*num4) """
#Polymorphism in Functions
""" print(len('string'))
print(len(['list',1,True, 0.5]))
print(len({'key':'value','dict':'form'})) """

#Polymorphism in Classes: diffrent class name but same method name
""" class A:
    def info(self):
        print("Class A method")
class B:
    def info(self):
        print("Class B method")
a_obj=A()
b_obj=B()
a_obj.info()
b_obj.info()
 """

#types:Operator overloading(arithmetic operator, comparision operator,assignment operator) 
# method overloading(by default not support but we can achive by if condn and for loop or multipledispatch modules),
# method overriding