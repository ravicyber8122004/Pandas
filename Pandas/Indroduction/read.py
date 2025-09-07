import pandas as pd

# read data from csv file inti a dataframe
df = pd.read_csv("file.csv", encoding="latin1")

# read the data from the excel file 
df = pd.read_excel("Map_App_Tasksheet.xlsx")

print(df)

# gcsfs # these library are used to read the cloud platform data 
