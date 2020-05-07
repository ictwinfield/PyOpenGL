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

class Cube():
    def __init__(self, x, y, z, s):
        self.x = x
        self.y = y
        self.z = z
        self.size = s
        self.vertices = (
                        (x+1, y, z),
                        (x+1, y+1, z),
                        (x, y+1, z),
                        (x, y, z),
                        (x+1, y, z+1),
                        (x+1, y+1, z+1),
                        (x, y, z+1),
                        (x, y+1, z+1)
                        )
        self.edges = (
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

    def draw(self):
        glColor3fv((0.8, 0.2, 0.2))
        glBegin(GL_LINES)
        for edge in self.edges:
            for v in edge:
                glVertex3fv(tuple(i * self.size for i in self.vertices[v]))
        glEnd()

def ground():
    glColor3fv((0.1, 0.15, 0.1))
    glBegin(GL_LINES)
    for n in range(-200, 200):
        glVertex3fv((100, 0, n/2))
        glVertex3fv((-100, 0, n/2))
        glVertex3fv((n/2, 0, 100))
        glVertex3fv((n/2, 0, -100))
    glEnd()


def main():
    pygame.init()
    display = (WIDTH, HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(1.0,-2.0, -10)
    cube1 = Cube(-1, 0, 0, 1)
    cube2 = Cube(1, 0, 1, 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glRotate(0.5, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)        
        ground()
        cube1.draw()
        cube2.draw()
        pygame.display.flip()
        pygame.time.wait(8)

main()
