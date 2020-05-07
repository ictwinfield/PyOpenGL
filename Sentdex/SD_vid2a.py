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

# The surfaces of our cube are quadrilaterals
surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

# Define some colours to use
colours = (
    (0.3, 0.2, 0.2),
    (0, 0.3, 0),
    (0, 0, 0.3)
)

# We define a cube by drawing all of its edges.  A line is made up of two vertices
def cube():
    # glColor3fv((0.5, 0.5, 0.5))
    # Because it is quads OpenGL knows it needs sets of 4 vertices
    glBegin(GL_QUADS)
    c = 0
    for face in surfaces:
        """
        # This colours each face
        glColor3fv(colours[c % 3])
        c += 1
        """
        for v in face:
            glColor3fv(colours[c % 3])
            c += 1
            glVertex3fv(vertices[v])
    glEnd()

    glColor3fv((0, 0, 0))
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
        
        glRotate(0.5, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()