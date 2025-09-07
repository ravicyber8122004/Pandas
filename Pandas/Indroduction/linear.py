import pandas as pd

data = {
    "Time": [1,2,3,4,5],
    "Value":[10,None,30,None,50],
}

df = pd.DataFrame(data)
print("Before interpolation")
print(df)

print("After interpolation")
print(df)

"""
1- Timer series data
2- Numeric data with trends
3- Avoid dropping rows
"""