import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere

class Mercury:
    def __init__(self, sun, radius=0.5):
        self.sun = sun  # parent object (Sun)

        # geometry
        self.radius = radius

        self.a = 4.5
        self.b = 3.5

        # orbit (revolution)
        self.orbit_angle = 0
        self.orbit_speed = 0.03

        # self rotation (spin)
        self.spin_angle = 0
        self.spin_speed = 1.0

        # axis tilt (degrees)
        self.tilt_angle = 10   # exaggerated for visibility (real Mercury ≈ 0.03°)

    def update(self):
        # update orbit angle
        self.orbit_angle += self.orbit_speed

        # update spin
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        """Draw Mercury's orbit around the Sun (circle)"""
        glColor3f(1, 1, 1)  # white orbit line
        glBegin(GL_LINE_LOOP)

        for i in range(200):
            t = 2 * math.pi * i / 200
            x = self.a * math.cos(t)
            z = self.b * math.sin(t)

            # orbit is drawn relative to Sun
            glVertex3f(self.sun.x + x, self.sun.y, self.sun.z + z)

        glEnd()

    def draw(self):
        # ---- draw orbit path first ----
        self.draw_orbit_path()

        glPushMatrix()

        # move to Sun (parent transform)
        glTranslatef(self.sun.x, self.sun.y, self.sun.z)

        # Mercury revolution around Sun
        x = self.a * math.cos(self.orbit_angle)
        z = self.b * math.sin(self.orbit_angle)
        glTranslatef(x, 0, z)

        # ---- TILT (arbitrary axis rotation) ----
        glRotatef(self.tilt_angle, 1, 0, 0)   # tilt around X-axis

        # ---- SPIN (self rotation) ----
        glRotatef(self.spin_angle, 0, 1, 0)

        # draw Mercury geometry
        glColor3f(0.6, 0.6, 0.6)  # gray Mercury
        draw_sphere(radius=self.radius, lat_div=20, lon_div=40)

        glPopMatrix()
