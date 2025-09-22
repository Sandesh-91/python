try:
    print(x)
except:
    print("An error occured")
finally:
    print("try and except block finished: ")

#we can raise exception ourselves in python

x = -5
if x < 0:
    raise ValueError("Negative numbers not allowed")

"""
ValueError-int("abc")
TypeError-"5"+3
NameError-variable not defined
ZeroDivisionError
AttributeError
FileNotFoundError   """