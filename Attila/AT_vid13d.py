import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr
from TextureLoader import load_texture
from Shapes import Cube, Line
import Shapes


vertex_src = """
# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_color;
uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;
out vec3 v_color;
out vec2 v_texture;
void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
    v_color = a_color;
}
"""

fragment_src = """
# version 330
in vec2 v_texture;
in vec3 v_color;
out vec4 out_color;
uniform int switcher;
uniform sampler2D s_texture;
void main()
{
    if (switcher == 0){
        out_color = texture(s_texture, v_texture);
    }
    else if (switcher == 1){
        out_color = vec4(v_color, 1.0);   
    }
    
}
"""
count = [True, True]
y_vel = [0]
# glfw callback functions
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

def key_pressed(window, key, scancode, action, mods):
    x = 0
    z = 0
    if key == 65:
        x = -0.1
        z = 0
    elif key == 83:
        x = 0.1
        z = 0
    if key == 80:
        z = -0.1
        x = 0
    elif key == 76:
        z = 0.1
        x = 0
    if key == 32 and my_cube.vert == 0:
        my_cube.vert = 0.159       
    if count[0]:
        move_cube(x, z)
        count[0] = False
    else:
        count[0] = True

def move_cube(x, z):
    my_cube.move(x, 0, z)

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

# set callback function for key pressed
glfw.set_key_callback(window, key_pressed)

# make the context current
glfw.make_context_current(window)

cube_vertices = Shapes.get_cube_vertices()
cube_indices = Shapes.get_cube_indices()

line_vertices = Shapes.get_line_vertices()
line_indices = Shapes.get_line_indices()

ground_vertices = Shapes.get_ground_vertices(51)
ground_indices = Shapes.get_ground_indices(51)

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))
model_loc = glGetUniformLocation(shader, "model")
proj_loc = glGetUniformLocation(shader, "projection")
view_loc = glGetUniformLocation(shader, "view")
switcher_loc = glGetUniformLocation(shader, "switcher")

textures = glGenTextures(2)

cube_texture = load_texture("/home/melvin/Documents/Python/OpenGL/Attila/textures/crate.jpg", textures[0])
quad_texture = load_texture("/home/melvin/Documents/Python/OpenGL/Attila/textures/brick.jpg", textures[1])

# Create objects
my_cube = Cube(cube_vertices, cube_indices, 0, 1, 12, model_loc, textures[0])
my_cube.move(1, 0, 0)

my_ground = Line(ground_vertices, ground_indices, 0, 2, 12, model_loc)


glUseProgram(shader)
glClearColor(0.2, 0.2, 0.2, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280/720, 0.1, 100)

# eye, target, up
view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 2, 5]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))

glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # my_cube.move(x_vel, 0, z_vel)
    my_cube.draw(switcher_loc)
    
    my_ground.draw(switcher_loc)

    rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time())
    rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())          

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()