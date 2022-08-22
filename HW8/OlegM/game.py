import pygame
import time

#Треба втекти курсором від червоного карліка. С часом розмір та швидкість карліка збільшуеться.

FPS = 10

WIDTH_DISPLAY = 1024
HEIGHT_DISPLAY = 800

WHITE_COLOR = (255, 255, 255)
ORANGE_COLOR = (255, 150, 100)
BLACK_COLOR = (0, 0, 0)

COORD_X = 50
COORD_Y = 50
RADIUS_CIRCLE = 20
DELTA_STEP = 5
GAME_OVER = False

TIME_BEGIN = time.time()

# ініціалізація та створення об'єктів
pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
pygame.display.set_caption("I will catch you!")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    while not GAME_OVER:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                GAME_OVER = True
            #elif event.type == pygame.MOUSEMOTION:
                #mouse_x, mouse_y = event.__dict__['pos']
        #малювання шару в координатах 50,50
        gameDisplay.fill(BLACK_COLOR)
        pygame.draw.circle(gameDisplay, (255, 0, 0), [COORD_X,
                                                      COORD_Y],
                           RADIUS_CIRCLE)
        #визначення координат курсора
        mouse_x, mouse_y = pygame.mouse.get_pos()
        size_of_display = pygame.display.get_window_size()
        if RADIUS_CIRCLE <= COORD_X <= size_of_display[0] and RADIUS_CIRCLE <= COORD_Y <= size_of_display[1]:
            COORD_X = COORD_X + DELTA_STEP if COORD_X < mouse_x else COORD_X - DELTA_STEP
            COORD_Y = COORD_Y + DELTA_STEP if COORD_Y < mouse_y else COORD_Y - DELTA_STEP

        if COORD_X < RADIUS_CIRCLE:
            COORD_X = RADIUS_CIRCLE+DELTA_STEP
        if COORD_Y < RADIUS_CIRCLE:
            COORD_Y = RADIUS_CIRCLE+DELTA_STEP
        if COORD_X > size_of_display[0]-RADIUS_CIRCLE:
            COORD_X = size_of_display[0]-RADIUS_CIRCLE
        if COORD_Y > size_of_display[1]-RADIUS_CIRCLE:
            COORD_Y = size_of_display[1]-RADIUS_CIRCLE

        #print(abs(mouse_x - COORD_X), abs(mouse_y - COORD_Y), RADIUS_CIRCLE)
        #Вивід секундоміра в лівій верхній частині екрану
        font = pygame.font.SysFont('Calibri', 20, True, False)
        text = font.render(f"{round(time.time() - TIME_BEGIN, 2)} сек.", True, (255, 150, 100))
        #Збільшення в часі розміру та швидкості кола
        DELTA_STEP += 0.025 * (time.time() - TIME_BEGIN)
        RADIUS_CIRCLE += 0.025 * (time.time() - TIME_BEGIN)
        #Умова закінчення гри
        if (abs(mouse_y - COORD_Y) < RADIUS_CIRCLE * 0.5 and abs(mouse_x - COORD_X) < RADIUS_CIRCLE * 0.5):
            font1 = pygame.font.SysFont('Calibri', 20, True, False)
            text = font1.render(f"Game Over!. Your result: {round(time.time() - TIME_BEGIN, 2)} сек.", True,
                                (255, 150, 100))
            GAME_OVER = True

        gameDisplay.blit(text, [0, 0])

        pygame.display.update()
        clock.tick(FPS)
