
#Activity 1

pet_parade_order = ['Pete the Pug', 'Sally the Siamese Cat', 'Beau the Boxer', 'Lulu the Labradror', 'Lily the Lynx', 'Pauline the Parrot', 'Gina the Gerbil', 'Tubby the Tabby Cat']

#A good thing has just happened! Gina just got adopted , so she no longer needs to be in the pet parade. Go ahead and remove Gina.
pet_parade_order.remove('Gina the Gerbil')

#Since Pauline the Parrot can talk, the shelter director decides that she should be first in line to say hello to the crowd! Move Pauline to the front of the pet parade order.
del pet_parade_order[5]
pet_parade_order[0:0] = ['Pauline the Parrot']

#Suddenly, two more animals get dropped off at the shelter. They are: Mimi the Maltese Cat and Cory the Corgi. Both of them must go afer Lily in the parade. Place Mimi and Cory together after Lily.
pet_parade_order[6:6] = ['Mimi the Maltese Cat', 'Cory the Corgi']

#More good news! Lulu and lily just got adopted my the same owner. He likes both of them very much and thinks they can be good friends. Remove Lulu and lily from the parade.
del pet_parade_order[4:6]
print(f"The order of the Pet Parade is : {pet_parade_order}")



#Activity 2

age = 10
favorite_outfit = "red dress"
favorite_hobby = "reading"
year == 2020

if year == 2020:
    print(f"It is 2020. I am currently {age} years old, love wearing a {favorite_outift}, and currently, {favorite_hobby} is my favorite thing to do!")

elif year == 2025:
    age += 5
    favorite_outfit = "jumpsuit"
    favorite_hobby = "coding"
    print(f"It is 2025. I am currently {age} years old, love wearing a {favorite_outfit}, and currently, {favorite_hobby} is my favorite thing to do!")

elif year == 2030:
    age += 10
    favorite_outfit = "jeans and a t-shirt"
    favorite_hobby = "playing the piano"
    print(f"It is 2030. I am currently {age} years old, love wearing a {favorite_outfit}, and currently, {favorite_hobby} is my favorite thing to do!")

elif year == 2035:
    age += 15
    favorite_outfit = "bike shorts and a t-shirt"
    favorite_hobby = "biking"
    print(f"It is 2035. I am currently {age} years old, love wearing a {favorite_outfit}, and currently, {favorite_hobby} is my favorite thing to do!")

elif year == 2040:
    age += 20
    favorite_outfit = "white dress"
    favorite_hobby = "playig board games"
    print(f"It is 2040. I am currently {age} years old, love wearing a {favorite_outfit}, and currently, {favorite_hobby} is my favorite thing to do!")

















