# settings.py

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30

DIFFICULTY_LEVELS = {
    "easy": 500,
    "medium": 300,
    "hard": 100
}

DEFAULT_CONTROLS = {
    "left": "Left",
    "right": "Right",
    "down": "Down",
    "rotate": "Up",
    "pause": "space"
}

def update_controls(new_controls):
    global DEFAULT_CONTROLS
    DEFAULT_CONTROLS.update(new_controls)

