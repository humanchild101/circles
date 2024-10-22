import pygame, sys
from pygame.locals import QUIT

pygame.init()

COLOR = (40, 40, 40)
WIN = pygame.display.set_mode((1000, 1000), pygame.RESIZABLE)

INSTRUCTION = pygame.Surface((250, 30))
FONT = pygame.font.Font(None, 26)
TEXT = FONT.render('Click anywhere on the screen!', True, (0, 0, 0))

RED_BUTTON = pygame.Surface((200, 40))
RED_WORDS = FONT.render('Red Scheme Button', True, (255, 0, 0))

MULTICOLOR_BUTTON = pygame.Surface((200, 40))
MULTICOLOR_WORDS = FONT.render('Multicolor Button', True,(150, 90, 59))

pygame.display.set_caption('Create Task')

RED_SCHEME = False
MULTICOLOR_SCHEME = False

circle_sets = []


def circles(coordinates):
   if coordinates:
       pressed_time = pygame.time.get_ticks()
       circle_sets.append((coordinates, pressed_time, pygame.Color(255, 255,255)))

   for circle, press_time, circle_color in circle_sets:
       current_time = pygame.time.get_ticks()
       passed_time = current_time - press_time

       for ms in range(0, passed_time, 5000):
           r = 1 + 0.05 * passed_time
           if RED_SCHEME:
               circle_color.r = max(circle_color.r - 1, 0)
               circle_color.g = max(circle_color.g - 10, 0)
               circle_color.b = max(circle_color.b - 30, 0)

           pygame.draw.circle(WIN, circle_color, circle, int(r), 3)

       for ms in range(0, passed_time, 500):
           r = 1 + 0.05 * passed_time
           if MULTICOLOR_SCHEME:
               circle_color.r = (ms * 2) % 255
               circle_color.g = (ms * 8) % 255
               circle_color.b = (ms * 7) % 255

           pygame.draw.circle(WIN, circle_color, circle, int(r),3)



while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()

       if event.type == pygame.MOUSEBUTTONDOWN:
           mouse_pos = pygame.mouse.get_pos()

           if 0 <= mouse_pos[0] <= 200 and 50 <= mouse_pos[1] <= 90:
               RED_SCHEME = True
               MULTICOLOR_SCHEME = False
           elif 0 <= mouse_pos[0] <= 200 and 110 <= mouse_pos[1] <= 150:
               MULTICOLOR_SCHEME = True
               RED_SCHEME = False

           circles(pygame.mouse.get_pos())
           if 0 <= mouse_pos[0] <= 1000 and 0 <= mouse_pos[1] <= 1000:
               INSTRUCTION.fill((0, 0, 0, 0))

   WIN.fill(COLOR)

   INSTRUCTION.fill((255, 255, 255))
   INSTRUCTION.blit(TEXT, (10, 10))

   RED_BUTTON.fill((255, 255, 255))
   RED_BUTTON.blit(RED_WORDS, (20, 10))

   MULTICOLOR_BUTTON.fill((255, 255, 255))
   MULTICOLOR_BUTTON.blit(MULTICOLOR_WORDS, (20, 10))

   WIN.blit(INSTRUCTION, (0, 0))
   WIN.blit(RED_BUTTON, (0, 50))
   WIN.blit(MULTICOLOR_BUTTON, (0, 110))

   circles(None)
   pygame.display.update()




















''' Resources used:
1. https://www.pygame.org/docs/ref/time.html
2. https://www.pygame.org/docs/ref/time.html
3.https://www.gamedev.net/forums/topic/650319-circles-appear-than-disappear-in-pythonpygame/5110849/
4.https://stackoverflow.com/questions/51973441/how-to-fade-from-one-colour-to-another-in-pygame#:~:text=Set%20your%20foreground%20surface%20to,background%20of%20your%20third%20color.
5. https://www.pygame.org/docs/ref/draw.html#pygame.draw.ellipse
6.https://www.google.com/search?q=how+to+detect+mouse+click+pygame&oq=how+to+detect+mouse+click+pygame&gs_lcrp=EgZjaHJvbWUyCggAEEUYFhgeGDkyCAgBEAAYFhgeMg0IAhAAGIYDGIAEGIoFMg0IAxAAGIYDGIAEGIoF0gEINTIzNmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8
7.https://www.google.com/search?q=how+to+use+mouse+position+as+parameter+pygame&sca_esv=7b4f5aad248322ac&sxsrf=ACQVn0_EVVlR7dURk-BTip_JZ8_Fnus8_A%3A1711735849476&ei=KQQHZp7DHIniiLMP-Iy1wAs&ved=0ahUKEwje-4b6iJqFAxUJMWIAHXhGDbgQ4dUDCBA&uact=5&oq=how+to+use+mouse+position+as+parameter+pygame&gs_lp=Egxnd3Mtd2l6LXNlcnAiLWhvdyB0byB1c2UgbW91c2UgcG9zaXRpb24gYXMgcGFyYW1ldGVyIHB5Z2FtZTIFECEYoAEyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGKABMgUQIRifBTIFECEYnwUyBRAhGJ8FMgUQIRifBTIFECEYnwVI3wxQ6gFYmAtwAXgBkAEAmAGjAaAB5QiqAQMwLji4AQPIAQD4AQGYAgegAtoGwgIKEAAYRxjWBBiwA8ICBBAhGBWYAwCIBgGQBgiSBwMxLjagB5FH&sclient=gws-wiz-serp
8.https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
9.https://stackoverflow.com/questions/51229740/how-to-draw-a-semi-transparent-circle-in-pygame
10.debugging/some code help done with ChatGPT
11.https://www.pygame.org/docs/ref/color.html#pygame.Color.a
12.https://gamedevacademy.org/how-to-make-buttons-in-pygame-tutorial-complete-guide/
'''
