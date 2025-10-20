import pandas as pd

df = pd.read_csv('./data.csv')
data = df.groupby('Product')['Quantity'].sum()
data = data.reset_index()
data.index = range(1, len(data) + 1)
data.to_csv('SalesOut.csv', index_label='id')
