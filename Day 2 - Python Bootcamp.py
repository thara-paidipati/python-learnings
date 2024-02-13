# 1.DATA TYPES
# a.String
print("Hello"[4])

print("123" + "456")  #❌
#Numbers aren't strings

# b.Integers
print(123 + 456)  #✅

# c.Float - has a decimal place
3.14159

# d.Boolean
True
False


# 2.TYPE CHECKING, TYPE CONVERSION
# a.Type checking
num_chart = len(input("What is your name?"))
#print("Your name has " + num_chart + "characters.")
print(type(len(input("What is your name?"))))

# b.Type conversion
num_chart = len(input("What is your name?"))
new_num_chart = str(num_chart)
print("Your name has " + new_num_chart + " characters.")

# 3.MATHEMATICAL OPERATIONS IN PYTHON
print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3)
print(2**3)
#PEMDASLR
#Parentheses ()
#Exponents **
#Multiplication *
#Division /
#Addition +
#Subtraction -
#LR means Left to Right

print(3 * 1 + 9 / 3 - 3)

# 4.NUMBER MANIPULATION AND F STRINGS IN PYTHON
# a.Rounding numbers
print(round(8 / 3))
print(8 // 3)  #floor division converts numbers into integers

result = 4 / 2
result /= 2
print(result)

score = 0
#User scores a point
score += 1
print(score)

# b.f-Strings
score = 0
height = 1.8
isWinning = True

print(
    f"Your score is {score}, your height is {height}, you are winning is {isWinning}"
)

#TIP CALCULATOR PROJECT
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
bill_as_float = float(bill)
tip_as_int = int(tip)
people_as_int = int(people)
tip_as_percent = tip_as_int / 100
total_tip_amount = bill_as_float * tip_as_percent
total_bill = bill_as_float + total_tip_amount
bill_per_person = total_bill / people_as_int
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
