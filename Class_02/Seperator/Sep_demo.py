a = "a5b6c3d9"
isalpha = a.isalpha()
isalnum = a.isalnum()
isdigit = a.isdigit()
islower = a.islower()

print(isalpha)
print(isalnum)
print(isdigit)
print(islower)


cur = ""
prv = ""
for i in a:
    if i.isalpha():
        cur=cur +i
        prv=i
    elif i.isdigit():
        cur=cur+prv*(int(i)-1)+ ","
print(cur)

# String Manipulation

s=input("Enter Some string=")
output=""
prev=""
for x in s:
    if x.isalpha():
     output=output + x 
     prev = x
    else:
        output=output + chr(ord(prev)+int(x))
    print(output)
    
# Remove duplicates from string
    
s=input("Enter Some string=")
output=""
prev=""
for x in s:
    if x not in output:
        output=output+x
print(output)
