import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

HEIGHT = 600
WIDTH = 800

# Every vertex needs to be registered
vertices = (
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 0),
    (1, 0, 1),
    (1, 1, 1),
    (0, 0, 1),
    (0, 1, 1)
    )
# Rather than refer to vertices individually we will find them by index
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

# We define a cube by drawing all of its edges.  A line is made up of two vertices
def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for v in edge:
            glVertex3fv(vertices[v])
    glEnd()

def main():
    pygame.init()
    display = (WIDTH, HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glRotate(0.5, 100, 10, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
