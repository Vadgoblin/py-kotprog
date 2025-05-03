import pygame
from config import Config
from .isPointInTrapezoid import is_point_in_trapezoid

_config : "Config | None" = None
_background : "pygame.Surface | None" = None

def _load_config():
    global _config
    _config = Config()

def _load_background():
    global _background
    bg_path = _config.menu["background"]
    _background = pygame.image.load(bg_path).convert()

def show_menu(screen : "pygame.Surface"):
    _load_config()
    _load_background()

    while True:
        for event in pygame.event.get():
            _process_event(event)

        screen.blit(_background,(0,0))
        pygame.display.flip()

def _process_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        click_pos = event.dict['pos']
        _process_click(click_pos)

def _process_click(click_pos):
    _check_exit_button(click_pos)
    _check_easy_button(click_pos)
    _check_normal_button(click_pos)
    _check_hard_button(click_pos)

def _check_exit_button(click_pos):
    click_x, click_y = click_pos
    x,y,w,h = _config.menu["exit_rect"]
    if x <= click_x <= click_x + w and y <= click_y <= y + h:
        pygame.quit()
        exit(0)

def _check_easy_button(click_pos):
    button_edges = _config.menu["easy_button_edges"]
    is_clicked = is_point_in_trapezoid(button_edges,click_pos)
    if is_clicked:
        print("easy")

def _check_normal_button(click_pos):
    button_edges = _config.menu["normal_button_edges"]
    is_clicked = is_point_in_trapezoid(button_edges,click_pos)
    if is_clicked:
        print("normal")

def _check_hard_button(click_pos):
    button_edges = _config.menu["hard_button_edges"]
    is_clicked = is_point_in_trapezoid(button_edges,click_pos)
    if is_clicked:
        print("hard")