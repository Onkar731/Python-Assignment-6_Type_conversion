"""
Write a python script to convert a str type data into an int type.
Also describe when a str type value is not possible to convert into an int type.
"""

# to convert "str" type value into "int" type
# we uses a function called - "int()" function
# which accepts "number string" as an argument and returns "int" value
int_var = int("234")
print("str type into int type =>", int("234"),"\nType of converted value is =>", type(int_var))


# describing when a str type value is not possible to convert into an int type

"""
1.  "int()" function converts specified string argument into int type value when specified 
    string is of "number string" i.e. "234", "685", "20439" etc.

2.  When the specified string value is of other than "number string" i.e. "23ab", "abc", "abd349sd"
    then "int()" function will given an error message - "ValueError".
    OR
    "int()" function only accepts "number string" as an argument, if we provide invalid 
    string as an argument, it will generate "ValueError".
    
3.  Thus, it proves that "int()" function cannot convert all type of string into an "int"  

"""