# high_score.py

import os

HIGH_SCORE_FILE = "high_score.txt"

def get_high_score():
    try:
        if os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read().strip())
    except IOError as e:
        print(f"Error reading high score file: {e}")
    return 0

def save_high_score(score):
    try:
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(score))
    except IOError as e:
        print(f"Error saving high score: {e}")
