a='raj'
b="raj"
print(a>b)

a=200
b=200
c=200
d=200
print( type(a), id(a))
print( type(b), id(b))
print( type(c), id(c))
print( type(d), id(d)) 
c=300
print( type(c), id(c))   

#even and odd;
a=int(input("enter a number:"))
# even and odd
if a&1:
    print("a is odd")
else:
    print("a is even:")
    
for i in range(1,11):
    for j in range(1,11):
        print(j, end="")
    print("")