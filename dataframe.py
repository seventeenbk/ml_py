import pandas as pd
df = pd.DataFrame({'Karthik':[10,20],'Insane':[50,70]},index=['Marks1','Marks2'])
ds = pd.DataFrame({'Karthik':[10,20],'Insane':[50,70]})
print(df)
print(ds)
df.to_csv('test.csv')
