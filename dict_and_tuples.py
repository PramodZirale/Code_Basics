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

#study big o notation very important concept in data structures and algorithms in youtube

# example without dict it will iterate through all the elements to find the value
contacts = [('John Doe', 8867676767), ('Jane Doe', 7867676767), ('John Smith', 9867676767)]

for contact in contacts:
    if contact[0] == 'Jane Doe':
        print(contact[1])
        break
    
# example with dict it will directly go to the key and get the value
# memory management is the only difference between dict and list - array in youtube

d = {
    'ravi': 8867676767,
    'john': 7867676767,
    'smith': 9867676767,
    'jane': 9867676767,
}

print(d['jane'])



