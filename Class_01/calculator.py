def Cal_culate(a,b):
    x=a+b
    y=a-b
    z=a//b
    m=a*b
    return x,y,z,m
a=int(input("A="))
b=int(input("B="))
m=Cal_culate(a,b)
for i in m:
    print(i)