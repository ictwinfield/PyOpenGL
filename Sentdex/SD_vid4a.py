import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import randint

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
    def __init__(self, x, y, z, size, solid):
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        self.solid = solid
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
        self.surfaces = (
                    (0,1,2,3),
                    (3,2,7,6),
                    (6,7,5,4),
                    (4,5,1,0),
                    (1,5,7,2),
                    (4,0,3,6)
                    )

    def draw(self):
        glColor3fv((0.8, 0.2, 0.2))
        glBegin(GL_LINES)
        for edge in self.edges:
            for v in edge:
                glVertex3fv(tuple(i * self.size for i in self.vertices[v]))
        glEnd()
        if self.solid:
            glColor3fv((0.8, 0.4, 0.4))
            glBegin(GL_QUADS)
            for face in self.surfaces:
                for v in face:
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
    glTranslatef(1.0,-2.0, -12)
    cubes = []
    for i in range(1):
        cubes.append(Cube(randint(-5, 5), 0, 0, 1, True))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(0.2, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-0.2, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, 0.1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -0.1, 0)
                if event.key == pygame.K_w:
                    glTranslatef(0, 0, 0.2)
                if event.key == pygame.K_s:
                    glTranslatef(0, 0, -0.2)
                if event.key == pygame.K_q:
                    glRotate(-10, 0, 1, 0)
                if event.key == pygame.K_e:
                    glRotate(10, 0, 1, 0)
                
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 0.2)
                if event.button == 5:
                    glTranslatef(0, 0, -0.2)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)        
        ground()
        for c in cubes:
            c.draw()
        # glRotate(0.5, 0, 1, 0)
        pygame.display.flip()
        pygame.time.wait(8)

main()