import math
from OpenGL.GL import *

def draw_circle(radius, segments=1000):

    glColor3f(0, 1, 1)   # Cyan color
    glBegin(GL_LINE_LOOP)

    for i in range(segments):
        theta = 2 * math.pi * i / segments

        x = radius * math.cos(theta)   # X axis
        y = radius * math.sin(theta)   # Y axis
        z = 0    # XY plane

        glVertex3f(x, y, z)

    glEnd()
