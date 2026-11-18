# 💻 Exercises: Day 6
# Exercises: Level 1

# Create an empty tuple
tpl = ()
print(tpl)

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
bros = ("Tushar", "Aadi", "Sumit", "Vivek")
sis = ("Khushi", "Amrit", "Sweta", "Ankita")
print(f"bros:{bros} & sis:{sis}")

# Join brothers and sisters tuples and assign it to siblings
siblings = bros + sis
print(siblings)

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parent = ("Dinesh", "Rekha")
siblings_list = list(siblings)
siblings_list.pop(3)
print(siblings_list)
siblings = tuple(siblings_list)
family_members = siblings + parent
print(family_members)

# Exercises: Level 2

# Unpack siblings and parents from family_members
*siblings, father, mother = family_members
print(siblings)
print(father, mother)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Apple", "Banana", "Cherry")
vegetables = ("Carrot", "Tomato", "Brinjal")
animal_products = ("gum", "pigments", "leather")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid = len(food_stuff_lt) // 2
slc = food_stuff_lt[mid:mid+1]
print(slc)

# Slice out the first three items and the last three items from food_stuff_lt list
slc1 = food_stuff_lt[0:3]
slc2 = food_stuff_lt[-3:]
print(f"{slc1} & {slc2}")

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries)

# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)
