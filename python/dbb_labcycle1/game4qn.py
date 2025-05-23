import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["game"]
games = db["games"]

games.insert_many([
    { "name": "Game1", "genre": "Adventure", "rating": 90 },
    { "name": "Game2", "genre": "Action", "rating": 85 },
    { "name": "Game3", "genre": "Puzzle", "rating": 88 },
    { "name": "Game4", "genre": "Racing", "rating": 91 },
    { "name": "Game5", "genre": "RPG", "rating": 95 }
])




for game in games.find({}, {"_id": 0, "name": 1, "genre": 1}):
    print(game)

game4 = games.find_one({"name": "Game4"})
print(game4)

games.update_many(
    {"name": {"$in": ["Game1", "Game2"]}},
    {"$set": {"achievement": ["GameMaster", "SpeedDemon"]}}
)

for game in games.find({"achievement": {"$all": ["GameMaster", "SpeedDemon"]}}):
    print(game)
