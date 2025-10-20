from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.db_game
coll = db.game
coll.delete_many({})

games = [
    {
        "name": "most wanted", "genre": "racing", "rating": 95
    },
    {
        "name": "PUBG", "genre": "shooting", "rating": 98
    },
    {
        "name": "e football", "genre": "sports", "rating": 90
    },
    {
        "name": "RDR 2", "genre": "action", "rating": 97
    },
    {
        "name": "Minecraft", "genre": "Sandbox", "rating": 95
    }
]
coll.insert_many(games)


def display_game():
    all_games = coll.find()
    for game in all_games:
        print(f"{game['name']}\n")


def find_game():
    game_name = input("Enter the game name: ")
    game = coll.find_one({"name": game_name})
    if game:
        print(f"Found game: {game['name']} - {game['genre']} (Rating: {game['rating']})")
    else:
        print("Game not found")


def update_achievement():
    game_name = input("Enter the game to update achievement: ")
    result = coll.update_one(
        {"name": game_name},
        {"$set": {"achievements": ["Grandmaster", "Speed Demon"]}}
    )
    if result.modified_count > 0:
        print("Success! Achievement updated.")
    else:
        print("Game not found or no changes made")


def get_game_achievement():
    games_with_achievements = coll.find({
        "achievements": {"$all": ["Grandmaster", "Speed Demon"]}
    })
    count = 0
    for game in games_with_achievements:
        count += 1
        print(f"{game['name']} has both achievements: {game['achievements']}")

    if count == 0:
        print("No games found with both achievements")


while True:
    print("\n\n1. Display all games.\n"
          "2. Find a game.\n"
          "3. Update a game achievement.\n"
          "4. Return games with Grandmaster and Speed Demon achievements.\n"
          "5. Exit.\n")

    try:
        option = int(input("Enter an option: "))
    except ValueError:
        print("Please enter a number between 1 and 5")
        continue

    if option == 1:
        display_game()
    elif option == 2:
        find_game()
    elif option == 3:
        update_achievement()
    elif option == 4:
        get_game_achievement()
    elif option == 5:
        print("Exiting...")
        break
    else:
        print("Invalid option. Please select between 1 and 5.")