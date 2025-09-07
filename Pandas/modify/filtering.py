"""
1 - Square brackets
2 - boolean conditions

Selecting Columns
1 - a series
2 - dataframe multiple columns of data

comlumn = df["Column Name"]
subset = df["Column1" , "Column2" , Column3,"...."]

filtering rows
boolean indexing

# based on a single condition
filtered_Rows = df[df["Salary"]>50000]

# combine multiple conditions
filtered_Rows = df[(df["Column"]>value)&(df["Column2"]<80000)]
"""

# Column filter

import pandas as pd

data = {
    "Name":['Ravi','Shyam','Ghanshyam','Akash','Vedant' , 'Himesh', 'Rishab'  ],
    "Age" : [20,23,25,24,22,21,19],
    "Salary":[50000 , 60000 , 450000 ,52000 , 49000 , 48000 , 58000 ],
    "Performance Score":[85,90,78,92,88,95,80]
}

df = pd.DataFrame(data)

print("Sample Dataframe")
print(df)
print("Names (Single column return series)")
Name = df['Name']
print(Name)
subset = df[["Name" , "Age"]]
print('\nSubset with Name and age')
print(subset)

# Rows filter 

high_salary = df[df['Salary']>50000]
print("Employees with salary > 50000")
print(high_salary)

filtered = df[(df['Age']>30) & (df['Salary']>50000)]
# print(f'Employee list Age > 30 + Salary >50000')
print(filtered)

or_filtered = df[(df['Age']>30) | (df['Salary']>50000)]
print(or_filtered)