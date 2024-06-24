# tetris.py

import pygame
from block import Block
from grid import Grid
from ui import UI
from settings import DIFFICULTY_LEVELS, DEFAULT_CONTROLS, SCREEN_WIDTH, SCREEN_HEIGHT
from themes import ThemeManager

class Tetris:
    def __init__(self, screen, difficulty="medium", theme="default", controls=None):
        self.screen = screen
        self.grid = Grid()
        self.theme_manager = ThemeManager(theme)
        self.ui = UI(self.theme_manager)
        self.blocks = [Block(self.grid.grid), Block(self.grid.grid)]
        self.paused = False
        self.difficulty = difficulty
        self.controls = controls or DEFAULT_CONTROLS
        self.set_controls()
        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        pygame.display.set_caption('Tetris')

    def set_controls(self):
        self.control_mapping = {
            self.controls["left"]: self.left,
            self.controls["right"]: self.right,
            self.controls["rotate"]: self.rotate,
            self.controls["down"]: self.down,
            self.controls["pause"]: self.toggle_pause
        }

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                self.handle_key_event(event.key)
        return True

    def handle_key_event(self, key):
        if key in self.control_mapping:
            self.control_mapping[key]()

    def toggle_pause(self):
        self.paused = not self.paused

    def left(self):
        if not self.paused:
            self.blocks[0].move_left()

    def right(self):
        if not self.paused:
            self.blocks[0].move_right()

    def down(self):
        if not self.paused:
            self.blocks[0].move_down()

    def rotate(self):
        if not self.paused:
            self.blocks[0].rotate()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            running = self.handle_events()
            
            if not self.paused:
                self.update()
            
            self.draw()
            
            clock.tick(DIFFICULTY_LEVELS[self.difficulty])

        pygame.quit()

    def update(self):
        current_block = self.blocks[0]
        if current_block.can_fall():
            current_block.erase()
            current_block.i += 1
            current_block.fill()
        else:
            if current_block.i == 0:
                current_block.fill()
                self.ui.draw_grid(self.grid.grid)
                self.ui.display_message("Game Over", (255, 0, 0))
                return
            lines_cleared = self.grid.check_lines()
            self.ui.update_score(lines_cleared)
            self.blocks.pop(0)
            new_block = Block(self.grid.grid)
            self.blocks.append(new_block)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.ui.draw_grid(self.grid.grid)
        self.ui.update_score_display()
        self.ui.draw_next_block(self.blocks[1])
        pygame.display.flip()

def start_game(screen):
    game = Tetris(screen)
    game.run()

def main_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 50)

    play_button = font.render('Play', True, (255, 255, 255))
    settings_button = font.render('Settings', True, (255, 255, 255))
    quit_button = font.render('Quit', True, (255, 255, 255))

    buttons = [(play_button, (SCREEN_WIDTH//2 - play_button.get_width()//2, 200)),
               (settings_button, (SCREEN_WIDTH//2 - settings_button.get_width()//2, 300)),
               (quit_button, (SCREEN_WIDTH//2 - quit_button.get_width()//2, 400))]

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button, pos in buttons:
                    rect = button.get_rect(topleft=pos)
                    if rect.collidepoint(mouse_pos):
                        if button == play_button:
                            start_game(screen)
                        elif button == settings_button:
                            settings_menu(screen)
                        elif button == quit_button:
                            running = False

        for button, pos in buttons:
            screen.blit(button, pos)

        pygame.display.flip()

    pygame.quit()

def settings_menu(screen):
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 50)

    theme_button = small_font.render('Themes', True, (255, 255, 255))
    back_button = small_font.render('Back', True, (255, 255, 255))

    buttons = [(theme_button, (SCREEN_WIDTH//2 - theme_button.get_width()//2, 200)),
               (back_button, (SCREEN_WIDTH//2 - back_button.get_width()//2, 300))]

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button, pos in buttons:
                    rect = button.get_rect(topleft=pos)
                    if rect.collidepoint(mouse_pos):
                        if button == theme_button:
                            theme_menu(screen)
                        elif button == back_button:
                            running = False

        for button, pos in buttons:
            screen.blit(button, pos)

        pygame.display.flip()

def theme_menu(screen):
    font = pygame.font.Font(None, 74)
    themes = ['Default', 'Dark', 'Neon']
    theme_buttons = [font.render(theme, True, (255, 255, 255)) for theme in themes]
    back_button = font.render('Back', True, (255, 255, 255))

    buttons = [(theme_buttons[i], (SCREEN_WIDTH//2 - theme_buttons[i].get_width()//2, 200 + i * 100)) for i in range(len(themes))]
    buttons.append((back_button, (SCREEN_WIDTH//2 - back_button.get_width()//2, 200 + len(themes) * 100)))

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, button_info in enumerate(buttons):
                    button, pos = button_info
                    rect = button.get_rect(topleft=pos)
                    if rect.collidepoint(mouse_pos):
                        if button == back_button:
                            settings_menu(screen)
                        else:
                            start_game(screen)

        for button, pos in buttons:
            screen.blit(button, pos)

        pygame.display.flip()

def main():
    pygame.init()
    main_menu()

if __name__ == "__main__":
    main()
