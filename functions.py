"""" 
Q1. If no return statement is used inside the function, the function will always return the value:

A) Null

B) 0

C) None

D) -1

Q2. What is the use of functions in programming languages?

A) Their main purpose is to increase the speed of the program

B) Functions are reusable pieces of programs

C) Functions are used to generate a smoke in the keyboard

D) All of the above

Q3. Which keyword is used to create functions in Python?

A) fun

B) define

C) def

D) function

"""



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

# Write a python function to check if any given number is a prime number and odd number?

def is_prime_and_odd(number):
    """
    Function to check if a given number is a prime number and odd number
    :param number: number to check
    :return: True if number is prime and odd, False otherwise
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    if number % 2 == 0:
        return False
    return True

#Write a python function that will take n as input and print the pattern of n rows. If the n is even, then print it flipped.
# Example:

# n=3
# *
# * *
# * * *

# n=4
# * * * *
# * * *
# * *
# *

def print_pattern(n):
    """
    Function to print a pattern of n rows
    :param n: number of rows
    """
    if n % 2 == 0:
        for i in range(n, 0, -1):
            print('* ' * i)
    else:
        for i in range(1, n+1):
            print('* ' * i)

# Master Yoda speaks a sentence in a different order. Let's say you want to convert a sentence to Yoda’s speech. 
# Write a function named master_yoda which will
# take a string as input and return the output after reversing the words of the sentence.

def master_yoda(sentence):
    """
    Function to convert a sentence to Yoda's speech
    :param sentence: sentence to convert
    :return: sentence in Yoda's speech
    """
    words = sentence.split()
    return ' '.join(words[::-1])

print(master_yoda('I am home')) # 'home am I'


# Write a function pay_bill which will take a list of expenses, percent commission, and a special offer amount

# If you don’t pass percent_comission it should be always 9.8%

# The Last argument special_offer_amount is not a required argument, you don’t need to pass it. Make it an optional parameter.

# If you want to give a special offer to the user, then you have to pass the third argument special_offer_amount. 

# If the user makes the purchase greater than special_offer_amount, then give him an extra commission of 1.2%.

# Calculate the final payable price of the bill and return it from the function.

def pay_bill(expenses, percent_commission=9.8, special_offer_amount=None):
    """
    Function to calculate the final payable price of the bill
    :param expenses: list of expenses
    :param percent_commission: percent commission
    :param special_offer_amount: special offer amount
    :return: final payable price of the bill
    """
    total_expenses = sum(expenses)
    commission = total_expenses * percent_commission / 100
    if special_offer_amount and total_expenses > special_offer_amount:
        commission += total_expenses * 1.2 / 100
    return total_expenses + commission

print(pay_bill([100, 200, 300])) # 609.0