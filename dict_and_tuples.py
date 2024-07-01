""" 
Q1. What will happen when you run this code?

person_info = ("bob gupta", 52, "1 free street, mumbai")
person_info[1] = 54

A) It will assign 54 value to second element in the tuple

B) You will get an error because tuples are immutable

C) It will assign 54 to the first element in the tuple

D) Bob gupta will take you to the court for modifying his age

Q2. What is the purpose of the items() function in a Python dictionary?

A) Returns an array of dictionary keys

B) Returns an array of dictionary values

C) items() is an invalid function for a dictionary

D) To iterate through every item of a dictionary and get key, value in each iteration

Q3. The following dictionary contains salaries based on skill and experience level. 
Which statement can retrieve a senior PHP engineer's salary?

salaries = {
    'python': { 'junior': '100k', 'senior': '600k' },
    'php': { 'junior': '70k', 'senior': '400k' },
    'java': { 'junior': '80k', 'senior': '500k' },
}

A) salaries['php']['senior']

B) salaries['senior']['php']

C) You can't retrieve salaries as they are confidential

D) salaries('php')('senior')

Q4. What is the output of the following?

d = {'Luke': 1994, 'Boba': 1989, 'Kyle': 1998, 'Hann': 1993}
print(d['Boba' : 'Kyle'])

A) [1989, 1998]

B) (1989, 1998)

C) It raises an Error

D) 1989

"""


# diff between  tuples & list
# tuple is immutable and list is mutable
# user case of tuple is when you want to make sure that the data is not changed like returning multiple values from a function
# user case of list is when you want to change the data like adding or removing elements

def find_pe_and_pb(price,eps,book_value):
    """
    Function to calculate PE and PB ratio
    :param price: price of the stock
    :param eps: earnings per share
    :param book_value: book value
    :return: PE and PB ratio
    """
    pe = price / eps
    pb = price / book_value
    return pe, pb

pe_ratio, pb_ratio = find_pe_and_pb(100, 10, 50)

print(pe_ratio, pb_ratio)

# dictionary is a key value pair data structure in python and is mutable like list 
# dictionary is unordered collection of items
# dictionary is defined using curly braces {}
# dictionary is defined as key value pairs
# dictionary is mutable
# dictionary is unordered
# dictionary is dynamic
# dictionary is indexed
# dictionary is nested
# dictionary is iterable

#study big o notation very important concept in data structures and algorithms in youtube  by dhaval patel

# example without dict it will iterate through all the elements to find the value
contacts = [('John Doe', 8867676767), ('Jane Doe', 7867676767), ('John Smith', 9867676767)]

for contact in contacts:
    if contact[0] == 'Jane Doe':
        print(contact[1])
        break
    
# example with dict it will directly go to the key and get the value
# memory management is the only difference between dict and list - array in youtube  by dhaval patel

d = {
    'ravi': 8867676767,
    'john': 7867676767,
    'smith': 9867676767,
    'jane': 9867676767,
}

# read hash table in youtube by dhaval patel
# if key is not present in the dictionary it will throw an error
print(d['jane'])


# if key is not present in the dictionary it will return None
d.get('jane') # 9867676767
d.get('jane1',0) # None , default value is 0

#if want to add a new key value pair to the dictionary
d['jane1'] = 7867676767
print(d)

#if want modify the value of a key in the dictionary
d['jane1'] = 7867676768

#if want to delete a key value pair from the dictionary
del d['jane1']

# if want to check if a key is present in the dictionary
print('jane' in d) # True

#in operator is used to check if a key is present in the dictionary
#in operator is used to check if a value is present in the list


e = {
    'ravi': {'phone': 8867676767,'email': 'p@g.com'},
    'john': {'phone': 7867676767,'email': 'j@g.com'},
    'smith': {'phone': 9867676767,'email': 's@g.com'},
    'jane': {'phone': 9867676767,'email': 'jj@g.com'},
}

print(e['ravi']['phone']) # 8867676767
print(e['ravi']['email']) # p@g.com


# it is iterating through the dictionary and printing the key and value
for name in d:
    print(name, d[name])

#another way to iterate through the dictionary
for name , number in d.items():
    print(name, number)

# to get all the methods of the dictionary
print(dir(d)) # to get all the methods of the dictionary

# to get all the keys of the dictionary
print(list(d.keys()))
# to get all the values of the dictionary
print(list(d.values()))
# to get all the items of the dictionary
print(list(d.items()))


# print(d['jane': 'smith'])

# Excercise

# Create a list of your friends' names and now create a list of tuples. 
# The tuple should contain the friend’s name and the length of the name. 
# For Example: if someone’s name is Adit12
# ya, the tuple would be: (‘Aditya’, 6)
friends = [('Pradnya', 7),('Kavita',6),('Pramod',6)]


# You and your wife argued about expenses last night. You both want to know who is spending more in a month. 
# Now you both go to the Little Yoda he is a good python programmer.
# He suggested that both of you add an entry in a dictionary next time you spend money. 
# So that you can have a clear picture of your expenses and plan to reduce them. Both dictionaries are as below-
# Your expenses -

# Clothes - 1100
# Shoes - 1000
# Watch - 900
# Mobile Recharge - 699
# Petrol - 1980

# Your Wife’s expenses -

# Mobile Recharge - 799
# DTH recharge - 999
# Clothes - 2310
# Makeup - 3670
# Shoes - 999
# Find out the total expenses for each of you.
# Find out who spending more
# Find out which thing you and your wife spending more

Pramod = {
    "Clothes": 1100,
    "Shoes": 1000,
    "Watch": 900,
    "Mobile Recharge": 699,
    "Petrol": 1980
}

Pradnya = {
    "Mobile Recharge": 799,
    "DTH Recharge": 999,
    "Clothes": 2310,
    "Makeup": 3670,
    "Shoes": 999
}

# Calculate total expenses for Pramod
Pramod_Expense = sum(Pramod.values())

# Calculate total expenses for Pradnya
Pradnya_Expense = sum(Pradnya.values())

# Determine who is spending more
if Pramod_Expense > Pradnya_Expense:
    spender = "Pramod"
    higher_expense = Pramod_Expense
else:
    spender = "Pradnya"
    higher_expense = Pradnya_Expense

# Find the highest expense category for Pramod
Pramod_Max_Spend_Category = max(Pramod, key=Pramod.get)
Pramod_Max_Spend_Amount = Pramod[Pramod_Max_Spend_Category]
print(Pramod_Max_Spend_Amount)

# Find the highest expense category for Pradnya
Pradnya_Max_Spend_Category = max(Pradnya, key=Pradnya.get)
Pradnya_Max_Spend_Amount = Pradnya[Pradnya_Max_Spend_Category]
print(Pradnya_Max_Spend_Amount)

# Print results
print(f"Total expenses for Pramod: {Pramod_Expense}")
print(f"Total expenses for Pradnya: {Pradnya_Expense}")
print(f"{spender} is spending more with a total of {higher_expense}.")
print(f"Pramod's highest spending is on {Pramod_Max_Spend_Category} with an amount of {Pramod_Max_Spend_Amount}.")
print(f"Pradnya's highest spending is on {Pradnya_Max_Spend_Category} with an amount of {Pradnya_Max_Spend_Amount}.")

    
# You are working on a project where you need to store the details of the students in a class.
# You need to store the student's name, roll number, and marks in a dictionary.








