cher_dress_color = 'pink'
cher_shoe_color = 'white'
cher_has_earrings = True
dionne_dress_color = 'purple'
dionne_shoe_color = 'pink'
dionne_has_earrings = True

#Outfit Check 1: Cher and Dionne have different dress colors
print(f"Both girls have different dress colors? {cher_dress_color != 'purple' and dionne_dress_color != 'pink'}")

#Outfit Check 2: Cher and Dionne are both wearing earrings
print(f"Both girls are wearing earrings? {cher_has_earrings == True and dionne_has_earrings == True}")

#Outift Check 3: At least one person is wearing pink
print(f"At least one person is wearing pink? {cher_dress_color == 'pink' or dionne_dress_color == 'pink'}")

#Outfit Check 4: No one is wearing green
print(f"No one is wearing green? {cher_dress_color != 'green' and dionne_dress_color != 'green'}")

#Outfit Check 5: Cher and Dionne have the same shoe color
print(f"Both girls have the same shoe colors? {(cher_shoe_color == 'pink' and dionne_shoe_color == 'pink') or (cher_shoe_color == 'white' and dionne_shoe_color == 'white')}")


beakers = 20
tubes = 30
rubber_gloves = 10
safety_glasses = 4

enough_safety_glasses = (safety_glasses % 4) == 0
enough_rubber_gloves == rubber_gloves >= (2 * 4)
enough_tubes = tubes >= 10 * 4
enough_beakers = beakers >= 5 * 4

final_report = f'''
    Here is the final report for lab materials:
    -
    Each girl had enough safety glasses: {enough_safety_glasses}
    Each girl had enough rubber gloves: {enough_rubber_gloves}
    Each girl had enough tubes: {enough_tubes}
    Each girl had enough beakers: {enough_beakers}
    -
    Ther are enough gloves and safety glasses for each girl:
    {enough_rubber_gloves and enough_safety_glasses}
    There are more than enough tubes and an exact amount of beakers for each girl: {tubes > 40 and beakers == 20}
    Each girl has at least the exact or greater amount of tubes or the exact amount of beakers: {tubes >= 40 or beakers == 20}
'''
print(final_report)
