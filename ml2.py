import pandas as pd
df = pd.read_csv("Bengaluru_House_data.csv")
print(df.shape)
#print(df.head())
#print(df["area_type"].head())
#print(df.area_type.head())
#print(df["location"][6])

#indexing elements, row first, column second
#print(df.iloc[2])
#print(df.iloc[:,4])
#print(df.iloc[1:11,5])
#print(df.iloc[1:10:2,5])
#print(df.iloc[-1:-10:-2,5])
#print(df.loc[:,["bath","balcony","price"]].head()) #label-based indexing

#iloc is non-inclusive of the last index value, whereas loc is inclusive of the last index value
#otherwise there's no difference
df.set_index("balcony")
print(df.head())
