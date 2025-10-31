# what is the runtime Environment in python?
# The runtime environment is the state of the computer when a program is running. It includes the hardware, operating system, and any software libraries or dependencies that the program relies on.

a, b,c = 40,5,0
try:
    for i in range(1,10):
       c = a/b
       print("c:", c)
       b=b-1
    print("Hello Indoresdfgd")
    print("Hello Indoresdfgs")

except ZeroDivisionError:
    print("Except working")

print("Hello Indore")
print("Hello Indore")
print("Hello Indore")
print("Hello Indore")


# ************** Exception Handling  in Python **************

a, b,c = 40,0,0
i,j = 0,0
while i<10:
    try:
        try:
            for j in range (0,10):
                if i==j:
                    c = a/b
                    print(c)
                print(i)
        except ZeroDivisionError:
            i =i+1
        finally:
            i = i+1
    except Exception:
        i = i+1
    finally:
        i = i+1
    i = i+1
