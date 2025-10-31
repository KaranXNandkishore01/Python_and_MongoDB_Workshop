# Set  mein Indexing  aur Slicing  nahi hoti hai kyunki Set  unordered hota hai.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# z = x.difference(y)
z = x.intersection(y)
k = x.isdisjoint(y)
print("intersection:", z)
print("is disjoint:", k)

m = {1,2,3}
n = {3,4,5}
j = m.intersection(n)
l = m.isdisjoint(n)
print("intersection:", j)
print("is disjoint:", l)

# Bugs = logical mistake in the program.
# error = syntactical mistake in the program.
# exception = runtime mistake in the program.