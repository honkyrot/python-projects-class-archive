# Bowling, by Hong Rot
# I'm so f****** sorry for making you read this. 😭
# I know all the rules of bowling now.
import random
import time

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

    def reset_pins(self):
        self.current_roll = 0
        self.current_frame += 1
        self.current_pins = self.max_pins
        self.spare_list.clear()

    def roll_ball(self):
        self.current_roll += 1
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

    def adjusted_scoreboard(self):  # Very hard part :(
        final_score = 0
        for index, score in enumerate(self.hit_count):
            frame_index = index + 1
            local_score = 0
            if index < 10:
                if len(score[1]) == 3:
                    local_score += sum(score[1])
                elif score[1] == [10, 10]:  # 1st strike
                    local_score = 10
                    try:  # Check if next frame exists
                        next_frame = self.hit_count[index + 1]
                    except IndexError:
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


play_input = input("Would you like to play bowling? (y/n)\n>").lower()
if play_input == "yes" or play_input == "y":
    active = True
    auto_play = False
    run_auto_input = input("Would you like to auto-run this? (y/n)\n>").lower()
    if run_auto_input == "yes" or run_auto_input == "y":  # Auto run, used for quick tests.
        auto_play = True
    else:
        sleep_time_wait = .5
    while active:
        game = BowlingGame()  # Where it all starts here
        while game.check_frame <= game.max_frames:
            print(f"\nFrame: {clamp(game.check_frame, 0, 10)}")
            print(f"Ball: {game.current_roll + 1}/2")
            if not auto_play:
                while True:
                    roll_input = input("Roll ball? (y)\n>").lower()
                    if roll_input == "yes" or roll_input == "y":
                        break
            print("\nRolling ball...\n")
            time.sleep(sleep_time_wait)
            game.roll_ball()
        if game.extra_roll == 1:
            print(f"\nFrame: {clamp(game.check_frame, 0, 10)}")
            print(f"Ball: 3/3")
            if not auto_play:
                while True:
                    new_roll_input = input("Roll ball? (y)\n>").lower()
                    if new_roll_input == "yes" or new_roll_input == "y":
                        break
            print("\nRolling ball...\n")
            time.sleep(sleep_time_wait)
            game.roll_ball()
        print("\nRound over... Calculating Scores\n")
        print(game.hit_count)
        game.adjusted_scoreboard()
        print(f"Final Score: {game.final_score}!")
        while True:
            replay = input("Want to play again? (y/n)\n>").lower()
            if replay == "n" or replay == "no":
                active = False
                break
            else:
                break
else:
    print("ok then")
