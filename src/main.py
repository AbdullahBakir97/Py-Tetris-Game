# main.py

import pygame
from tetris import Tetris
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')

    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 50)

    play_button = font.render('Play', True, (255, 255, 255))
    settings_button = font.render('Settings', True, (255, 255, 255))
    quit_button = font.render('Quit', True, (255, 255, 255))

    buttons = [
        (play_button, (SCREEN_WIDTH//2 - play_button.get_width()//2, 200)),
        (settings_button, (SCREEN_WIDTH//2 - settings_button.get_width()//2, 300)),
        (quit_button, (SCREEN_WIDTH//2 - quit_button.get_width()//2, 400))
    ]

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_button_click(event.pos, buttons, screen, play_button, settings_button, quit_button)

        for button, pos in buttons:
            screen.blit(button, pos)

        pygame.display.flip()

    pygame.quit()

def handle_button_click(mouse_pos, buttons, screen, play_button, settings_button, quit_button):
    for button, pos in buttons:
        rect = button.get_rect(topleft=pos)
        if rect.collidepoint(mouse_pos):
            if button == play_button:
                print("Play button clicked")  # Placeholder for action
                game = Tetris(screen)
                game.run()
            elif button == settings_button:
                print("Settings button clicked")  # Placeholder for action
                settings_menu(screen)
            elif button == quit_button:
                print("Quit button clicked")  # Placeholder for action
                pygame.quit()
                quit()

def settings_menu(screen):
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 50)

    theme_button = small_font.render('Themes', True, (255, 255, 255))
    back_button = small_font.render('Back', True, (255, 255, 255))

    buttons = [
        (theme_button, (SCREEN_WIDTH//2 - theme_button.get_width()//2, 200)),
        (back_button, (SCREEN_WIDTH//2 - back_button.get_width()//2, 300))
    ]

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_button_click(event.pos, buttons, screen, None, None, None)

        for button, pos in buttons:
            screen.blit(button, pos)

        pygame.display.flip()

    return theme_menu(screen)

def theme_menu(screen):
    font = pygame.font.Font(None, 74)
    themes = ['Default', 'Dark', 'Neon']
    theme_buttons = [font.render(theme, True, (255, 255, 255)) for theme in themes]
    back_button = font.render('Back', True, (255, 255, 255))

    buttons = [
        (theme_buttons[i], (SCREEN_WIDTH//2 - theme_buttons[i].get_width()//2, 200 + i * 100)) for i in range(len(themes))
    ]
    buttons.append((back_button, (SCREEN_WIDTH//2 - back_button.get_width()//2, 200 + len(themes) * 100)))

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_button_click(event.pos, buttons, screen, None, None, None)

        for button, pos in buttons:
            screen.blit(button, pos)

        pygame.display.flip()

    # Determine which button was clicked and return the selected theme
    for button, pos in buttons:
        rect = button.get_rect(topleft=pos)
        if rect.collidepoint(mouse_pos):
            if button == back_button:
                return None
            else:
                return themes[buttons.index((button, pos))]

    return None

if __name__ == '__main__':
    main_menu()

