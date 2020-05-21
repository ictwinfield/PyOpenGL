from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr
from PIL import Image

span = np.pi / 12

strip_vertices = []

for b in (0, span):
    for n in range(-6, 7):
        a = n * span
        x = np.round(np.cos(a) * np.sin(b), 3)
        strip_vertices.append(x)
        y = np.round(np.sin(a), 3)
        strip_vertices.append(y)
        z = np.round(np.cos(a) * np.cos(b), 3)
        strip_vertices.append(z)
        if n % 3 == 0:
            strip_vertices += [0.0, 0.0]
        elif n % 3 == 1:
            strip_vertices += [1.0, 0.0]
        else:
            strip_vertices += [1.0, 1.0]



strip_indices = [0, 1, 11, 
                1, 11, 2, 
                11, 2, 10, 
                2, 10, 3, 
                10, 3, 9, 
                3, 9, 4, 
                9, 4, 8, 
                4, 8, 5, 
                8, 5, 7, 
                5, 7, 6]

def get_strip_vertices():
    return np.array(strip_vertices, dtype=np.float32)

def get_strip_indices():
    return np.array(strip_indices, dtype=np.uint32)

class Strip():
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
        self.vert = 0
        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)

        # strip Vertex Buffer Object
        self.VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        # Strip Element Buffer Object
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
        self.y += y
        self.z += z
        self.pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([self.x, self.y, self.z]))
