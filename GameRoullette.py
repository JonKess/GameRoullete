import random 
import os
import operator





#Path to Steam library
steam_library ="D:\SteamLibrary\steamapps\common"
library = [] # List of games in the steam library
picked = {} # Dictionary to keep track of how many times each game is picked

# Loop through the list of games and add them to the library list
for foldername in os.listdir(steam_library):
    if os.path.isdir(os.path.join(steam_library, foldername)):
         # Get the game title by removing the path and file extension
        game_title = os.path.splitext(os.path.basename(foldername))[0]
         # Add the game to the dictionary with an initial count of 0
        library.append(game_title)
        picked[game_title] = 0


while True:
    game = random.choice(library)

    picked[game] = picked.get(game, 0) + 1 # Increment the count for the picked game

    # print(game, 'picked', picked[game], 'times')
    if picked[game] == 5:
        print(game, 'is the game to play')
        break
# This shows the results of some of the games picked and orders them from most to least    
sorted_games = sorted(picked.items(), key=operator.itemgetter(1), reverse=False)

print("RUNNER UP GAMES")
# You want the count in close range to the max so the whole library does not print
for game, count in sorted_games:
    if count < 5:
        if count >= 3:
            print(f"{game}: {count}")



# Also think of a way to order the games from most -> least picked
# For when I organize my games by multiplayer and singleplayer

# single_player_library = [] # List of single player games in the steam library
# multi_player_library = [] # List of multiplayer games in the steam library
# picked = {} # Dictionary to keep track of how many times each game is picked

# # Loop through the list of games and add them to the library list
# for foldername in os.listdir(steam_library):
#     if os.path.isdir(os.path.join(steam_library, foldername)):
#         # Get the game title by removing the path and file extension
#         game_title = os.path.splitext(os.path.basename(foldername))[0]
#         # Check if the game is in the multiplayer folder
#         if 'multiplayer' in foldername.lower():
#             multi_player_library.append(game_title)
#         else:
#             single_player_library.append(game_title)
#         # Add the game to the dictionary with an initial count of 0
#         picked[game_title] = 0












