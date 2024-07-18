from settings import *
import moderngl as mgl
from world import World
from world_objects.voxel_marker import VoxelMarker
from world_objects.water import Water
from world_objects.clouds import Clouds
from world_objects.state import State
from world_objects.line import Line


class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)
        self.voxel_marker = VoxelMarker(self.world.voxel_handler)
        self.water = Water(app)
        self.clouds = Clouds(app)
        self.states = dict()
        self.states[(480, 33, 480)] = State(app, glm.vec3(480.33, 33.33, 480.33))
        self.states[(480, 33, 480)].mode = 0
        self.states[(482, 37, 489)] = State(app, glm.vec3(482.33, 37.33, 489.33))
        self.states[(482, 37, 489)].mode = 0
        self.states[(481, 33, 480)] = State(app, glm.vec3(481.33, 33.33, 480.33))
        self.states[(481, 33, 480)].mode = 1
        self.states[(482, 33, 480)] = State(app, glm.vec3(482.33, 33.33, 480.33))
        self.states[(482, 33, 480)].mode = 2
        self.states[(483, 33, 480)] = State(app, glm.vec3(483.33, 33.33, 480.33))
        self.states[(483, 33, 480)].mode = 3
        self.states[(484, 33, 480)] = State(app, glm.vec3(484.33, 33.33, 480.33))
        self.states[(484, 33, 480)].mode = 0
        self.states[(485, 33, 480)] = State(app, glm.vec3(485.33, 33.33, 480.33))
        self.states[(485, 33, 480)].mode = 0
        self.states[(486, 33, 480)] = State(app, glm.vec3(486.33, 33.33, 480.33))
        self.states[(486, 33, 480)].mode = 0
        self.states[(487, 33, 480)] = State(app, glm.vec3(487.33, 33.33, 480.33))
        self.states[(487, 33, 480)].mode = 0
        self.edges = dict()
        self.edges[(480, 33, 480)] = Line(app, (480.475, 33.475, 480.475), (482.475, 37.475, 489.475))
        self.edges[(480, 33, 480)].mode = 3
        self.edges[(481, 33, 480)] = Line(app, (480.475, 33.475, 480.475), (481.475, 33.475, 480.475))
        self.edges[(481, 33, 480)].mode = 3

    def update(self):
        self.world.update()
        self.voxel_marker.update()
        self.clouds.update()

    def render(self):
        # chunks rendering
        self.world.render()

        # rendering without cull face
        self.app.ctx.disable(mgl.CULL_FACE)
        self.clouds.render()
        self.water.render()
        self.app.ctx.enable(mgl.CULL_FACE)

        # voxel selection
        self.voxel_marker.render()

        # States render
        for key in self.states.keys():
            self.states[key].render()

        for key in self.edges.keys():
            self.edges[key].render()
