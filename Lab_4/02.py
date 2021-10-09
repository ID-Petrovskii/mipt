import pygame
from pygame.draw import *
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
BLUE = (64, 128, 255)
LIGHT_BLUE = (0, 200, 200)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)


def draw_bird(screen, color, x, y, size):
    '''
    Функция рисует птичку типа "галочка", ну знаешь, как на детском рисунке
    screen - передаеться поверхость, на которой рисуешь
    color - цвет птички
    x, y - координаты правого верхнего угла птички на поверхности
    size - размер птички по горизонтали (по вертикали будет в 2 раза меньше) в px
    '''
    Surface_for_bird = pygame.Surface((2 * size, size * 0.5))
    Surface_for_bird.set_colorkey((0, 0, 0))
    arc(Surface_for_bird, color, (size, 0, size, size * 0.5), math.pi * 0.5, math.pi)
    arc(Surface_for_bird, color, (0, 0, size, size * 0.5), 0, math.pi * 0.5)
    screen.blit(Surface_for_bird, (x - size*0.5, y))
    
    

def draw_fish(screen, color, x, y, size):
    '''
    Функция рисует рыбу, тут все понятно
    screen - передаеться поверхость, на которой рисуешь
    color - основной цвет рыбы
    x, y - координаты правого верхнего примерно угла рыбы на поверхности
    size - некий характерный размер рыбы в px
    '''
    Surface_for_fish = pygame.Surface((2 * size, size))
    Surface_for_fish.set_colorkey((0, 0, 0))
    polygon(Surface_for_fish, PINK,
            ((size * 0.45, size * 0.5), (size * 0.3, size * 0.7), (size * 0.5, size * 0.7)))
    polygon(Surface_for_fish, PINK,
            ((size * 0.9, size * 0.5), (size * 0.9, size * 0.8), (size * 1.1, size * 0.7)))
    polygon(Surface_for_fish, PINK,
            ((size * 0.8, size * 0.3), (size * 0.9, size * 0.1), (size * 0.4, size * 0)))
    ellipse(Surface_for_fish, color, (size * 0.2, size * 0.2, size, size * 0.4))
    circle(Surface_for_fish, BLUE, (size * 1, size * 0.4), size * 0.05)
    polygon(Surface_for_fish, color, ((size * 0.2, size * 0.4), (size * 0, size * 0.2), (size * 0, size * 0.6)))
    screen.blit(Surface_for_fish, (x - size * 0.2, y - size *0.2))
    
    
    

def draw_gull(screen, color, x, y, size):
    '''
    Функция рисует чайку, которая на английском звучит устрашающе
    screen - передаеться поверхость, на которой рисуешь
    color - основной цвет чайки
    x, y - координаты правого верхнего примерно угла чайки на поверхности
    size - некий характерный размер чайки в px
    '''
    Surface_for_gull = pygame.Surface((3 * size, 3 * size))
    rect(Surface_for_gull, (0, 0, 1), (0, 0, 3 * size, 3 * size))
    Surface_for_gull.set_colorkey((0, 0, 1))
    ellipse(Surface_for_gull, color, (size, size, size, size / 2))
    ellipse(Surface_for_gull, color, (size * 1.8, size * 1.1, size / 2, size / 4))
    ellipse(Surface_for_gull, color, (size * 2, size, size / 2, size / 4))
    ellipse(Surface_for_gull, BLACK, (size * 2.3, size * 1.04, size / 10, size / 20))
    line(Surface_for_gull, YELLOW, (size * 2.5, size * 1.12), (size * 2.8, size * 1.12), int(size * 0.06))
    line(Surface_for_gull, BLACK, (size * 2.5, size * 1.12), (size * 2.8, size * 1.12), int(size * 0.01))
    polygon(Surface_for_gull, color,
            ((size * 1.25, size * 1.25), (size * 0.75, size * 1.25), (size * 0.75, size)))
    polygon(Surface_for_gull, color,
            ((size * 1.5, size * 1.5), (size * 1.25, size * 0.75), (size * 0.4, size * 0.5)))

    circle(Surface_for_gull, color, (size * 1.5, size * 1.5), size / 8)
    circle(Surface_for_gull, color, (size * 1.5, size * 1.6), size / 8)
    ellipse(Surface_for_gull, color, (size * 1.5, size * 1.5, size / 2, size / 8))
    ellipse(Surface_for_gull, color, (size * 1.5, size * 1.6, size / 2, size / 8))
    line(Surface_for_gull, YELLOW, (size * 2, size * 1.55), (size * 2.2, size * 1.55), int(size * 0.03))
    line(Surface_for_gull, YELLOW, (size * 2, size * 1.67), (size * 2.2, size * 1.67), int(size * 0.03))
    line(Surface_for_gull, YELLOW, (size * 2, size * 1.55), (size * 2.2, size * 1.63), int(size * 0.03))
    line(Surface_for_gull, YELLOW, (size * 2, size * 1.67), (size * 2.2, size * 1.73), int(size * 0.03))
    line(Surface_for_gull, YELLOW, (size * 2, size * 1.55), (size * 2.2, size * 1.7), int(size * 0.03))
    line(Surface_for_gull, YELLOW, (size * 2, size * 1.67), (size * 2.2, size * 1.8), int(size * 0.03))
    line(Surface_for_gull, YELLOW, (size * 2, size * 1.55), (size * 2, size * 1.65), int(size * 0.03))
    line(Surface_for_gull, YELLOW, (size * 2, size * 1.67), (size * 2, size * 1.77), int(size * 0.03))
    screen.blit(Surface_for_gull, (x - size, y - size))


pygame.init()

FPS = 30
width = 794
height = 1123
screen = pygame.display.set_mode((width, height))

# sky and water
rect(screen, (21, 21, 78), (0, 0, width, 116))
rect(screen, (141, 95, 211), (0, 116, width, 178 - 116))
rect(screen, (205, 87, 222), (0, 178, width, 282 - 178))
rect(screen, (222, 87, 170), (0, 282, width, 430 - 282))
rect(screen, (255, 99, 55), (0, 430, width, 552 - 430))
rect(screen, (00, 66, 80), (0, 552, width, height - 552))

# drawing objects
draw_gull(screen, WHITE, 400, 800, 160)
draw_gull(screen, WHITE, 600, 600, 100)
draw_gull(screen, WHITE, 200, 650, 60)

draw_fish(screen, LIGHT_BLUE, 600, 950, 80)
draw_fish(screen, LIGHT_BLUE, 100, 900, 100)
draw_fish(screen, LIGHT_BLUE, 500, 700, 50)

draw_bird(screen, WHITE, 100, 100, 150)
draw_bird(screen, WHITE, 150, 400, 150)
draw_bird(screen, WHITE, 500, 200, 150)
draw_bird(screen, WHITE, 600, 300, 100)
draw_bird(screen, WHITE, 550, 400, 100)
draw_bird(screen, WHITE, 700, 250, 100)
draw_bird(screen, WHITE, 200, 200, 50)
draw_bird(screen, WHITE, 250, 300, 50)
draw_bird(screen, WHITE, 300, 350, 50)
draw_bird(screen, WHITE, 200, 350, 50)
draw_bird(screen, WHITE, 350, 250, 50)
draw_bird(screen, WHITE, 300, 200, 50)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
