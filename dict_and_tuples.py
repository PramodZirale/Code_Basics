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



for name in d:
    print(name, d[name])

for name , number in d.items():
    print(name, number)

print(dir(d)) # to get all the methods of the dictionary

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))



