# #string can be written as '_',"_",""_"", '''_''', 

a ='hello'
b ="hi students"
c ='''This is a multi line string.
    It can span multiple lines.'''
d ="""This is also a multi line string.
It can also span multiple lines."""

print(type(a), type(b), type(c), type(d))

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

a='''indore is a "cool" city
indore is a big city'''

print(a[13:17][::-1])  #reverse string slicing
print(a[13:17])  #string slicing



