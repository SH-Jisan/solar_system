import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere

class MarsMoon2:
    def __init__(self, mars, radius=0.15):
        self.mars = mars   # parent object (Mars)

        # geometry
        self.radius = radius

        # -------- Orbit around Mars (farther & slower) --------
        self.orbit_radius = 2.0     # farther than first moon
        self.orbit_angle = 0
        self.orbit_speed = 0.04     # slower than Phobos-like moon

        # -------- Self rotation (spin) --------
        self.spin_angle = 0
        self.spin_speed = 0.3

        # -------- Axis tilt --------
        self.tilt_angle = 2.0

    def update(self):
        # revolution around Mars
        self.orbit_angle += self.orbit_speed

        # self spin
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        """Draw second moon orbit around Mars"""
        glColor3f(0.6, 0.6, 0.6)
        glBegin(GL_LINE_LOOP)

        for i in range(120):
            t = 2 * math.pi * i / 120
            x = self.orbit_radius * math.cos(t)
            z = self.orbit_radius * math.sin(t)

            glVertex3f(self.mars.x + x, self.mars.y, self.mars.z + z)

        glEnd()

    def draw(self):
        # draw orbit path
        self.draw_orbit_path()

        glPushMatrix()

        # ---- move to Mars (parent) ----
        glTranslatef(self.mars.x, self.mars.y, self.mars.z)

        # ---- Moon revolution ----
        x = self.orbit_radius * math.cos(self.orbit_angle)
        z = self.orbit_radius * math.sin(self.orbit_angle)
        glTranslatef(x, 0, z)

        # ---- tilt ----
        glRotatef(self.tilt_angle, 1, 0, 0)

        # ---- spin ----
        glRotatef(self.spin_angle, 0, 1, 0)

        # draw second Mars moon
        glColor3f(0.65, 0.65, 0.65)
        draw_sphere(radius=self.radius, lat_div=12, lon_div=24)

        glPopMatrix()
