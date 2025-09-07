"""
10
20
NaN
40
50

1000
2000
3000
4000
5000
6000
7000

linear 

1- Preserve data integrity
2- Smooth trends
3- Avoid data loss

interpolate

"""

import pandas as pd

data = {
    "Name":['Ravi','Shyam','Ghanshyam','Akash','Vedant' , 'Himesh', 'Rishab'  ],
    "Age" : [20,None,25,24,22,21,19],
    "Salary":[50000 , None , 450000 ,52000 , 49000 , 48000 , 58000 ],
    "Performance Score":[85,None,92,88,95,80]
}

df = pd.DataFrame(data)
print(df)

# linear , polynomial , time

df.interpolate(method = "linear" , axis = 0 , inplace = True)