from OpenGL.GL import *

def draw_point(x, y, z):
    glPointSize(8)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 0)
    glVertex3f(x, y, z)
    glEnd()
