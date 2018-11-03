import pygame, sys

from core.frame import Frame
from core.spatial import is_direction

pygame.init()
pygame.event.set_blocked([
    pygame.ACTIVEEVENT,
    pygame.KEYUP,
    pygame.MOUSEMOTION,
    pygame.MOUSEBUTTONUP,
    pygame.MOUSEBUTTONDOWN,
    pygame.JOYAXISMOTION,
    pygame.JOYBALLMOTION,
    pygame.JOYHATMOTION,
    pygame.JOYBUTTONUP,
    pygame.JOYBUTTONDOWN,
    pygame.VIDEORESIZE,
    pygame.VIDEOEXPOSE,
    pygame.USEREVENT,
])
pygame.event.set_allowed([
    pygame.QUIT,
    pygame.KEYDOWN,
])

frame = Frame()
clock = pygame.time.Clock()
while True:
    clock.tick(20)
    for event in pygame.event.get(pygame.QUIT):
        print(frame.scoreboard.score)
        pygame.quit()
        sys.exit(0)
    direction_events = [event for event in pygame.event.get(pygame.KEYDOWN) if is_direction(event.key)]
    if direction_events:
        direction_event = direction_events.pop(0)
        frame.snake.turn(direction_event.key)
    frame.snake.move()
    if frame.snake.head == frame.apple:
        frame.snake.grow()
        frame.scoreboard.inc_score()
        frame.make_apple()
    if frame.snake.is_colliding() or frame.snake_is_out_of_bounds():
        print(frame.scoreboard.score)
        pygame.quit()
        sys.exit(0)
    else:
        frame.draw()
        pygame.display.flip()

