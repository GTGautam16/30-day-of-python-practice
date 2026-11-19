# 💻 Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Infosys", "NEC", "Boomlet", "HCLTech"])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.pop()                  # pop for random deletion & remove for specific deletion.
print(it_companies)

# What is the difference between remove and discard
'''
remove method delete specific items from the set but raise errors if specific elements is not present in the set while discard method delete in similar method but doesn't raise erros if the specific item/elemsnt is not present.
'''

# Exercises: Level 2

# Join A and B
print(A.union(B))

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
print(A.union(B))
print(B.union(A))

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A, B

# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(age))
Age = set(age)
print(len(Age))

# Explain the difference between the following data types: string, list, tuple and set
'''
String : Ordered, Cannot be modiefied(Immutable), Indexed 
List : Ordered, Mutable(update), use [], all data types can be stored, can store duplicates, Indexed
Tuple : Ordered, Immutable(cannot update), use (), all data types can be stored, can store duplicates, Indexed
Set : Unordered, Mutable(But each elements should be immutable/hashable), use set() ( {} ), all data types can be stored, cannot store duplicates, Unindexed, set properties like union, joins, etc.
''' 

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print(unique_words)
print(f"unique words in the sentence is: {len(unique_words)}")
