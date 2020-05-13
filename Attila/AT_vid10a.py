import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr
from PIL import Image
import Shapes
from TextureLoader import load_texture


vertex_src = """
# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
uniform mat4 transformation; // combined translation
uniform mat4 projection;
out vec2 v_texture;
void main()
{
    gl_Position = projection * transformation * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

fragment_src = """
# version 330
in vec2 v_texture;
out vec4 out_color;
uniform sampler2D s_texture;
void main()
{
    out_color = texture(s_texture, v_texture);
}
"""


# glfw callback functions
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# creating the window
window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

# set the callback function for window resize
glfw.set_window_size_callback(window, window_resize)

# make the context current
glfw.make_context_current(window)

vertices = Shapes.cube_vertices
indices = Shapes.cube_indices

vertices = np.array(vertices, dtype=np.float32)
indices = np.array(indices, dtype=np.uint32)

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

# Vertex Buffer Object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

# Element Buffer Object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices.itemsize * 5, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices.itemsize * 5, ctypes.c_void_p(12))

# Here we generate our two textures
texture = glGenTextures(2)

cube_texture1 = load_texture("/home/melvin/Documents/Python/OpenGL/Attila/textures/crate.jpg", texture[0])
cube_texture2 = load_texture("/home/melvin/Documents/Python/OpenGL/Attila/textures/brick.jpg", texture[1])


glUseProgram(shader)
glClearColor(0, 0.3, 0.1, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280/720, 0.1, 100)

# Here we say what the cube translations will be
cube1_translation = pyrr.matrix44.create_from_translation(pyrr.Vector3([5, 0, -10]))
cube2_translation = pyrr.matrix44.create_from_translation(pyrr.Vector3([-1, 0, -3]))

transformation_loc = glGetUniformLocation(shader, "transformation")
proj_loc = glGetUniformLocation(shader, "projection")

glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw cube 1
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glUniformMatrix4fv(transformation_loc, 1, GL_FALSE, cube1_translation)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    # Draw cube 2
    glBindTexture(GL_TEXTURE_2D, texture[1])
    glUniformMatrix4fv(transformation_loc, 1, GL_FALSE, cube2_translation)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()