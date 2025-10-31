a="     helloo         agsd     "
print(a.lstrip(), a.rstrip()) 

#removes spaces from right side 
#removes spaces from left side

b=input("Name=")
c=input("City=")
print("i am {} i am from {}".format(b,c))

d="Hello guys! this is sait. I am a student at sait. sait is a wonderful college. sait is at ujjain HW, sait belongs for the freedom fighter, sait has many streams sait is new sait is old sait is mine sait is our sait has red color sait is in globe sait is in india sait is in mp"

print("sait is present:",d.count("sait"), d.index("sait"),)

sub = "sait"
i=d.find(sub)

if i==-1:
    print("not found")
while i!=-1 :
    print( "{} present at {} position".format(sub,i))
    i=d.find(sub,i+len(sub),len(d))