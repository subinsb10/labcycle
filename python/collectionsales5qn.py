import pymongo
import pandas as pd
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["store"]

store = db["store"]
data = store.find()
datalist = list(data)
df = pd.DataFrame(datalist)
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.to_period('M')
df['date'] = df['date'].astype(str)
df['revenue'] = df['quantity']*df['price']
monthrev = df.groupby(['store','date'])['revenue'].sum()
monthrev = monthrev.reset_index()
print(monthrev)
store2 = db['store2']
monthrev = monthrev.to_dict(orient='records')
store2.insert_many(monthrev)