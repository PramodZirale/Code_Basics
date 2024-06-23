# function to accept a list of numbers and return the sum of all numbers in the list

def sum_of_numbers(numbers):
    """ 
    Function to accept a list of numbers and return the sum of all numbers in the list
    :param numbers: list of numbers
    :return: sum of all numbers in the list    

    """
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(sum_of_numbers([1, 2, 3, 4, 5])) # 15

# print(help(sum_of_numbers)) : pycharm will show the docstring of the function

