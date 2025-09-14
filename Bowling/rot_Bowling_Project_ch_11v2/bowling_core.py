"""Core of bowling, where all the processing of bowling goes here.
v1.0"""
import json
import pathlib
import random

save_file = pathlib.Path("bowling_save.json")


class BowlingGame:
    def __init__(self):
        self.total_score = 0
        self.end_game = False
        self.scoreboard = {}
        self.score = 0
        self.current_frame_roll = 1
        self.current_pins = 10
        self.current_frame = 1
        self.knocked_pins = 0
        self.hit_score = []
        self.final_hit_score = []
        self.extra_frames = 0
        self.final_score_str = ""
        self.final_str = ""
        self.current_game = 0
        self.game_history = {}

    def get_game_stats_full(self):
        return f"""=====FINAL=====
{self.readable_scoreboard()}
TOTAL SCORE: {self.calculate_score()}
GAMES PLAYED: {self.current_game}
COMBINED SCORE: {self.total_score}
==============="""

    def get_game_stats_mini(self):
        return f"""===============
Current roll: {self.current_frame_roll}
Current frame: {self.current_frame}
==============="""

    def print_debug(self):
        print(f"""\n===============DEBUG
scoreboard {self.scoreboard}
hit_score {self.hit_score}
fin_score {self.final_hit_score}
cur_frame {self.current_frame}
cur_roll {self.current_frame_roll}
conv_score {self.final_score_str}\n
===============""")

    @staticmethod
    def clamp(num, min_value, max_value):  # Clamp values
        return max(min(num, max_value), min_value)

    def reset_pins(self):
        """Reset pins"""
        self.current_pins = 10
        self.knocked_pins = 0
        self.hit_score = []

    def increment_frame(self):
        """Increment frame"""
        self.current_frame += 1

    def increment_score(self, score):
        """Increment score"""
        self.score += score

    def check_frame(self):
        """Check if frame is over"""
        if self.current_frame < 10:
            if self.knocked_pins == 10:
                self.scoreboard.update({self.current_frame: self.hit_score})
                self.increment_frame()
                print("\nStrike!")
                self.reset_pins()
                self.current_frame_roll = 1
            if self.current_frame_roll == 3 and self.current_frame < 10:
                self.scoreboard.update({self.current_frame: self.hit_score})
                self.increment_frame()
                if sum(self.hit_score) == 10:
                    print("\nSpare!")
                self.reset_pins()
                self.current_frame_roll = 1
        elif self.current_frame == 10:
            self.scoreboard.update({self.current_frame: self.final_hit_score})
            if self.knocked_pins == 10:
                print("\nStrike!")
                if self.current_frame_roll == 2:
                    print("Gained 2 extra frames!")
                    self.extra_frames = 2
                self.reset_pins()
            if self.current_frame_roll == 3 and sum(self.final_hit_score) == 10:
                print("\nSpare!")
                print("Gained an extra frame!")
                self.reset_pins()
                self.extra_frames = 1
            elif self.current_frame_roll == 3 and self.knocked_pins < 10 and self.extra_frames == 0:
                print("Maximum rolls 2/2 reached!")
                self.end_game = True
            elif self.current_frame_roll == 4:
                print("Maximum rolls 3/3 reached!")
                self.end_game = True

    def roll_ball(self, manual):
        """Roll the ball"""
        self.current_frame_roll += 1
        if manual or manual == 0:
            self.knocked_pins = self.clamp(manual, 0, self.current_pins)
        else:
            self.knocked_pins = random.randint(0, self.current_pins)
        print(f"\nKnocked {self.knocked_pins}/{self.current_pins}.")
        self.current_pins -= self.knocked_pins
        self.hit_score.append(self.knocked_pins)
        print(f"{self.current_pins} remaining")
        if self.current_frame == 10:
            self.final_hit_score.append(self.knocked_pins)
        self.check_frame()

    def calculate_score(self):
        """shitty code, but it works
        score calculation"""
        for key, data in self.scoreboard.items():
            if key < 10:
                if data == [10]:  # 1st Frame Strike
                    self.increment_score(10)
                    if self.scoreboard[key + 1] == [10]:  # 2nd Frame Strike
                        self.increment_score(10)
                        if self.scoreboard[key + 2] == [10]:  # 3rd Frame Strike
                            self.increment_score(10)
                        else:  # 3rd Open Frame / Spare
                            self.increment_score(self.scoreboard[key + 2][0])
                    elif self.scoreboard[key + 1][0] == 10:  # 2nd / 10th Frame Strike
                        self.increment_score(10)
                        if self.scoreboard[key + 1][1] == 10:  # 3rd / 10th Frame Strike
                            self.increment_score(10)
                        elif self.scoreboard[key + 1][1] + self.scoreboard[key + 1][2] == 10:  # 3rd / 10th Frame Strike
                            self.increment_score(self.scoreboard[key + 1][1])
                    elif self.scoreboard[key + 1][0] + self.scoreboard[key + 1][1] == 10:  # 3rd / 10th Frame Spare
                        self.increment_score(10)
                    elif sum(self.scoreboard[key + 1]) == 10 and self.scoreboard[key + 2] != [10]:  # 2nd Frame Spare
                        self.increment_score(sum(self.scoreboard[key + 1]))
                    elif sum(self.scoreboard[key + 1]) < 10:  # 2nd Open Frame
                        self.increment_score(self.scoreboard[key + 1][0] + self.scoreboard[key + 1][1])
                elif sum(data) == 10:  # 1st Frame Spare
                    self.increment_score(sum(data))
                    if self.scoreboard[key + 1] == [10]:  # 2nd Frame Strike
                        self.increment_score(10)
                    else:  # 2nd Open Frame
                        self.increment_score(self.scoreboard[key + 1][0])
                else:  # Add up score in Frame
                    self.increment_score(sum(data))
            elif key == 10:  # For 10th Frame
                if sum(data) < 10:  # 10th Open Frame
                    self.increment_score(sum(data))
                elif data[0] == 10:  # 10th Frame 1st Roll strike
                    try:
                        self.increment_score(10 + data[1] + data[2])
                    except IndexError:
                        return "MISSING 3RD VALUE FOR 10th STRIKE"
                elif sum(data) == 30:  # 10th Frame Strike
                    self.increment_score(30)
                elif data[0] + data[1] == 10:  # 10th Frame Spare
                    try:
                        self.increment_score(data[0] + data[1] + data[2])
                    except IndexError:
                        return "MISSING 3RD VALUE FOR 10th SPARE"
#            print(key, data, self.score)
        return self.score

    def readable_scoreboard(self):
        """Prints the scoreboard in a readable format"""
        final_string = ""
        for keys, data in self.scoreboard.items():
            if data == [10]:
                final_string += "| _ X "
                self.final_score_str += "X "
            elif sum(data) == 10 and len(data) == 2:
                final_string += f"| {data[0]} / "
                self.final_score_str += f"{data[0]}/ "
            else:
                try:
                    temp_data = data.copy()
                    if data[0] + data[1] == 10:
                        temp_data[1] = "/"
                    if data[0] == 10:
                        temp_data[0] = "X"
                    if data[1] == 10:
                        temp_data[1] = "X"
                    if data[2] == 10:
                        temp_data[2] = "X"
                    elif data[1] + data[2] == 10 and temp_data[1] != "/":
                        temp_data[2] = "/"
                    self.final_score_str += f"{temp_data[0]}{temp_data[1]}{temp_data[2]}"
                    final_string += f"| {temp_data[0]} {temp_data[1]} {temp_data[2]} |"
                except IndexError:
                    self.final_score_str += f"{data[0]}{data[1]} "
                    final_string += f"| {data[0]} {data[1]} "
        self.final_str = final_string
        return final_string

    def save_scoreboard(self):
        """Saves the scoreboard to a file"""
        self.game_history.update({self.current_game: [self.final_str, self.score]})

    @staticmethod
    def new_save():
        """Creates a new save file"""
        new_save_data = {"current_game": 0, "total_score": 0, "game_history": {}}
        new_content = json.dumps(new_save_data)
        save_file.write_text(new_content)

    def save_game(self):
        """Saves the game to a file"""
        loaded_save_content = save_file.read_text()
        loaded_save_data = json.loads(loaded_save_content)
        saving_save_data = {"current_game": self.current_game,
                            "total_score": self.score + loaded_save_data["total_score"],
                            "game_history": self.game_history}
        saving_content = json.dumps(saving_save_data)
        save_file.write_text(saving_content)

    def load_game(self):
        """Loads the game from a file"""
        loading_save_content = save_file.read_text()
        loading_save_data = json.loads(loading_save_content)
        self.total_score = loading_save_data["total_score"]
        self.current_game = loading_save_data["current_game"]
        self.game_history = loading_save_data["game_history"]
