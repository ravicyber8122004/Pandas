import pandas as pd

df = pd.read_json("sample_data.json")

print('Displaying the info of the data set')
print(df.info())