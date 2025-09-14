# Bowling, by Hong Rot
# I'm so f****** sorry for making you read this. 😭
# I know all the rules of bowling now.
# V 2.0
# Saving and error handling.
# Manual inputs for scoring.
import random
import time
import json
import pathlib

sleep_time_wait = 0  # Used for rolling time artificial wait.


def clamp(num, min_value, max_value):  # Clamp values
    return max(min(num, max_value), min_value)


class BowlingGame:

    def __init__(self):
        self.knocked_pins = None
        self.score = 0
        self.final_score = 0
        self.hit_count = []
        self.adjusted_score = {}
        self.max_pins = 10
        self.current_pins = self.max_pins
        self.current_roll = 0
        self.current_frame = 1
        self.max_frames = 10
        self.extra_roll = 0
        self.spare_list = []
        self.current_game = 0
        self.comb_final_score = 0

    def reset_pins(self):
        self.current_roll = 0
        self.current_frame += 1
        self.current_pins = self.max_pins
        self.spare_list.clear()

    def roll_ball(self, manual=False):
        self.current_roll += 1
        if manual or manual == 0:
            self.knocked_pins = clamp(manual, 0, self.current_pins)
        else:
            self.knocked_pins = random.randint(0, self.current_pins)  # RNG
        #        self.knocked_pins = 5  # DEBUG
        new_pins = self.current_pins - self.knocked_pins
        print(f"Knocked {self.knocked_pins}/{self.current_pins}.")
        self.score += self.knocked_pins
        self.current_pins -= self.knocked_pins
        self.spare_list.append(self.knocked_pins)
        print(f"{self.current_pins} remaining")
        if self.knocked_pins == 0:
            print("Missed all pins :(")
        if new_pins == 0:  # strike/spare!
            if self.current_roll == 1:
                print(f"Strike! ({self.max_pins}/{self.max_pins} Pins hit)")
                if self.current_frame == 11:
                    self.hit_count[self.current_frame - 2][1].append(10)
                else:
                    self.hit_count.append([self.current_frame, [10, 10]])
                if self.current_frame == 10 and self.current_roll == 1:
                    self.extra_roll += 1
            else:
                print(f"Spare! ({self.max_pins}/{self.max_pins} Pins hit)")
                self.hit_count.append([self.current_frame, self.spare_list[:]])
                if self.current_frame == 10 and self.current_roll == 2:
                    self.extra_roll += 1
            self.reset_pins()
        else:
            if self.current_roll == 1:
                if self.current_frame == 11 and self.current_roll == 1:
                    self.hit_count[self.current_frame - 2][1].append(10 - self.current_pins)
            elif self.current_roll == 2:
                self.hit_count.append([self.current_frame, self.spare_list[:]], )
                self.reset_pins()
                print("Didn't hit all, next frame.")

    @property
    def check_frame(self):
        return self.current_frame

    def human_readable_format(self):
        scoreboard = []
        final_string = ""
        for index, score in enumerate(self.hit_count):
            if score[1] == [10, 10]:
                scoreboard.append("X")
                final_string += "| _ X "
            elif sum(score[1]) == 10:
                scoreboard.append([score[1][0], "/"])
                final_string += f"| {score[1][0]} / "
            else:
                scoreboard.append(score[1])
                try:
                    if score[1][0] + score[1][1] == 10:
                        score[1][1] = "/"
                    if score[1][0] == 10:
                        score[1][0] = "X"
                    if score[1][1] == 10:
                        score[1][1] = "X"
                    if score[1][2] == 10:
                        score[1][2] = "X"
                    final_string += f"| {score[1][0]} {score[1][1]} {score[1][2]} "
                except IndexError:
                    final_string += f"| {score[1][0]} {score[1][1]} "
        final_string += "|"
        print(final_string)

    def adjusted_scoreboard(self):  # Very hard (to understand) part :(
        final_score = 0
        for index, score in enumerate(self.hit_count):
            frame_index = index + 1
            local_score = 0
            if index < 10:  # if frame is less than 10
                if len(score[1]) == 3:
                    local_score += sum(score[1])
                elif score[1] == [10, 10]:  # 1st strike
                    local_score = 10
                    try:  # Check if next frame exists
                        next_frame = self.hit_count[index + 1]
                    except IndexError:  # If it does not exist, make it empty.
                        next_frame = [0, [0, 0]]
                    try:  # Check if next next frame exists if there's 3 strikes in a row.
                        next_next_frame = self.hit_count[index + 2]
                    except IndexError:
                        next_next_frame = [0, [0, 0]]
                    if score[0] < 10:
                        if next_frame[1] == [10, 10]:  # 2nd strike
                            local_score += 10
                            if next_next_frame[1] == [10, 10]:  # 3rd strike
                                local_score += 10
                            elif next_next_frame[1] == [10, 10, 10]:  # 3rd strike 10th frame
                                local_score += 10
                            elif len(next_next_frame[1]) == 3 and next_next_frame[1][0] == 10:
                                local_score += 10
                            else:
                                local_score += next_next_frame[1][0]
                        elif next_frame[1][0] + next_frame[1][1] == 10:  # 2nd spare
                            local_score += next_frame[1][0] + next_frame[1][1]
                        else:  # 2nd open frame
                            local_score += next_frame[1][0] + next_frame[1][1]
                    self.adjusted_score.update({frame_index: local_score})
                elif score[1][0] + score[1][1] == 10:  # 1st spare
                    local_score = 10
                    try:  # Check next frame exists
                        next_frame = self.hit_count[index + 1]
                    except IndexError:
                        next_frame = [0, [0, 0]]
                    if next_frame[1] == [10, 10]:  # 2nd strike check
                        local_score += 10
                    elif next_frame[1][0] + next_frame[1][1] == 10:  # 2nd spare
                        local_score += next_frame[1][0]
                    else:
                        local_score += next_frame[1][0]
                    if len(score[1]) == 3:
                        local_score += score[1][2]
                    self.adjusted_score.update({frame_index: local_score})
                else:  # man I don't know
                    local_score = 0
                    local_score += score[1][0] + score[1][1]
                    self.adjusted_score.update({frame_index: local_score})
            final_score += local_score
            # print(f"{frame_index} + {local_score} | {final_score - local_score} > {final_score}")  # DEBUG FORMAT
        self.final_score = final_score
        self.human_readable_format()

    save_file = pathlib.Path("bowling_save.json")

    @staticmethod
    def new_save():  # Start new save!
        new_save_data = {"current_game": 0, "total_score": 0}
        new_content = json.dumps(new_save_data)
        save_file.write_text(new_content)

    def save_game(self):
        loaded_save_content = save_file.read_text()
        loaded_save_data = json.loads(loaded_save_content)
        saving_save_data = {"current_game": self.current_game,
                            "total_score": self.final_score + loaded_save_data["total_score"]}
        saving_content = json.dumps(saving_save_data)
        save_file.write_text(saving_content)

    def load_game(self):
        loading_save_content = save_file.read_text()
        loading_save_data = json.loads(loading_save_content)
        self.current_game = loading_save_data["current_game"]
        self.comb_final_score = loading_save_data["total_score"]


play_input = input("Would you like to play bowling? (y/n)\n>").lower()
while play_input != "yes" and play_input != "y" and play_input != "no" and play_input != "n":
    play_input = input("Would you like to play bowling? (y/n)\n>").lower()
if play_input == "yes" or play_input == "y":  # START
    active = True
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
    while active:
        game = BowlingGame()  # Where it all starts here
        game.load_game()
        game.current_game += 1
        print(f"\nCurrent game: {game.current_game}")
        while game.check_frame <= game.max_frames and active:  # Everything below, good luck.
            print(f"\nFrame: {clamp(game.check_frame, 0, 10)}")
            print(f"Ball: {game.current_roll + 1}/2")
            roll_input = ""
            manual_score = False
            if not auto_play:
                while True:  # Forced user input on rolling or quitting.
                    if not manual_input:
                        roll_input = input("Roll ball (y) or [Q]uit\n>").lower()
                        if roll_input == "yes" or roll_input == "y":
                            break
                        elif roll_input == "q":
                            active = False
                            break
                    else:
                        manual_score = input("Enter the pins you hit: \n>")
                        try:
                            manual_score = int(manual_score)
                        except ValueError:
                            print("Enter a number!")
                        else:
                            break
            if not roll_input == "q":
                print("\nRolling ball...\n")
                time.sleep(sleep_time_wait)
                game.roll_ball(manual_score)
        if game.extra_roll == 1:  # For the extra frame then you get the 10th strike.
            print(f"\nFrame: {clamp(game.check_frame, 0, 10)}")
            print(f"Ball: 3/3")
            new_roll_input = ""
            manual_score = False
            if not auto_play:
                while True:  # Forced user input on rolling or quitting.
                    if not manual_input:
                        roll_input = input("Roll ball (y) or [Q]uit\n>").lower()
                        if roll_input == "yes" or roll_input == "y":
                            break
                        elif roll_input == "q":
                            active = False
                            break
                    else:
                        manual_score = input("Enter the pins you hit: \n>")
                        try:
                            manual_score = int(manual_score)
                        except ValueError:
                            print("Enter a number!")
                        else:
                            break
            if not new_roll_input == "q":
                print("\nRolling ball...\n")
                time.sleep(sleep_time_wait)
                game.roll_ball(manual_score)
        print("\nRound over... Calculating Scores\n")
        game.adjusted_scoreboard()
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
