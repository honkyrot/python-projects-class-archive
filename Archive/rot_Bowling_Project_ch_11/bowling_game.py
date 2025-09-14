import Saving_Bowling_v3
from Saving_Bowling_v3 import clamp
import pathlib
import json
import time

sleep_time_wait = 0  # Used for rolling time artificial wait.


def quit_game():
    while True:  # Forced user input on rolling or quitting.
        if not manual_input:
            q_roll_input = input("Roll ball (y) or [Q]uit\n>").lower()
            if q_roll_input == "yes" or q_roll_input == "y":
                return True
            elif q_roll_input == "q":
                return False
        else:
            q_manual_input = input("Enter the pins you hit: \n>")
            try:
                q_manual_score = int(q_manual_input)
            except ValueError:
                print("Enter a number!")
            else:
                return q_manual_score

def quick_roll(manual_score_set):
    print("\nRolling ball...\n")
    time.sleep(sleep_time_wait)
    game.roll_ball(manual_score_set)


play_input = input("Would you like to play bowling? (y/n)\n>").lower()
while play_input != "yes" and play_input != "y" and play_input != "no" and play_input != "n":
    play_input = input("Would you like to play bowling? (y/n)\n>").lower()
if play_input == "yes" or play_input == "y":  # START
    active = True
    debug_options = False
    show_debug = input("Show debug options? (deletes save)(y/n)\n>").lower()
    while show_debug != "n" and show_debug != "y":
        show_debug = input("\nWould you want to manually input your scores? (y/n)\n>").lower()
    if show_debug == "y":
        debug_options = True
    manual_input = False
    run_manual_input = input("\nWould you want to manually input your scores? (y/n)\n>").lower()
    while run_manual_input != "n" and run_manual_input != "y":
        run_manual_input = input("\nWould you want to manually input your scores? (y/n)\n>").lower()
    if run_manual_input == "y":
        manual_input = True
    auto_play = False
    if not manual_input:
        run_auto_input = input("\nWould you like to auto-run this? (y/n)\n>").lower()
        while run_auto_input != "yes" and run_auto_input != "y" and run_auto_input != "no" and run_auto_input != "n":
            run_auto_input = input("Would you like to auto-run this? (y/n)\n>").lower()
        if run_auto_input == "yes" or run_auto_input == "y":  # Auto run, used for quick tests.
            auto_play = True
        else:
            sleep_time_wait = .5
    save_file = pathlib.Path("bowling_save.json")
    if not debug_options:
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
                print("Save file deleted!\n")
                print("Ending session, reload to play.")
                active = False  # End game.
        else:
            print("No save file detected, saving to new file.")  # Make a new file to save on.
            save_data = {"current_game": 0, "total_score": 0}
            content = json.dumps(save_data)
            save_file.write_text(content)
    else:
        save_data = {"current_game": 0, "total_score": 0}
        content = json.dumps(save_data)
        save_file.write_text(content)
    while active:
        game = Saving_Bowling_v3.BowlingGame()  # Where it all starts here
        game.load_game()
        game.current_game += 1
        print(f"\nCurrent game: {game.current_game}")
        while game.check_frame <= game.max_frames and active:  # Everything below, good luck.
            print(f"\nFrame: {clamp(game.check_frame, 0, 10)}")
            print(f"Ball: {game.current_roll + 1}/2")
            manual_score = None
            if not auto_play:
                user_response = quit_game()
                if type(user_response) == int:
                    manual_score = user_response
                else:
                    active = user_response
            quick_roll(manual_score)
        if game.extra_roll == 1:  # For the extra frame then you get the 10th strike. or spare
            print(f"\nFrame: {clamp(game.check_frame, 0, 10)}")
            print(f"Ball: 3/3")
            manual_score = None
            if not auto_play:
                user_response = quit_game()
                if type(user_response) == int:
                    manual_score = user_response
                else:
                    active = user_response
            quick_roll(manual_score)
        print("\nRound over... Calculating Scores\n")
        game.adjusted_scoreboard()
        print(f"DEBUG Score: {game.hit_count}")
        print(f"Final Score: {game.final_score}")
        print(f"Total score from all games: {game.comb_final_score + game.final_score}")
        while True:
            replay = input("Want to play again? (y/n)\n>").lower()
            if replay == "n" or replay == "no":
                final_save_choice = input("Save game? (y/n)\n>").lower()
                if final_save_choice == "y" or final_save_choice == "yes":
                    game.save_game()
                active = False
                break
            elif replay == "y" or replay == "yes":
                game.save_game()
                break
else:
    print("ok then")
