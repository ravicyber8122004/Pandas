"""
vartically (row-wise)
horizontally (column wise)

pd.concate([df1 , df2] , axis = 0 , ignore_index = True)

[df1 , df2] = merge both data 
axis = 1

ignore_index = True
"""

# vertically

import pandas as pd 

df_Region1 = pd.DataFrame({
    'CustomerID' : [1,2],
    'Name' : ['Gopal' , 'Raju']
})

df_Region2 = pd.DataFrame({
    'CustomerID':[3,4],
    'Name':['Shyam','Baburao']
})

# concatenate vartically

df_concat = pd.concat([df_Region1 , df_Region2] ,axis=1 , index = False)
print(df_concat)