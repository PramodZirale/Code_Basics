""" 

Q1. What value of x will this program print?
x = -1
while x <=99:
  x += 2
print(x)

a) 99 b) 100 c) 101 d) No of the above

Q2.
Every element in the transactions array is a tuple where the first element is a credit card transaction ID and the second one is a code that indicates if that transaction is a fraud. Code ‘f’ means fraud and other codes are valid transactions. What is the purpose of the count variable in this case?

count = 0
transactions = [(456, 'f'), (457, 'n'), (458, 'w'), (459, 'f')]
for transaction in transactions:
    if transaction[1] != 'f':
        count += 1
        
A. Nothing. A programmer was feeling bored so they wrote some random code

B. Keep a count of all fraud transactions

C. Keep a count of all non-fraud transactions

D. Filter fraud transactions from an array

Q3. What is the output?

for l in 'SkillBasics':
    if l == 'i':
        continue
    print(l, end='')

A. SkillBasics

B. SkllBasics

C. SkillBascs

D. SkllBascs


Q4. What is the output of the following range() function?

for n in range(1, -6, -2):
    print(n, end=', ')

A) 0, -2, -4, -6

B) 1, -1, -3, -5

C) 1, 0, -1, -2, -3, -4

D) 1, 0, -1, -2

"""




#looping through a list of expenses and calculating total expense
expenses = [10, 20, 30, 40, 50]
total = 0

for expense in expenses:
    total = total + expense
    
print(total)

#looping through a list of monthly expenses and calculating total expense
total_expense = 0
for i in range(len(expenses)):
    expense = expenses[i]  
    print(f' Month {i+1} expense: {expense}')
    total_expense  = total_expense + expense

print(f'Total expense: {total_expense}')

#looping through expense list using enumerate
total_expense = 0
for i, expense in enumerate(expenses):
    print(f' Month {i+1} expense: {expense}')
    total_expense  = total_expense + expense

print(f'Total expense: {total_expense}')


#for loop with if else & break
locations = ['Pune', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata']

key_location = 'Bangalore'

for location in locations:
    if location == key_location:
        print(f'{key_location} found')
        break
    else:
        print(f'{key_location} not found')


#for loop with if & continue
for i in range(1,10):
    if i%2 == 0:
        print(f'{i} is even')
        continue
    
#while loop 
i = 0

while i < 10:
    print(i)
    i += 1

#Looping Quiz    
x = -1
while x <=99:
  x += 2
print(x)



for n in range(1, -6, -2): # range(start, stop, step)
    print(n, end=', ')
    
for l in 'SkillBasics':
    if l == 'i':
        continue
    print(l, end='')


# Write a Python program to print the following pattern.

# 1 2 3 4 5
# 1 2 3 4 
# 1 2 3
# 1 2
# 1

for i in range(6, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print() 
    
# Write a Python program to find the sum of all the numbers
# except odd numbers between 1 and 20 using a loop. Can you also do this using a while loop?
#using for
odd_num_sum = 0
for i  in range(1,21):
    if i%2 != 0:
        odd_num_sum+=i
      
print(f'Sum of odd numbers between 1 and 20 using for loop: {odd_num_sum}')      

# Using While

odd_num_sum_1 = 0
i=0
while i<=20:
    if i%2 != 0:
        odd_num_sum_1+=i
    i=i+1

print(f'Sum of odd numbers between 1 and 20 using while loop: {odd_num_sum_1}')        
        

# After throwing the dice several times, you got this result,
dice_result  = [5,6,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
# Using a for loop find out the followings:
# How many times have you got 6s
# How many times have you got 1s
# How many times have you got 6s two times in a row
for i in range (len(dice_result)):
    if dice_result[i] == 6:
        print(f'6 found at index {i}')
    if dice_result[i] == 1:
        print(f'1 found at index {i}')
    if i < len(dice_result)-1 and dice_result[i] == 6 and dice_result[i+1] == 6:
        print(f'6 found at index {i} and {i+1}')
        
# Let's say you are doing push-ups and you have to complete 50 push-ups daily, write a program that,

# Upon completing 10 push-ups in a go, asks you, “Are you tired?”

# If you reply “yes” or “y” then it should break and print “You did total push-ups.”

# For example: If you did only 30  push-ups and answered “yes” to your program. 
# It will break the loop and print “You did a total of 30 push-ups**”**

# If you reply “no” or “n” then it should continue and display how many push-ups are remaining  
# now after that ask you again “Are you tired?”

# For Example: if you answered “no” then it should display that 20 push-ups are remaining and ask you again “Are you tired?”

# If you complete all 50 push-ups, then it should print the “Congratulations! You made it” and stopped the program.