import math
from math import sqrt
#Lab 3
#1. Please use Python to find the answer
# a2+ b3, where a is 3 and b is 4 (What does the operator ** do?)
#The ** operator lets us use expnents. Three squared would be written as 3**2
a = 3
b = 4
a_squared = int(a**2) 
print(a_squared)
b_cubed = int(b**3)
print(b_cubed)
total = a_squared + b_cubed
print("a squared + b cubed = " + str(total))
# the remainder of 34568 ÷ 345 (What does the % operator do?)
#The % is the modulo operator, which gets the remainder from the quotient of two integers (or floats)
remainder = 34568 % 345
print("Remainder is: " + str(remainder))
#Output: Remainder is: 68
# Show that int(8.2)/int(2.1) ≠ int(8.2/2.1)
first_int = int(8.2) / int(2.1)
print("First Integer: " + str(first_int))
#Output: First Integer: 4.0
#When we divide int(8.2) by int(2.1), the two floats, 8.2 and 2.1, are rounded down once they are converted to integers.
second_int = int(8.2/2.1)
print("Second Integer: " + str(second_int))
#Output: Second Integer: 3
#When we divide the numbers prior to converting them to integers, the calculation is made, and the answer is 3.9. Once the floats are converted to integers, the number is rounded down to 3.
# sqrt (678) / truncate(8.3/3) Hint: Use // for truncate. math.sqrt() for sqrt. You need to import the math module
square_root = sqrt(678)
math_trunc = math.trunc(8.3/3)
print("Square Root: " + str(square_root))
print("Math Trunc: " + str(math_trunc))
quotient = square_root // math_trunc
print("Quotient: " + str(quotient))
#Output: Quotient: 13.0
#2. Write a Tipper program where the user enters a restaurant bill total. The program should display the tip amount and total bill
#HINT: Your program flow should be
# Greet the customer
# Ask them how much the total bill is
# Ask if they want to pay a top
# If yes, ask what percentage. If no, do nothing
# Print out the tip amount and the total bill
greeting = "Hello customer. I hope you enjoyed your meal! It is time to pay now."
meal_total = float(input("How much was the total bill tonight?"))
print(meal_total)
tip_or_nah = input("Would you like to tip your server?")
if tip_or_nah in ["y","Y","yes","YES","YAY","Yeah", "Yee", "YEAH"]:
  tip_percentage = float(input("What percentage would you like to tip your server tonight?(1% = .01, 100% = 1.0)"))
  tip_amount = (meal_total * tip_percentage)
  formatted_tip_amount = "%.2f" % tip_amount
  print(formatted_tip_amount)
  final_bill_total =  meal_total + tip_amount
  formatted_bill_total = "%.2f" % final_bill_total
  print("After your tip of $" + str(formatted_tip_amount) + ", your total is $" + str(formatted_bill_total))
else:
  print("Thank you for eating and not tipping your server, cheapo. Your total is " + str(meal_total))
#3. Write a program that asks the user their total score (a floating point number) in the python class.
#Your program will tell them the grade. 
score = float(input("What is your score in this Python Class?"))
print("Your Score is " + str(score))
if score >= 450:
  grade = "A"
  print("Your Grade is an " + str(grade) + " : Distinguished")
if score >= 400 and score < 450:
  grade = "B"
  print("Your Grade is a " + str(grade) + " : Above Average")
if score >= 350 and score < 400:
  grade = "C"
  print("Your Grade is a " + str(grade) + " : Average")
if score >= 300 and score < 350:
  grade = "D"
  print("Your grade is a " + str(grade) + " : Minimum Passing")
if score < 300:
  grade = "F"
  print("Your grade is an " + str(grade) + " : Failing")