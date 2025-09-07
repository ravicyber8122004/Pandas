"""
# Aggregation Function :-
df["Column Name"].mean()
df["Column Name"].sum()
df["Column Name"].min()
df["Column Name"].max()
df["Column Name"].count()
df["Column Name"].std()
"""

import pandas as pd

data = {
    "Name" :['Arun' , 'Varun' , 'Karan'],
    "Age" : [10,20,30],
    "Salary" :[10000 , 20000 , 30000]
}
df = pd.DataFrame(data)

avg_salary = df['Salary'].mean()
print(f"Average Salary is: {avg_salary}")

max_salary = df['Salary'].max()
print(f"The Maximum salary is : {max_salary}")

min_salary = df['Salary'].min()
print(f"The minimum salary is: {min_salary}")

sum_salary = df['Salary'].sum()
print(f"The sum of all person salary: {sum_salary}")