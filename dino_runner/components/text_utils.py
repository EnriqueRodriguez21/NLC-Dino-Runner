import pygame.font

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FRONT_STYLE = 'freesansbold.ttf'
black_color = (212, 175, 55)


def get_score_element(points):
    font = pygame.font.Font(FRONT_STYLE, 30)
    text = font.render('Points: {}'.format(points), True, black_color)
    text_rect = text .get_rect()
    text_rect.center = (100, 40)
    return text, text_rect


def get_centered_message(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FRONT_STYLE, 30)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect


def show_number_of_deaths(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FRONT_STYLE, 25)
    text_death = font.render(message, True, black_color)
    text_death_rect = text_death.get_rect()
    text_death_rect.center = (width, height + 50)
    return text_death, text_death_rect


