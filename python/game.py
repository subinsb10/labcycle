import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["gamestore"]

games = db["games"]

for x in games.find({},{"name":1, "_id":0, "genre":1}):
   print(x)


k



lis = games.find_one({"name":"Game4"})
print(lis)




sett1 = {"$set":{"achievement":["GameMaster","SpeedDemon"]}}
games.update_many({"name" :{"$in" :["Game1","Game2"]}},sett1 )




query = {"achievement":["GameMaster","SpeedDemon"]}
for a in games.find(query):
    print(a)