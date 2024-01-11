
#Activity 1

slicing_area = []
dicing_area = []

crate_1 = ['onions', 'peppers', 'mushrooms', 'apples', 'peaches']
crate_2 = ['lemons', 'limes', 'broccoli', 'cauliflower', 'tangerines']
crate_3 = ['squash', 'potatoes', 'cherries', 'cucumbers', 'carrots']

#Crate 1 solution
slicing_area.append(crate_1[3])
slicing_area.append(crate_1[4])
dicing_area.append(crate_1[0])
dicing_area.append(crate_1[1])
dicing_area.append(crate_1[2])

#Crate 2 solution
dicing_area[3:3] = crate_2[2:4]
slicing_area[2:2] = crate_2[0:2]
slicing_area.append(crate_2[4])

#Crate 3 solution
dicing_area[5:5] = crate_3[0:2]
slicing_area.append(crate_3[2])
dicing_area[7:7] = crate_3[3:5]

print(f"Vegetables: {dicing_area}")
print(f"Fruits: {slicing_area}")


