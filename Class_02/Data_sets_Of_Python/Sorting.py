# What is sorting in Python?
#Sorting in Python is the process of arranging the elements of a list or any other iterable in a specific order, either ascending or descending. Python provides built-in functions and methods to perform sorting operations easily.


#sorting based on first element

a =[[3,4],[1,2],[5,6]]
a.sort(key=lambda x:x[0])
print(a)

#sorting based on second element

a =[7,4,1,2,5,6]
a.sort(key=lambda x:x[1])
print(a)

# Modification in the list while sorting

stack = [3,4,5,6]
stack.append(7)
print(stack)
stack.pop()
print(stack)

#list as Queue

from collections import deque
queue = deque(["indore","ujjain","mumbai"])
queue.append("delhi")
print(queue)
'indore'
queue.popleft()
'ujjain'
print(queue)

#want to create a list of squares of first 10 numbers

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
    
#want to create a list of squares of first 10 numbers using lambda

squares = []
squares = list(map(lambda x:x**2, range(10)))
print(squares)

squeares = [x**2 for x in range(11)]
print(squares)

k=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
del k[2:5]
print(k)