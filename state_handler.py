from world_objects.state import State
from settings import *

class StateHandler:
    def __init__(self, world):
        self.app = world.app
        # Modes| 0: Graph, 1: Searched, 2: Action Plan
        self.states = dict()
        self.states[(480, 33, 480)] = State(self, glm.ivec3(480.5, 33.5, 480.5))
        self.states[(481, 33, 481)] = State(self, glm.ivec3(481.5, 33.5, 480.5))
        self.states[(481, 33, 481)].mode = 1

    def create_state(self):
        self.states[(480, 33, 480)] = State(self, glm.ivec3(480.5, 33.5, 480.5))
        self.states[(481, 33, 481)] = State(self, glm.ivec3(481.5, 33.5, 480.5))
        self.states[(481, 33, 481)].mode = 1


    def set_state(self):
        pass

    def update(self):
        pass

    def render(self):
        for key in self.states:
            self.states[key].render()