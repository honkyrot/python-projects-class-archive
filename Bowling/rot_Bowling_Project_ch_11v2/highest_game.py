"""Small script for counting the highest scored game.
v1.0"""
import pathlib
import json

save_file = pathlib.Path("bowling_save.json")

if save_file.exists():
    loading_save_content = save_file.read_text()
    loading_save_data = json.loads(loading_save_content)
    game_number = 0
    max_scored_games = 0
    highest_score = 0
    for key, data in loading_save_data["game_history"].items():
        if data[1] >= highest_score:
            game_number = key
            highest_score = data[1]
        if highest_score >= 300:  # 300 is max so...
            max_scored_games += 1
    if max_scored_games > 0:
        print(f"There are {max_scored_games} games with the max score of 300!")
    else:
        print(f"Game: {game_number} has the highest score of {highest_score}!")
