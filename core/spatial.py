from collections import namedtuple
from pygame import K_UP, K_DOWN, K_RIGHT, K_LEFT

#TODO: Move Point to its own class, possibly
#      something called, 'body_segment' or some
#      such thing to convey its use
Point = namedtuple('Point','x y')

UP = K_UP
DOWN = K_DOWN
RIGHT = K_RIGHT
LEFT = K_LEFT

class DirectionError(Exception):
    pass

def translate(coord, direction):
    if direction == K_UP:
        return Point(coord.x, coord.y-1)
    elif direction == K_DOWN:
        return Point(coord.x, coord.y+1)
    elif direction == K_RIGHT:
        return Point(coord.x+1, coord.y)
    elif direction == K_LEFT:
        return Point(coord.x-1, coord.y)
    else:
        raise DirectionError("arg 'direction' must be 'int' between 273 and 276")

def opposite(direction):
    if direction == K_UP:
        return K_DOWN
    if direction == K_DOWN:
        return K_UP
    if direction == K_RIGHT:
        return K_LEFT
    if direction == K_LEFT:
        return K_RIGHT
    else:
        raise DirectionError("arg 'direction' must be 'int' between 273 and 276")

def is_direction(key):
    return key == K_UP or key == K_DOWN or key == K_RIGHT or key == K_LEFT

def apply_scale(point, scale):
    return Point(scale*point.x, scale*point.y)
