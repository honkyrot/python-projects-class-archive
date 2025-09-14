"""Recreated/Rewrote bowling, by Hong Rot
2 Files are needed, this file and bowling_core
test_bowling.py and highest_game.py is optional.
Best read if you have a mono-type font.

NOT RECOMMENDED TO BATCH RUN OVER 1000 TIMES.
SAVING STILL NEEDS TO BE MORE EFFICIENT.
CURRENTLY GAME SAVES & LOADS AFTER EVERY LOOP.

v5.7
Version history
v1.0 - Bowling.
v2.0 - Refactoring and saving
v3.0 - Attempted to do TDD on bowling, ending up rewriting whole thing.
v4.0 - Rewritten bowling, but in one file.

v5.0 - Rewrote script and structure
v5.1 - Added more tests and fixed that scoring bug
v5.2 - Added game history to save file, yay data.
v5.3 - Added a batch run, useful for mass data.
v5.4 - fixed more scoring issues
v5.5 - fixed spare mark
v5.6 - more scoring fixes
v5.7 - new fun script
"""
import json
import pathlib
import time

import bowling_core as BowlingGame

save_file = pathlib.Path("bowling_save.json")


def read_loaded_save():
    loading_save_content = save_file.read_text()
    loading_save_data = json.loads(loading_save_content)
    for key, data in loading_save_data["game_history"].items():
        data_clone_score = str(data[1])
        data_clone_game = str(key)
        if len(data_clone_game) == 1:
            data_clone_game = "00" + data_clone_game
        elif len(data_clone_game) == 2:
            data_clone_game = "0" + data_clone_game
        if len(data_clone_score) < 3:
            data_clone_score = "0" + data_clone_score
        print(f"Game: {data_clone_game} - Score: {data_clone_score} - {data[0]}")


def y_n_response(input_message):
    while True:
        start_input = input(input_message).lower()
        if start_input == "y":
            return True
        elif start_input == "n":
            return False


user_play = y_n_response("Do you want to play bowling? (y/n)\n>")
if user_play:
    user_manual = y_n_response("Do you want to have manual input on score? (y/n)\n>")
    user_show_debug = y_n_response("Do you want to see debug messages (prevents saving)? (y/n)\n>")
    user_auto = False
    user_batch_auto = False
    if not user_manual:
        user_auto = y_n_response("Do you want to auto run this? (y/n)\n>")
    if user_auto:
        user_batch_option = y_n_response("Do you want to batch run this (y/n)?\n>")
        if user_batch_option:
            try:
                user_batch_auto = int(input("Please type the amount to loop this.\n>"))
            except ValueError:
                print("Please enter a number next time!")
    if not user_show_debug:
        save_file = pathlib.Path("bowling_save.json")
        if not user_show_debug:
            if save_file.exists():  # Check if save exists
                print("\nSave file detected.")
                save_choice = input("[L]oad file or [D]elete save\n>").lower()
                while save_choice != "l" and save_choice != "d":  # If user wishes to delete save.
                    save_choice = input("[L]oad file or [D]elete save\n>").lower()
                if save_choice == "l":  # Load Save File
                    print("\nLoading save file\n")
                    time.sleep(1)  # Artificial wait
                elif save_choice == "d":  # Delete save file!
                    print("\nDeleting save file!\n")
                    save_file.unlink()
                    time.sleep(1)  # Artificial wait
                    print("Save file deleted! Continuing to game!\n")
                    save_data = {"current_game": 0, "total_score": 0, "game_history": {}}
                    content = json.dumps(save_data)
                    save_file.write_text(content)
            else:
                print("No save file detected, saving to new file.")  # Make a new file to save on.
                save_data = {"current_game": 0, "total_score": 0, "game_history": {}}
                content = json.dumps(save_data)
                save_file.write_text(content)
            read_save_file = y_n_response("Read game history so far? (y/n)\n>")
            if read_save_file:
                read_loaded_save()
            input("\nPlease press enter to continue.\n")
    game_is_active = True
    print("\nStarting game!\n")
    while game_is_active:
        game = BowlingGame.BowlingGame()
        game.load_game()
        game.current_game += 1
        while not game.end_game:
            print(game.get_game_stats_mini())
            user_input_score = None
            if user_show_debug:
                game.print_debug()
            if not user_manual and not user_auto:
                input("[Enter] to roll ball.")
                print("\nRolling ball...\n")
            elif user_manual and not user_auto:
                while True:
                    try:
                        user_input_score = int(input("\nInput pins knocked down.\n>"))
                    except ValueError:
                        print("\nPlease input a number!")
                    else:
                        break
            game.roll_ball(user_input_score)
            print()
        print("Ending game!")
        print(game.get_game_stats_full())
        game.save_scoreboard()
        user_continue = True
        if user_show_debug:
            game.print_debug()
        if user_batch_auto == 0:
            user_continue = y_n_response("Continue bowling? (y/n)\n>")
        else:
            user_batch_auto -= 1
        if not user_show_debug:
            game.save_game()
        if not user_continue:
            print("Ending bowling.")
            read_save_file = y_n_response("Read game history so far? (y/n)\n>")
            if read_save_file:
                read_loaded_save()
            game_is_active = False
    print("Goodbye!")
else:
    print("Goodbye!")
