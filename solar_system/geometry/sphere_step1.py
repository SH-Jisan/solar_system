import math
from OpenGL.GL import *

def draw_sphere_lit(radius=2, lat_div=20, lon_div=40):
    """
    Draw sphere with NORMALS for lighting (shaded sphere)
    """

    for i in range(lat_div):
        theta1 = math.pi * i / lat_div
        theta2 = math.pi * (i + 1) / lat_div

        glBegin(GL_TRIANGLE_STRIP)

        for j in range(lon_div + 1):
            phi = 2 * math.pi * j / lon_div

            # ----- first ring point -----
            x1 = radius * math.sin(theta1) * math.cos(phi)
            y1 = radius * math.sin(theta1) * math.sin(phi)
            z1 = radius * math.cos(theta1)

            # normal = position normalized
            nx1 = x1 / radius
            ny1 = y1 / radius
            nz1 = z1 / radius

            glNormal3f(nx1, ny1, nz1)
            glVertex3f(x1, y1, z1)

            # ----- second ring point -----
            x2 = radius * math.sin(theta2) * math.cos(phi)
            y2 = radius * math.sin(theta2) * math.sin(phi)
            z2 = radius * math.cos(theta2)

            nx2 = x2 / radius
            ny2 = y2 / radius
            nz2 = z2 / radius

            glNormal3f(nx2, ny2, nz2)
            glVertex3f(x2, y2, z2)

        glEnd()
