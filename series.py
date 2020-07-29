import pandas as pd
ds = pd.Series([1,2,3,4])
df = pd.Series([1,2,3,4],index=[5,6,7,8])
dg = pd.Series([1,2,3,4],index=[5,6,7,8],name='Kill')
print(ds)
print(df)
print(dg)
