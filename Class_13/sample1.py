import pandas as pd

import numpy as np
lst = ["indore", "mumbai", "pune"]
sr = pd.Series(lst)
print(type(sr))
print(sr)


lst2 = [1,3,4,2,5]
st = pd.Series(lst2)
print(type(st))
print(st)


dict = { "a":1, "b":3, "c":34}
dsr = pd.Series(dict)
print(type(dsr))
print(dsr)


arr = (1,2,3,44,5,66,7,8)
# Create an array
exm = { 2,3,4,5,6,7}
# asr = np.series(arr)



lt =["sunny","bunny","chinny"]
srd = pd.series(lt , index ="a")
print(type(srd))
print(srd)
