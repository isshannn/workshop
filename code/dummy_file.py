a = 100
b = 200
# swap values of a and b in as many ways as possible

"""
Using temporary variable 
"""
temp = a
a = b
b = temp
print("Using temporary variable: \n a = ", a, "b =",b)

"""
Without using a thrid variable
"""
a = 100
b = 200
a = a + b
b = a - b
a = a - b
print("Without using a thrid variable: \n a =", a, " b = ",b)

# Using set
(a,b) = (100,200) 
(a,b) = (b,a)
print("Using set: \n a =", a, " b = ",b)

# Using xor operator? To be explored

# Using arry sway
a = 100; b =200
arr = [a,b]
arr.reverse()
# print(arr2)
print(arr)

import datetime
class newspaper():
    name: str
    print_date: datetime.date
    edition: str
    pages: int
    addendum: bool
    
# class <my_abstract_class>:
    # pass