"""
Write a python script to convert an integer value into a bool value
"""

# to convert an integer value into bool value
# we uses a "bool()" function
# which evaluates -

"""
1.  Non-zero value as True
2.  zero as Flase
3.  Non-empty string as True
4.  Empty string as False
"""

# printing corresponding value of specified argument of "bool()" function
print("Non-zero \"bool(234)\" value as True =>", bool(234))
print("Zero \"bool(0)\" as False =>", bool(0))
print("Non-empty string \"bool('onkar')\" as True =>", bool("onkar"))
print("Empty string \"bool('')\" as False =>", bool(""))