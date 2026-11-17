# 💻 Exercises: Day 5
# Exercises: Level 1

# Declare an empty list
ls = []
print(ls)

# Declare a list with more than 5 items
ls1 = [5, "5g", "GT", 5.2, "Hello", "Friend"]
print(ls1)

# Find the length of your list
print(len(ls1))

# Get the first item, the middle item and the last item of the list
print(ls1[0], ls1[2], ls1[4])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Gautam", 22, 175, "single", "mumbai" ]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(mixed_data_types)
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0], it_companies[3], it_companies[6])

# Print the list after modifying one of the companies
it_companies1 = it_companies.copy()
it_companies1.pop(3)
print(it_companies1)

# Add an IT company to it_companies
it_companies.append("NVIDIA")

# Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies)/2), "NEC")        # Here i use common logic using len/2 to get middle index😁
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()          # here first it modified the value and return the value and added to the list.
print(it_companies)

# Join the it_companies with a string '#;  '
print("#; ".join(it_companies))

# Check if a certain company exists in the it_companies list.
print("NEC" in it_companies)        # use in to find if the value is present or not.

# Sort the list using sort() method
it_companies.sort()         # i can use sorted() if i want to create a new sorted list.
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
del it_companies[0:3]
print(it_companies)

# Slice out the last 3 companies from the list
del it_companies[-3:]
print(it_companies)

# Slice out the middle IT company or companies from the list
del it_companies[1]
print(it_companies)

# Remove the first IT company from the list
it_companies.remove("Microsoft")
print(it_companies)

# Remove the last IT company from the list
it_companies.remove("Google")
print(it_companies)

# Remove all IT companies from the list
IT_Companies = it_companies1
IT_Companies.clear()
print(IT_Companies)

# Destroy the IT companies list
del IT_Companies

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, 
# then insert Python and SQL after Redux.
full_stack_copy = full_stack.copy()
full_stack_copy.insert(5, "Python")
full_stack_copy.insert(6, "SQL")
print(full_stack_copy)

# Exercises: Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
srt_ls = sorted(ages)
print(srt_ls[0], srt_ls[-1])

# Add the min age and the max age again to the list
min_age = srt_ls[0]
max_age = srt_ls[-1]
srt_ls.append(min_age)
srt_ls.append(max_age)
print(srt_ls)

# Find the median age (one middle item or two middle items divided by two)
print(len(srt_ls))

mid = len(srt_ls) // 2  # to get middle index
median = (srt_ls[mid-1] + srt_ls[mid]) // 2   # to get medain age (here two values has to add and divide by 2 as list has 12 elements.)
print(median)

# Find the average age (sum of all items divided by their number )
avg = sum(ages) / len(ages)    # use sum method to add all the elements in the list 
print(avg)

# Find the range of the ages (max minus min)
range = max(ages) - min(ages)
print(range)

# Compare the value of (min - average) and (max - average), use abs() method
avg = sum(ages) / len(ages)

min_diff = abs(min(ages) - avg)
max_diff = abs(max(ages) - avg)
print(f"{min_diff:.2f}")
print(f"{max_diff:.2f}")

# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

middle = len(countries) // 2
if len(countries) % 2 == 0:
    print(countries[middle-1:middle+1])
else:
    print(countries[middle])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
middle = (len(countries) + 1) // 2
first_half = countries[:middle]
second_half = countries[middle:]
print(first_half)
print(second_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first, second, third, *scandic = countries
print(f"first:{first}, \nsecond:{second}, \nthird:{third}, \nscandic countries:{scandic}")
