import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

HEIGHT = 600
WIDTH = 800

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

def cube():
    # We set the drawing colour that is used from then on
    glColor3fv((0.8, 0.2, 0.2))
    glBegin(GL_LINES)
    for edge in edges:
        for v in edge:
            glVertex3fv(vertices[v])
    glEnd()

def ground():
    glColor3fv((0.2, 0.2, 0.2))
    glBegin(GL_LINES)
    for n in range(-20, 20):
        glVertex3fv((10, 0, n/2))
        glVertex3fv((-10, 0, n/2))
        glVertex3fv((n/2, 0, 10))
        glVertex3fv((n/2, 0, -10))
    glEnd()


def main():
    pygame.init()
    display = (WIDTH, HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(1.0,-2.0, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glRotate(0.5, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)        
        ground()
        cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
