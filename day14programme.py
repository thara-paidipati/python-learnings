
#Activity 1

name = "Thara Paidipati"

#Adventure beigns
print(f"Welcome to {name}'s Choose your own Adventure game! As you follow the story, you will be presented with choices that decide your fate. Take care and choose wisely! Let's begin.")

print("You find yourself in a dark room with 2 doors. The first door is red, the second is white!")

door_choice = input("Which door do you want to choose? red=red door white=white door")

if door_choice == "red":
    print("Great, you walk through the red door and are now in the future! You meet a scientist who gives you a mission of helping save the world!")

    choice_one = input("What do you want to do? 1=Accept or 2=Decline")
    if choice_one=="1":
        print("""__________SUCCESS__________
        You helped the scientist to save the world! In gratitude, the scientist builds a time machine and sends you home!""")
    else:
        print("""__________GAME OVER__________
        Too bad! You declined the scientist's offer and now you are stuck in the future!""")

else:
    print("Great, you walked through the white door and now you are in the past! You meet a princess who asks you to go on a quest.")

    quest_choice = input("Do you want to accept her offer and do on the quest, or d you want to stay where you are? 1=Accept and go on the quest or 2=Stay")

    if quest_choice=="!":
        print("The princess thanks you for accepting her offer, You begin the quest.")
    else:
        print("""__________GAME OVER__________
        Well, I guess your story ends here!""")
