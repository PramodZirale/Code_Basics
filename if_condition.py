""" 
Q1.Range for a normal blood pressure is 80 to 120 (including 80 and 120). 
Assume patient's blood pressure is stored in a variable called bp, select
the correct if condition that will perform a check if it is normal

a) if bp >= 80 or bp <= 120:

b) if bp > 80 or bp < 120:

c) if bp >= 80 and bp <= 120:

d) if bp >= 80 &&& bp <= 120

Q2. A score of 80 or more is a grade A. Less than 80 is grade B. How is this expressed in Python?

a) grade = if score > 80 "A" then "B"

b) grade = if score > 80 "A" else "B"

c) grade = "A" if score > 80 else "B"

d) grade = "A" if score >= 80 else "B"

Q3. You bought a watch from a company called banana in the past and had a bad experience.
    Now you have decided to buy a watch from any company except banana. 
    If a company name is stored in a variable called company, what will be the condition to perform this check?

a) if company != 'banana':

b) if company not 'banana':

c) if company not equal to 'banana':

d) if company == 'banana':


"""

n = input("Enter a number: ")

n = int(n)

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


indian = ["samosa", "daal", "naan", "paneer", "aloo", "gobi"]
chinese = ["role", "pot sticker", "fried rice", "dumpling", "spring roll"]
italian = ["pizza", "pasta", "risotto", "panzanella", "lasagna"]

dish = input("Enter a dish name: ")

if dish in indian:
    print(f" {dish} is Indian")
elif dish in chinese:
    print(f" {dish} is Chinese")
elif dish in italian:
    print(f" {dish} is Italian")
else:
    print("Not found")
    
    
    
# 1] Write a program that can tell you your BMI Category.
# Ask user to enter height in Meter
height = input("Enter height in Meter: ")    
# Ask user to enter weight in KG
weight = input("Enter weight in KG: ")
# Calculate the BMI(Body Mass Index) = weight /(height)**2 and store it in a variable
BMI = int(weight) / (int(height) ** 2)

# If the BMI is 30 or greater, print “Obesity”
if BMI >= 30:
    print("Obesity")
# If the BMI is in between 25 and 29, print “Overweight”
elif BMI >= 25 and BMI < 29:
    print("Overweight")
# If the BMI is in between 18.5 and 25, print “Normal”
elif BMI >= 18.5 and BMI < 25:
    print("Normal")
# If the BMI is less than 18.5, print “Underweight”
elif BMI < 18.5:
    print("Underweight")
else:
    print("Invalid input")


# 2] Using the following list of cities per country,
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]
# Write a program that asks the user to enter a city name, and it should tell which country the city belongs to
city = input("Enter a city name: ")

if city in India:
    print(f"{city} is in India")
elif city in USA:
    print(f"{city} is in USA")
elif city in UK:
    print(f"{city} is in UK")
else:
    print("City not found")    


# Write a program that asks users to enter two cities, and it tells you if they both are in the same country or nor />
  # For example:
  # If I enter Mumbai and Chennai, it will print "Both cities are in India" but if I enter Mumbai and New York it should print "They don't belong to the same country"

cities = input("Enter two cities: ").split('and')    
city1 = cities[0]
city2 = cities[1]

city1 = city1.strip()
city2 = city2.strip()

if city1 in India and city2 in India:
    print("Both cities are in India")
elif city1 in USA and city2 in USA:
    print("Both cities are in USA")
elif city1 in UK and city2 in UK:
    print("Both cities are in UK")
else:            
    print("They don't belong to the same country")
