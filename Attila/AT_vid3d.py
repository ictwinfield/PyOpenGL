import glfw
from OpenGL.GL import *
import numpy as np
from OpenGL.GL.shaders import compileProgram, compileShader

vertex_src = """
# version 330

in vec3 a_position;
in vec3 a_color;

out vec3 v_color;

void main()
{
    gl_Position = vec4(a_position, 1.0);
    v_color = a_color;
}
"""

fragment_src = """
# version 330

in vec3 v_color;
out vec4 out_color;

void main()
{
    out_color = vec4(v_color, 1.0);
}
"""

def set_vertex_attribute_pointer(name, size, offset):
    pos = glGetAttribLocation(shader, name)
    glEnableVertexAttribArray(pos)
    glVertexAttribPointer(pos, size, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(offset))

if not glfw.init():
    raise Exception("glfw can not be initialized!")

window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

glfw.set_window_pos(window, 400, 200)

glfw.make_context_current(window)

vertices = [-0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0,
             1.0, 0.0, 0.0,
             0.0, 1.0, 0.0,
             0.0, 0.0, 1.0]

vertices = np.array(vertices, dtype=np.float32)

# Create a compiled shader
shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

# Create the vertex buffer object that is where the information is put to be pass to the compiled shader program
VBO = glGenBuffers(1)
# We now bind the VBO to the GL_ARRAY_BUFFER
glBindBuffer(GL_ARRAY_BUFFER, VBO)

glBufferData(GL_ARRAY_BUFFER, vertices.nbytes,vertices, GL_STATIC_DRAW)

set_vertex_attribute_pointer("a_position", 3, 0)
set_vertex_attribute_pointer("a_color",3, 36)

# Tell the GPU to use this shader
glUseProgram(shader)

glClearColor(0, 0.1, 0.1, 1)

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    ct = glfw.get_time() 

    glLoadIdentity()

    glDrawArrays(GL_TRIANGLES, 0, 3)

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()