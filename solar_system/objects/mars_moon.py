import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere

class MarsMoon:
    def __init__(self, mars, radius=0.2):
        self.mars = mars   # parent object (Mars)

        # geometry
        self.radius = radius

        # -------- Orbit around Mars --------
        self.orbit_radius = 1.2
        self.orbit_angle = 0
        self.orbit_speed = 0.08   # faster than Mars

        # -------- Self rotation (spin) --------
        self.spin_angle = 0
        self.spin_speed = 0.5

        # -------- Axis tilt --------
        self.tilt_angle = 1.0   # small tilt

    def update(self):
        # revolution around Mars
        self.orbit_angle += self.orbit_speed

        # self spin
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        """Draw moon orbit around Mars"""
        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_LINE_LOOP)

        for i in range(120):
            t = 2 * math.pi * i / 120
            x = self.orbit_radius * math.cos(t)
            z = self.orbit_radius * math.sin(t)

            # relative to Mars world position
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
        glRotatef(self.tilt_angle, 0, 0, 1)

        # ---- spin ----
        glRotatef(self.spin_angle, 0, 1, 0)

        # draw Mars moon
        glColor3f(0.7, 0.7, 0.7)  # grayish
        draw_sphere(radius=self.radius, lat_div=12, lon_div=24)

        glPopMatrix()
