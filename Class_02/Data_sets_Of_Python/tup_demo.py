k = (12, 34, 56, 78)
print("Length", len(k))
print("Max", max(k))
print("Min", min(k))
print("Sum", sum(k))
print("Count of 34", k.count(34))
print("Index of 56", k.index(56))
print("Sorted", sorted(k))

#Joing of string with tuple
t = ('sunny', 'bunny', 'chinny')
s='-'.join(t)
print(s)

#second largest element in tuple by max function
t = [12, 34, 54, 78, 78,72,90]
p = max(t)
r = t[0]
for k in t:
    if r<k and k!=p:
        r=k
    elif r==p:
        r=k
print(r)

#tuple packing and unpacking
t = (1,2,3)
a,b,c = t
print(a)
print(b)
print(c)

#nested tuple
n = (1,2,(3,4), (5,6))
print(n[2][1])  # prints 4
print(n[3][0])  # prints 5

#tuple with single element
t1 = (5,)
print(type(t1))  # prints <class 'tuple'>
t2 = (5)
print(type(t2))  # prints <class 'int'>

#tuple concatenation

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)  # prints (1, 2, 3, 4, 5, 6)

#tuple repetition

t1 = (1,2,3)
t2 = t1 * 3
print(t2)
# prints (1, 2, 3, 1, 2, 3, 1, 2, 3)

#slicing of tuple
t = (1,2,3,4,5,6,7,8,9)
print(t[2:5])  # prints (3, 4, 5)
print(t[:4])   # prints (1, 2, 3, 4
print(t[5:])   # prints (6, 7, 8, 9)
print(t[-5:-2]) # prints (5, 6, 7)
print(t[::-1])  # prints (9, 8, 7, 6, 5, 4, 3, 2, 1)
print(t[::2])  # prints (1, 3, 5, 7, 9)
print(t[1::2])  # prints (2, 4, 6, 8)
print(t[-1::-1])  # prints (9, 8, 7, 6, 5, 4, 3, 2, 1)
print(t[-2::-2])  # prints (8, 6, 4, 2)
print(t[-3::-3])  # prints (7, 4, 1)

#tuple methods
t = (1,2,3,4,2,5,2)
print(t.count(2))  # prints 3 index ke according count karta hai

print(t.index(4))  # prints 3 index ke according position dikhata hai

print(t.index(2))  # prints 1 first occurrence ka index dikhata hai

print(t.index(2,2))  # prints 4 start index se search karta hai