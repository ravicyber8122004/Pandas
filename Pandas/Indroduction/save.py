import pandas as pd

data={
    "Name":['Ram' , 'Shyam' , 'Ganshyam'],
    "age" : [10,20,30],
    "city" : ['Nagpur' , 'Mumbai' , 'Delhi']

}

df = pd.DataFrame(data)
print(df)


# output.to_<filetype>("<FileName>")
df.to_csv("output.csv" , index=False)

# .head(x) is used for display x rows from the upper side // by default x=5
print(df.head(1))

# .tail(x) is used for display x rows from the bottom side // by default x=5
print(df.tail(1))