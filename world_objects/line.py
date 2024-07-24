from settings import *
from meshes.line_mesh import LineMesh
from meshes.cube_mesh import CubeMesh


class Line:
    def __init__(self, app, start_pos, end_pos):
        self.app = app
        self.position = glm.vec3(start_pos[0], start_pos[1], start_pos[2])
        self.m_model = self.get_model_matrix()
        self.mesh = LineMesh(self.app, start_pos, end_pos)
        self.mode = 2

    def set_uniform(self):
        self.mesh.program['mode_id'] = self.mode
        self.mesh.program['m_model'].write(self.get_model_matrix())

    def get_model_matrix(self):
        m_model = glm.translate(glm.mat4(), glm.vec3(self.position))
        return m_model

    def render(self):
        self.set_uniform()
        self.mesh.render()
