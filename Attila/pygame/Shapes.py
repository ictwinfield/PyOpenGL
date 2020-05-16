from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr
from PIL import Image

cube_vertices = [-0.5, -0.5,  0.5, 0.0, 0.0,
             0.5, -0.5,  0.5, 1.0, 0.0,
             0.5,  0.5,  0.5, 1.0, 1.0,
            -0.5,  0.5,  0.5, 0.0, 1.0,

            -0.5, -0.5, -0.5, 0.0, 0.0,
             0.5, -0.5, -0.5, 1.0, 0.0,
             0.5,  0.5, -0.5, 1.0, 1.0,
            -0.5,  0.5, -0.5, 0.0, 1.0,

             0.5, -0.5, -0.5, 0.0, 0.0,
             0.5,  0.5, -0.5, 1.0, 0.0,
             0.5,  0.5,  0.5, 1.0, 1.0,
             0.5, -0.5,  0.5, 0.0, 1.0,

            -0.5,  0.5, -0.5, 0.0, 0.0,
            -0.5, -0.5, -0.5, 1.0, 0.0,
            -0.5, -0.5,  0.5, 1.0, 1.0,
            -0.5,  0.5,  0.5, 0.0, 1.0,

            -0.5, -0.5, -0.5, 0.0, 0.0,
             0.5, -0.5, -0.5, 1.0, 0.0,
             0.5, -0.5,  0.5, 1.0, 1.0,
            -0.5, -0.5,  0.5, 0.0, 1.0,

             0.5, 0.5, -0.5, 0.0, 0.0,
            -0.5, 0.5, -0.5, 1.0, 0.0,
            -0.5, 0.5,  0.5, 1.0, 1.0,
             0.5, 0.5,  0.5, 0.0, 1.0]

cube_indices = [ 0,  1,  2,  2,  3,  0,
            4,  5,  6,  6,  7,  4,
            8,  9, 10, 10, 11,  8,
           12, 13, 14, 14, 15, 12,
           16, 17, 18, 18, 19, 16,
           20, 21, 22, 22, 23, 20]

line_vertices = [-3.5, 0.0, 0.0, 0.0, 0.0, 1.0,
                 3.5, 0.0, 0.0, 1.0, 1.0, 1.0]
line_indices = [0, 1]

def get_ground_vertices(n):
    d = (n - 1) / 4
    vertices = []
    for i in range(n):
        vertices += [i/2 - d, -0.5, d, 1.0, 1.0, 1.0]
        vertices += [i/2 - d, -0.5, -d, 1.0, 1.0, 1.0]
        vertices += [-d, -0.5, i/2 - d, 1.0, 1.0, 1.0]
        vertices += [d, -0.5, i/2 - d, 1.0, 1.0, 1.0]
    return np.array(vertices, dtype=np.float32)

def get_ground_indices(n):
    return np.array(list(range(n * 4)), dtype=np.uint32)
        

def get_cube_vertices():
    return np.array(cube_vertices, dtype=np.float32)

def get_cube_indices():
    return np.array(cube_indices, dtype=np.uint32)

def get_line_vertices():
    return np.array(line_vertices, dtype=np.float32)

def get_line_indices():
    return np.array(line_indices, dtype=np.uint32)

class Cube():
    def __init__(self, vertices, indices, a_position, a_texture, offset, mod_loc, texture):
        self.off_set = offset
        self.a_pos = a_position
        self.a_tex = a_texture
        self.vertices = vertices
        self.indices = indices
        self.model_loc = mod_loc
        self.texture = texture
        self.pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
        self.x = 0
        self.y = 0
        self.z = 0

        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)

        # Cube Vertex Buffer Object
        self.VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        # Cube Element Buffer Object
        self.EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)
        
        glEnableVertexAttribArray(self.a_pos)
        glVertexAttribPointer(self.a_pos, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(self.a_tex)
        glVertexAttribPointer(self.a_tex, 2, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(self.off_set))
    
    def draw(self, switcher):
        glUniform1i(switcher, 0)
        glBindVertexArray(self.VAO)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, self.pos)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)
    
    def move(self, x, y, z):
        self.x += x
        self.y +=y
        self.z += z
        self.pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([self.x, self.y, self.z]))

        
class Line():
    def __init__(self, vertices, indices, a_position, a_color, offset, mod_loc):
        self.off_set = offset
        self.a_pos = a_position
        self.a_col = a_color
        self.vertices = vertices
        self.indices = indices
        self.model_loc = mod_loc
        self.pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))

        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)

        # Cube Vertex Buffer Object
        self.VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        # Cube Element Buffer Object
        self.EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)
        
        glEnableVertexAttribArray(self.a_pos)
        glVertexAttribPointer(self.a_pos, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(self.a_col)
        glVertexAttribPointer(self.a_col, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(self.off_set))

    def draw(self, switcher):
        glUniform1i(switcher, 1)
        glBindVertexArray(self.VAO)
        glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, self.pos)
        glDrawElements(GL_LINES, len(self.indices), GL_UNSIGNED_INT, None)