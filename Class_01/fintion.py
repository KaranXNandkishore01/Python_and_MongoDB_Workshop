# Function is the self contained block.
def sum_sub(a,b):
    x = a+b
    y= a-b
    return x,y
a=int(input("A="))
b=int(input("B="))
c,d=sum_sub(a,b)
print("sum=",c)
print("sub=",d)

