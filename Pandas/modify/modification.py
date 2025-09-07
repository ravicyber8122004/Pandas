import pandas as pd

data = {
    "Name":['Ravi','Shyam','Ghanshyam','Akash','Vedant' , 'Himesh', 'Rishab'  ],
    "Age" : [20,23,25,24,22,21,19],
    "Salary":[50000 , 60000 , 450000 ,52000 , 49000 , 48000 , 58000 ],
    "Performance Score":[85,90,78,92,88,95,80]
}

df = pd.DataFrame(data)
print(df)

# adding column in dataframe df["Column_Name"]= some_data
df["Bonus"] = df["Salary"]*0.1
print(df)

# using insert()
# df.insert (loc , "Column_Name , some_data")
df.insert(0,"Employee ID",[10,20,30,40,50,60,70])
print(df)


# => Updating values in a dataframe :- 

# .loc[row_index , "Column Name"] =new_value
df.loc[0,'Salary'] = 55000
print(df)

# increasing salary by 5%
df['Salary'] = df['Salary']*1.05

print(df)


# => Removing Column from the dataframe 
# df.drop(columns = ["Columns_Name1", "Columns_Name1".....], inplace = True)

df.drop(columns=["Performance Score"] , inplace=True)

print(df)