import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["game"]
games = db["games"]

# games.insert_many([
#     { "name": "Game1", "genre": "Adventure", "rating": 90 },
#     { "name": "Game2", "genre": "Action", "rating": 85 },
#     { "name": "Game3", "genre": "Puzzle", "rating": 88 },
#     { "name": "Game4", "genre": "Racing", "rating": 91 },
#     { "name": "Game5", "genre": "RPG", "rating": 95 }
# ])




print(*games.find({}, {"_id": 0, "name": 1, "genre": 1}), sep="\n")

print(games.find_one({"name": "Game4"}))

games.update_many({"name": {"$in": ["Game1", "Game2"]}},
                  {"$set": {"achievement": ["GameMaster", "SpeedDemon"]}})

print(*games.find({"achievement": {"$all": ["GameMaster", "SpeedDemon"]}}), sep="\n")