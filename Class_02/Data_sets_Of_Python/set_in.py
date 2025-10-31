#set is unordered collection of unique elements.it is mutable
#it is represented by {}

# write a code to find the prime numbers from 1 to 100 and store them in a set

list=[ 12, 11,7,5,3,2,1,4,6,8,9,10,13,14,15]
for i in list:
    if i>1:
        for j in range(2,i):
            if(i%j)==0: 
                break
        else:
            print(i)

# Modification in sets in python
s={1,2,3,4,5}
s.add(6) # adding element to set
print(s)

s.remove(3) # removing element from set
print(s)

s.discard(4) # removing element from set
print(s)

s.pop() # removes an arbitrary element from the set
print(s)

s.clear()   # removes all elements from the set
print(s)

# set operations in python
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2)) # union of two sets

print(s1.intersection(s2)) # intersection of two sets
print(s1.difference(s2)) # difference of two sets
print(s2.difference(s1)) # difference of two sets
print(s1.symmetric_difference(s2)) # symmetric difference of two sets
print(s1.issubset(s2)) # check if s1 is subset of s2
print(s1.issuperset(s2)) # check if s1 is superset of s2
print(s1.isdisjoint(s2)) # check if s1 and s2 are disjoint sets
print(s1.copy()) # copy of set s1
print(len(s1)) # length check karne ke liye.

# frozenset in python
# it is immutable version of set
fs=frozenset([1,2,3,4,5])
print(fs)
# fs.add(6) # will give error as frozenset is immutable
print(fs.union({6,7,8})) # union of frozenset and set
print(fs.intersection({4,5,6,7,8})) # intersection of frozenset and set
print(fs.difference({4,5,6,7,8})) # difference of frozenset and set
print(fs.symmetric_difference({4,5,6,7,8})) # symmetric difference of frozenset and set

print(len(fs)) # length check karne ke liye.
