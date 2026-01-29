from OpenGL.GL import *

def draw_axes():
    glBegin(GL_LINES)

    # X axis (Red)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(3, 0, 0)

    # Y axis (Green)
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 3, 0)

    # Z axis (Blue)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 3)

    glEnd()
