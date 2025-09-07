"""
1 - How big is your dataset
2 - what are the names of columns

shape and column
"""

import pandas as pd

data = {
    "Name":['Ravi','Shyam','Ghanshyam','Akash','Vedant' , 'Himesh', 'Rishab'  ],
    "Age" : [20,23,25,24,22,21,19],
    "Salary":[50000 , 60000 , 450000 ,52000 , 49000 , 48000 , 58000 ],
    "Performance Score":[85,90,78,92,88,95,80]
}

df = pd.DataFrame(data)
print(df)
print(f'shape:{df.shape}')
print(f'Columns Names:{df.columns}')