from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

radius = 1.0
slices = 40   # u direction (latitude)
stacks = 40   # v direction (longitude)

def draw_sphere():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(0,0,5,  0,0,0,  0,1,0)

    glBegin(GL_POINTS)   # point দিয়ে sphere আঁকবো
    for i in range(slices):
        u = i * math.pi / slices          # u: 0 → π
        for j in range(stacks):
            v = j * 2 * math.pi / stacks # v: 0 → 2π

            x = radius * math.sin(u) * math.cos(v)
            y = radius * math.sin(u) * math.sin(v)
            z = radius * math.cos(u)

            glVertex3f(x, y, z)
    glEnd()

    glutSwapBuffers()

def init():
    glClearColor(0,0,0,1)
    glEnable(GL_DEPTH_TEST)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600,600)
    glutCreateWindow(b"Sphere using Parametric Equation")
    init()
    glutDisplayFunc(draw_sphere)
    glutMainLoop()

main()
