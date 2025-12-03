from ssl import CHANNEL_BINDING_TYPES
import pandas as pd
s= pd.Series([i for i in range(100)])
def odd_selection(s):
    return [True if i%7==0 else False for i in range(s.size)]
print(s[odd_selection])

# Consider the series:
# sunny 1000
# bunny 2000
# chinny 3000
# vinny 4500
# pinny 6000
# dtype : int64

j = pd.Series(data =[1000,2000,3000,4500,6000],index=['sunny','bunny','chinny','vinny','pinny'])
print(s[lambda s:[True if sal>=2500 and sal<=5000 else False for sal in s]])
print(s[lambda s: [True if sal in range(2500,5002) else False for sal in s]])

s1 = pd.Series(data=[10,20,30,40,60],index=['A','B','C','D','E'])
s2 = pd.Series(data=[10,20,30,40,50],index=['C','D','E','F','G'])
print("here")
print(s1.sub(s2))
print(s1.sub(s2,fill_value=0))

print(s1.mul(s2))
print(s1.mul(s2,fill_value=0))

print(s1.div(s2))
print(s1.div(s2,fill_value=0))