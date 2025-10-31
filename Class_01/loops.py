# Loops in Python

# For Loop
print("For Loop:")

for i in range(0,10):
    for j in range(1,11-i):
        print(j, end="")
    print("")
    
# While Loop
print("While Loop:")
i=0
while i<10:
    j=1
    while j<=10-i:
        print(j, end="")
        j=j+1
    print("")
    i=i+1
    
    
# Nested Loop
print("Nested Loop:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"({i}, {j})", end=" ")
    print("")
    
# Loop Control Statements
print("Loop Control Statements:")
for i in range(1, 11):
    if i == 5:
        print("Skipping 5")
        continue
    if i == 8:
        print("Breaking at 8")
        break
    print(i)
    
# Using else with Loops
print("Using else with Loops:")
for i in range(1, 6):
    print(i)
else:
    print("Loop completed without break")
    
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("While loop completed without break")
# Using pass statement in Loops
print("Using pass statement in Loops:")
for i in range(1, 6):
    if i == 3:
        pass  # Placeholder for future code
    print(i)
    
print("End of Loops demonstration.")