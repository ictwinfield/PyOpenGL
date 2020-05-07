import pygame
from pygame.locals import *
from math import sin, cos, pi
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
    def __init__(self, x, y, z, s, solid):
        self.x = x
        self.y = y
        self.z = z
        self.solid = solid
        self.vertices = (
                        (x+s, y, z),
                        (x+s, y+s, z),
                        (x, y+s, z),
                        (x, y, z),
                        (x+s, y, z+s),
                        (x+s, y+s, z+s),
                        (x, y, z+s),
                        (x, y+s, z+s)
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
                glVertex3fv(self.vertices[v])
        glEnd()
        if self.solid:
            glColor3fv((0.8, 0.4, 0.4))
            glBegin(GL_QUADS)
            for face in self.surfaces:
                for v in face:
                    glVertex3fv(self.vertices[v])
            glEnd()
        
class Pyramid():
    def __init__(self, x, y, z, s, solid):
        self.x = x
        self.y = y
        self.z = z
        self.solid = solid
        self.vertices = (
            (x, y, z),
            (x+s, y, z),
            (x, y, z+s),
            (x+s, y, z+s),
            (x+s/2, y+s, z+s/2)
        )
        self.edges = (
            (0, 1),
            (0, 2),
            (0, 4),
            (3, 1),
            (3, 2),
            (3, 4),
            (4, 1),
            (4, 2)
        )
        self.sides = (
            (0, 2, 4),
            (0, 1, 4),
            (3, 2, 4),
            (3, 1, 4)
        )
        self.base = (0, 1, 3, 2)
    
    def draw(self):
        
        if self.solid:
            glColor3fv((0.3, 0.3, 0.3))
            glBegin(GL_TRIANGLES)
            for side in self.sides:
                for v in side:
                    glVertex3fv(self.vertices[v])
            glEnd()
            glBegin(GL_QUADS)
            for v in self.base:
                glVertex3fv(self.vertices[v])
            glEnd()
        glColor3fv((0, 0, 0))
        glBegin(GL_LINES)
        for edge in self.edges:
            for v in edge:
                glVertex3fv(self.vertices[v])
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
    bearing = 0
    pygame.init()
    display = (WIDTH, HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(1.0,-2.0, -12)
    cube = Cube(1, 0, 1, 2, True)
    pyramid = Pyramid(1, 2, 1, 2, True)

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
                    glTranslatef(0.2 * sin(bearing * pi/180), 0, 0.2 * cos(bearing * pi/180))
                if event.key == pygame.K_s:
                    glTranslatef(-0.2 * sin(bearing * pi/180), 0, -0.2 * cos(bearing * pi/180))
                if event.key == pygame.K_q:
                    bearing -= 10
                    glRotate(-10, 0, 1, 0)
                if event.key == pygame.K_e:
                    bearing += 10
                    glRotate(10, 0, 1, 0)
                
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 0.2)
                if event.button == 5:
                    glTranslatef(0, 0, -0.2)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)        
        ground()
        cube.draw()
        # glRotate(0.5, 3, 1, 1)
        pyramid.draw()
        pygame.display.flip()
        pygame.time.wait(8)

main()