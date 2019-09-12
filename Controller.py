import pygame
from pygame.joystick import Joystick
import Collision
from Playground import Playground


class Controller:
    def __init__(self, joystick: Joystick):
        self.Joy = joystick

    def get_button_pressed(self, blo, position, collision: Collision.Collision_Dedektor, playground: Playground):
        events = pygame.event.get()
        for event in events:
            direction = None
            if event.type == pygame.JOYHATMOTION:
                hat_x, hat_y = event.value
                if hat_x == -1 and hat_y == 0:
                    direction = True  # left
                if hat_x == 1 and hat_y == 0:
                    direction = False  # right
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 1:
                    direction = False  # right
                if event.button == 0:
                    direction = True  # left
                if event.button == 7:
                    return "Restart"
                if event.button == 4:
                    return "Left Title"
                if event.button == 5:
                    return "Right Title"
            self.rotate_if_possible(blo, collision, direction, playground, position)

        newposition = None
        if self.Joy.get_axis(0) < -0.3:
            newposition = (position[0] - 1, position[1])

        if self.Joy.get_axis(0) > 0.3:
            newposition = (position[0] + 1, position[1])

        if self.Joy.get_axis(1) > 0.3:
            newposition = (position[0], position[1]+1)

        if newposition is not None:
            if not collision.at_wall(playground, blo, newposition[0]) and \
                    not collision.on_ground(playground, blo, newposition[1]) and \
                    not collision.with_block(playground, blo, newposition[0], newposition[1]):
                position = newposition

        return position