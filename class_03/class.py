# Here I import re module for regular expressions, whihch is used later in the code.
import re
class Student:
    def talk(self):
        print("Hello, I am Karan.")
s1 = Student()
s1.talk()
class Outer:
    def __init__(self):
        print("Outer class object creation")
    class Inner:
        def __init__(self):
           print("Inner class object creation")
        class InnerMost:
           def Inmost(self):
               print("InnerMost class object creation")
        def m1(self):
           print("Inner class method.")
ob = Outer()
i = ob.Inner()
im = i.InnerMost()
im.Inmost()

#Here I import time module to use sleep function for delaying the execution of the program.

import time
class Test:
    def __init__(self):
        print("Constructor executed")
    def __del__(self):
        print("Destructor executed")
list = [Test(), Test(), Test()]
del list
time.sleep(5)
print("End of an application") 

class Demo:
    def __init__(self, a=None,b=None,c=None):
        print("value of {} is value of {} is value of {} is".format(a,b,c))
d0 = Demo()
d1 = Demo(10)
d2 = Demo(10,20)
d3 = Demo(10,20,30)
d4 = Demo(c=30,b=20,a=10,d=40)
d5 = Demo(b=20,a=10)

# Validation of mobile number, email id and vehicle number using regular expressions

import re
n=input("Enter Your Mobile Number:")
m=re.match(r"[7-9]\d{9}", n)
if m!=None:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
   
import re
email=input("Enter Your Email ID:") 
EM = re.match("[a-zA-Z0-9_.]*@gmail[.]com", email)
if EM!=None:
    print("Valid Email ID")
else:
    print("Invalid Email ID")

s= input("Enter your vehicle number:")
v = re.match("MP[012][0-9][A-Z]{2}\d{4}", s)
if v!=None:
    print("Valid Vehicle Number")
else:
    print("Invalid Vehicle Number")