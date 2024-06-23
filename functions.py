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

#find valume of cylinder pi*r^2*h
#positional orguments
def cylinder_volume(radius, height):
    """
    Function to calculate the volume of a cylinder
    :param radius: radius of the cylinder
    :param height: height of the cylinder
    :return: volume of the cylinder
    """
    pi = 3.14159
    return pi * (radius ** 2) * height

r= 5
h = 10
print(cylinder_volume(radius=r, height=h)) # 942.477

#default arguments

def cylinder_volume(radius, height=10):
    """
    Function to calculate the volume of a cylinder
    :param radius: radius of the cylinder
    :param height: height of the cylinder
    :return: volume of the cylinder
    """
    pi = 3.14159
    return pi * (radius ** 2) * height

