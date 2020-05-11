from OpenGL.GL import *
import numpy as np
from OpenGL.GL.shaders import compileProgram, compileShader
from PIL import Image

def set_vertex_attribute_pointer(pos, size, quantity, offset, shader):
    glEnableVertexAttribArray(pos)
    glVertexAttribPointer(pos, size, GL_FLOAT, GL_FALSE, quantity, ctypes.c_void_p(offset))

def set_buffer_object(kind, buffer, data):
    glBindBuffer(kind, buffer)
    glBufferData(kind, data.nbytes, data, GL_STATIC_DRAW)

def load_image(addr):
    image = Image.open(addr)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = image.convert("RGBA").tobytes()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

def set_texture_parameter():
    # Set the texture wrapping parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    # Set texture filtering parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)