import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/sales.csv')
data = df.groupby('product')['quantity'].sum()
print(data)
data = data.reset_index()
data.index = range(1, len(data) + 1)
data.to_csv('Sales.csv', index_label='id')
print(data)