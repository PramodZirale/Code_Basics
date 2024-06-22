""" 
Question 1
Index of the strings in Python starts with  
a) 1  
b) 0  
c) Any random number  
d) -1

Question 2
Which method should you use to convert the string “hello python!” to “Hello Python!”?  
a) title()  
b) upper()  
c) lower()  
d) capitalize()

Question 3
What is the output of the following code?
```python
my_fav_sweet = "I love jalebi, kaju katli and laddu."
"Jalebi" not in my_fav_sweet
```
a) True  
b) False  
c) None  
d) Error

Question 4
What is the output of the following code?
```python
string = "CodeBasics"
print(string[:4].replace("Code", "Skill"))
```
a) CodeBasics  
b) SkillBasics  
c) Skill  
d) Code

Question 5
How to get the length of the string in Python?  
a) length()  
b) len()  
c) count()  
d) .length()

"""
#Open the Jupyter notebook and type this code help(str) in the code cell and press CTRL+enter. 
# Now see what it returns? 
# Go through these string methods and try to practice them.
first_name = "Pramod"
last_name = "IoT"

fullname = f'{first_name} {last_name}'

first_name = first_name.upper()
last_name = last_name.upper()   

first_name = first_name.lower()
last_name = last_name.lower()

first_name = first_name.capitalize()
last_name = last_name.capitalize()

name_format = fullname[0:].replace("IoT", "Jain")
print(name_format)


#Create two variables to store how many fruits and vegetables you eat in a day. 
# Now Print "I eat x vegetables and y fruits daily" where x and y present 
# vegetables and fruits that you eat every day. Use python f string for this.
vegetables = 2
fruits = 3

print(f"I eat {vegetables} vegetables and {fruits} fruits daily where {vegetables} and {fruits} present "
      f"vegetables and fruits that you eat every day.")


#Create a variable and store the string “The Himalayas are one of the youngest mountain ranges on the planet.”
# Print ‘The Himalayas’ using slice operator
# Print “mountain range” using a negative index
# Print “The Himalayas on the planet” using slice as well as f-string

sentence = "The Himalayas are one of the youngest mountain ranges on the planet."
print(sentence[:13])
print(sentence[-30:-15])
print(f"{sentence[:13]} {sentence[-15:]}")


#You have created a string variable called string= ”There are 9 planets in the solar system”. 
# After some time, you have realized that your sentence is incorrect and there are only 8 planets, 
# now correct your sentence by replacing the incorrect words. (Bonus: Try to do it in one line)
string = "There are 9 planets in the solar system"
string = string.replace("9", "8")
print(string)

print("There are 9 planets in the solar system".replace("9", "8"))




