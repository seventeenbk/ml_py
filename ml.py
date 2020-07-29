import pandas as pd
df = pd.read_csv("Bengaluru_House_Data.csv")
#use parameter index_col=0 in read_csv() to set 0th column of csv file as index of the DataFrame
print(df.shape)
print()
print(df.head())
