""" 
Question 1
Which statement is True about list data type in python?
a) You can store only the same type of elements in a list.
b) You can store any type of element in a list.
c) You cannot make a list containing lists.
d) You need to initialize the list with a predetermined size.

Question 2
Select the option to join two lists in python
a) new_list = list_1 + list_2
b) new_list= list_1 - list_2
c) new_list = extend(list_1, list_2)
d) new_list.join(list_1, list_2)

Question 3
These are the top English movies by their revenues arranged in ascending order. This means the last movie on the list (Avatar) made the most money. Which Python statement can help you find out the top 3 movies by their revenues?
movies = ["Jurassic World","Spider-man","Titanic","Avengers-Endgame","Avatar"]
a) movies[:3]
b) movies[:4]
c) movies[1:3]
d) movies[-3:]

"""



items = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

print(items)

items.append('kiwi')

print(items)

items.remove('banana')

print(items)    

items.insert(2, 'mango')

print(items)


print("rice" in items)

expenses = [2200, 2350, 2600, 2130, 2190]

expenses.sort()

print(expenses)

expenses.sort(reverse=True)

print(expenses)


food_items  = ['rice', 'wheat', 'sugar', 'salt', 'milk', 'fruits', 'vegetables']
bathroom_items = ['soap', 'shampoo', 'toothpaste', 'toothbrush', 'towel', 'napkin', 'comb'] 

all_items = food_items + bathroom_items

print(all_items)

print(len(all_items))

print(dir(all_items))

#betrogenious list
#homogenous list

""" 
You are a Marvel fan and created a list of superheroes.

avengers  = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]

Using this list, do the following:

Calculate how many members are in the Avengers team?
Iron Man made Spider-Man a new member of the Avengers, add him to your list.
Captain America is the leader of the Avengers, you need to add him before Iron Man,
so remove him from the list and add him before Iron Man.
You don't like Thor and Hulk together because they get angry easily and fight with each other.
So you have to separate them from each other. To separate them, either move “Black Widow” or “Hawkeye” in between them.
After Avengers: End Game the original six avengers are retired, 
now you need to remove them from your list and add new superheroes 
like Doctor Strange, Vision, Wanda, Kate Bishop, and Ant-Man.
As “Captain America” is also retired and now currently, no one is the leader, 
so sort the list in alphabetical order. Whoever will come at the 0th
index will become the Leader. (BONUS: can you guess who will become the leader)

"""
avengers  = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]

#Calculate how many members are in the Avengers team?
print(len(avengers))

#Iron Man made Spider-Man a new member of the Avengers, add him to your list.
avengers.append("Spider Man")
print(avengers)

#Captain America is the leader of the Avengers, you need to add him before Iron
avengers.remove("Captain America")
avengers.insert(0, "Captain America")   
print(avengers)

#You don't like Thor and Hulk together because they get angry easily and fight with each other.
#So you have to separate them from each other. To separate them, either move “Black Widow” or “Hawkeye” in between them.
avengers.remove("Black Widow")
avengers.insert(3, "Black Widow")
print(avengers)

#After Avengers: End Game the original six avengers are retired,
#now you need to remove them from your list and add new superheroes

avengers.clear()
avengers.extend(["Doctor Strange", "Vision", "Wanda", "Kate Bishop","Ant Man"])
print(avengers)

#As “Captain America” is also retired and now currently, no one is the leader,
#so sort the list in alphabetical order. Whoever will come at the 0th index will become the Leader.
avengers.sort()
print(avengers)
print(f'Leader : {avengers[0]}')




