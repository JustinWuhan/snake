from collections import deque
from itertools import islice

from .spatial import Point, translate, opposite, K_RIGHT

class Snake(object):
    def __init__(self):
        self.length = 9
        self.coords = deque([Point(x,5) for x in range(15,15-self.length,-1)])
        self.head = self.coords[0]
        self.tail = self.coords[-1]
        self.direction = K_RIGHT
        self.growing = 0

    def _should_turn(self, key):
        return not (self.direction == key or opposite(self.direction) == key)

    def _get_new_head(self):
        return translate(self.head, self.direction)

    def is_colliding(self):
        return self.head in islice(self.coords, 1, self.length)

    def turn(self,key):
        if self._should_turn(key):
            self.direction = key

    def grow(self):
        self.growing += 3

    def move(self):
        new_head = self._get_new_head()
        self.coords.appendleft(new_head)
        if self.growing:
            self.growing-=1
            self.length+=1
        else:
            self.coords.pop()
        self.head = new_head

