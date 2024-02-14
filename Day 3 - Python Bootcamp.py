#IF/ELSE CONDITIONAL OPERATORS
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# a.Greater than
if height > 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry, you have to grow taller before you can ride")

# b. Lesser than
if height < 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry, you have to grow taller before you can ride")

# c. Greater than or equal to
if height >= 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry, you have to grow taller before you can ride")

# d. Lesser than or equal to
if height <= 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry, you have to grow taller before you can ride")

# e. Equal to
if height == 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry, you have to grow taller before you can ride")


#NESTED IF/ELIF STATEMENTS
if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age?"))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
    

#TREASURE ISLAND PROJECT
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right".').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower() 
  if choice2 == "wait":
    choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?').lower()
    if choice3 == "red":
      print('You have entered a room full of fire. Game Over.')
    elif choice3 == "yellow":
      print('You found the treasure! You win!')
    elif choice3 == "blue":
      print('You have entered a room full of beasts. Game Over.')
    else:
      print('You chose a door that doesn\t exist. Game Over.')
  else:
    print('The sea is full of poisonous, slimy snakes which killed you. Game Over.')
else:
  print("You were brutally killed by numerous, large, sharp knives attacking you from either side. Game Over.")

  
