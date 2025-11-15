#The 'match' statement is used to perform different actions based on different conditions.
#Instead of writing many if..else statements, you can use the match statement.
#The match statement selects one of many code blocks to be executed.
#syntax:
""" 
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block 
    """
#Example
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")