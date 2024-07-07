x = input ('Enter a number 1: ')
y = input ('Enter a number 2: ')

# handling exception
try:
    z = int(x) / int(y)
except Exception as e:
    print ("Exception Occured:",e)    
    z = None

print ("division is:",z)

# handling exception using specific exception
try:
    z = int(x) / int(y)
    a = 'a' + 1
    

except ZeroDivisionError as e:
    print ("Exception Occured:",e)    
    z = None

except TypeError as e:
    print ("Exception Occured:",e)    
    z = None

except Exception as e:
    print ("Generic exception occured:",e)    
    z = None    

print ("division is:",z)



