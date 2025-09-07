"""
NaN (Not a Number)
None (for object data types)

is null()
NaN is missing
False - value is present

"""

import pandas as pd 

data = {
    "Name":['Ravi','None','Ghanshyam','Akash','Vedant' , 'Himesh', 'Rishab'  ],
    "Age" : [20,23,None,24,22,21,19],
    "Salary":[50000 , 60000 , 450000 ,None , 49000 , 48000 , 58000 ],
    "Performance Score":[85,90,78,None,None,95,80] 
}

df = pd.DataFrame(data)

print(df.isnull())

#  Total missing value in the pandas :- 
print(df.isnull().sum())

# dropna()
# df.dropna(axis = 1 , inplace = True)

# fillna(0,inplace=True)
df.fillna(0 , inplace =True)
print(df)

df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)