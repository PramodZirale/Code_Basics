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


    