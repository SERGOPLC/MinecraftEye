from settings import *
import moderngl as mgl
from world import World
from world_objects.voxel_marker import VoxelMarker
from world_objects.water import Water
from world_objects.clouds import Clouds
from world_objects.state import State
from world_objects.line import Line
import time


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
        self.edges[(480, 33, 480)] = Line(app, (480.45, 33.45, 480.45), (482.45, 37.45, 489.45))
        self.edges[(480, 33, 480)].mode = 3
        self.edges[(481, 33, 480)] = Line(app, (480.45, 33.45, 480.45), (481.45, 33.45, 480.45))
        self.edges[(481, 33, 480)].mode = 3
        self.grid = dict()
        self.time = time.time()
        self.render_mode = 0
        self.render_mode_name = 'All Data'
        self.read_only = False

    def update(self):
        self.world.update()
        self.voxel_marker.update()
        self.clouds.update()
        updated = False
        current_state = None

        if time.time() - self.time > 2 and not self.read_only:
            try:
                load_states = np.load('C:/Users/tron3/PycharmProjects/experiential-minecraft/examples/output/state_output.npy', allow_pickle=True).item()
                load_edges = np.load('C:/Users/tron3/PycharmProjects/experiential-minecraft/examples/output/edge_output.npy', allow_pickle=True).item()
                load_grid = np.load('C:/Users/tron3/PycharmProjects/experiential-minecraft/examples/output/grid_output.npy', allow_pickle=True).item()

                self.time = time.time()
                self.states = dict()
                self.edges = dict()

                for load_key in load_states.keys():
                    self.states[load_key] = State(self.app, glm.vec3(load_states[load_key][0] + (WORLD_W * CHUNK_SIZE / 2) + .33, load_states[load_key][1] + .33, load_states[load_key][2] + (WORLD_D * CHUNK_SIZE / 2) + .33))
                    self.states[load_key].mode = load_states[load_key][3]
                    updated = True

                for load_key in load_edges.keys():
                    self.edges[load_key] = Line(self.app, glm.vec3(load_edges[load_key][0] + (WORLD_W * CHUNK_SIZE / 2) + .45, load_edges[load_key][1] + .45, load_edges[load_key][2] + (WORLD_D * CHUNK_SIZE / 2) + .45), glm.vec3(load_edges[load_key][3] + (WORLD_W * CHUNK_SIZE / 2) + .45, load_edges[load_key][4] + .45, load_edges[load_key][5] + (WORLD_D * CHUNK_SIZE / 2) + .45))
                    self.edges[load_key].mode = load_edges[load_key][6]
                    updated = True

                for load_key in load_grid.keys():
                    if load_key not in self.grid.keys():
                        self.grid[load_key] = load_grid[load_key]
                        self.world.voxel_handler.add_voxel(load_grid[load_key][0] + (WORLD_W * CHUNK_SIZE / 2), load_grid[load_key][1], load_grid[load_key][2] + (WORLD_D * CHUNK_SIZE / 2), load_grid[load_key][3])
                        updated = True
            except FileNotFoundError:
                pass
            except PermissionError:
                pass

            # if updated:
            #     for state in self.states.keys():
            #         if self.states[state] != current_state:
            #             self.states[state].mode = 3




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

        # States / Edges render

        for key in self.states.keys():
            self.states[key].render()

        for key in self.edges.keys():
            match self.render_mode:
                case 0:
                    # 0 - All
                    self.edges[key].render()
                case 1:
                    # 1 - Only Plan
                    match self.edges[key].mode:
                        case 1:
                            self.edges[key].render()
                        case 4:
                            self.edges[key].render()
                        case 5:
                            self.edges[key].render()
                case 2:
                    # 2 - Plan + Perfect Match Edges
                    match self.edges[key].mode:
                        case 3:
                            self.edges[key].render()
                        case 1:
                            self.edges[key].render()
                        case 4:
                            self.edges[key].render()
                        case 5:
                            self.edges[key].render()
                case 3:
                    # 3 - Plan + Imperfect Match Edges
                    match self.edges[key].mode:
                        case 0:
                            self.edges[key].render()
                        case 1:
                            self.edges[key].render()
                        case 4:
                            self.edges[key].render()
                        case 5:
                            self.edges[key].render()
                case 4:
                    # 4 - Only Perfect Match Edges
                    if self.edges[key].mode == 3:
                        self.edges[key].render()
                case 5:
                    # 5 - Only Imperfect Match Edges
                    if self.edges[key].mode == 0:
                        self.edges[key].render()