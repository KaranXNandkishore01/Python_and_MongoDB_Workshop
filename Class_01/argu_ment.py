#positional Arguments

def keyfun(name,msg):
    print("Welcome",name,msg)
    
keyfun(name="Karan",msg="Good Morning")
keyfun(msg="Good Morning",name="Prajapati")

def task_ii(name,address,mob,user_name, Password):
    print("Welcome",name,address,mob,user_name, Password)

task_ii(name="Karan, ",address="Delhi, ",mob="1234567890, ",user_name="karan123, ", Password="pass@123")
task_ii(address="Mumbai, ", name="Rajkumar, ",mob="0987654321, ",user_name="praja123, ", Password="pass@456")
task_ii(name="Prajapati, ",address="Chennai, ",mob="1122334455, ",user_name="prajapati123, ", Password="pass@789")
task_ii(name="Ramesh, ",address="Kolkata, ",mob="6677889900, ",user_name="ramesh123, ", Password="pass@000")
task_ii(name="Suresh, ",address="Bangalore, ",mob="4455667788, ",user_name="suresh123, ", Password="pass@111")

#Variable Length Arguments. 

def sum(*n):
    s=0
    for i in n:
        s=s+i
    print(s)
sum(10)
sum(10,20)
sum(10,20,30)
sum(10,20,30,40)
sum(10,20,30,40,50)

#Global and Local Variables
a=10
def f1():
    global a
    a=777
    print(a) 
    
def f2():
    a=1111
    print(a)
f1()  
f2()

# #Question
s=lambda n:n*n
print("The square of 4 is:",s(4))
print("The square of 5 is:",s(5))

# #Question
s=lambda a,b:a+b
print("The sum of 2 and 3 is:",s(10,20))
print("The sum of 100,200 is :", s(100,200))

# #Question
s=lambda a,b:a if a>b else b
print("The Biggest of 10,20 is:", s(10,20))
print("The Biggest of 100,200 is:", s(100,200))

def outer():
    print("outer function started")
    def inner():
     print("inner function execution")
    print("outer function calling inner function")
    inner()
outer()


x=6500
def add2(a,b):
    print("The Sum:",a+b)

def prod(a,b):
    print("The Prod:", (a*b))
    
def powl(a,b):
    print("The Powl:", (a*b))

import jmath as j
print(j.x)
print(j.add2(65,35))
print(j.powl(5,6))