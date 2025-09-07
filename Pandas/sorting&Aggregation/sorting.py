"""
# sorting data
# SORTING DATA 1 COLUMN sort_values

df.sort_values(by="Column Name" , True/False , inplace = True)
"""

import pandas as pd

data = {
    "Name" :['Arun' , 'Varun' , 'Karan'],
    "Age" : [10,20,30],
    "Salary" :[10000 , 20000 , 30000]
}


df = pd.DataFrame(data)
print("Before the sorting the data")
print(df)


df.sort_values(by="Age" , ascending=False , inplace=True)
# df.sort_values(by=["Age","Salary"] , ascending=False , inplace=True)
# df.sort_values(by=["Age","Salary"] , ascending=[True ,False] , inplace=True)


print("After the sorting the data is:")
print(df)