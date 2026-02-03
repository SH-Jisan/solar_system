import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere

class Jupiter:
    def __init__(self, sun, radius=1.2):
        self.sun = sun   # parent (Sun)

        # -------- Geometry (big planet) --------
        self.radius = radius
        self.inclination = 1.3

        # -------- Elliptical Orbit (scaled) --------
        self.a = 16.0   # semi-major axis
        self.b = 15.5   # semi-minor axis (almost circular)

        self.orbit_angle = 0
        self.orbit_speed = 0.008   # much slower than Mars

        # -------- Self Rotation (spin) --------
        self.spin_angle = 0
        self.spin_speed = 2.0      # Jupiter spins fast

        # -------- Axis Tilt --------
        self.tilt_angle = 3.0      # Jupiter tilt ≈ 3°

        # -------- World Position --------
        self.x = 0
        self.y = 0
        self.z = 0

    def update(self):
        # ---- Jupiter revolution ----
        i = math.radians(self.inclination)
        self.x = self.a * math.cos(self.orbit_angle)
        self.z = self.b * math.sin(self.orbit_angle) * math.cos(i)
        self.y = self.b * math.sin(self.orbit_angle) * math.sin(i)

        self.orbit_angle += self.orbit_speed

        # ---- Jupiter self spin ----
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        glColor3f(0.7, 0.7, 0.4)  # light brown orbit line
        glBegin(GL_LINE_LOOP)

        for i in range(240):
            t = 2 * math.pi * i / 240
            x = self.a * math.cos(t)
            z = self.b * math.sin(t)

            glVertex3f(self.sun.x + x, self.sun.y, self.sun.z + z)

        glEnd()

    def draw(self):
        # draw orbit path
        self.draw_orbit_path()

        glPushMatrix()

        # ---- move to Sun (parent) ----
        glTranslatef(self.sun.x, self.sun.y, self.sun.z)

        # ---- move to Jupiter orbit position ----
        glTranslatef(self.x, self.y, self.z)

        # ---- axis tilt ----
        glRotatef(self.tilt_angle, 1, 0, 0)

        # ---- self spin ----
        glRotatef(self.spin_angle, 0, 1, 0)

        # ---- draw Jupiter ----
        glColor3f(0.8, 0.6, 0.3)   # brownish Jupiter
        draw_sphere(radius=self.radius, lat_div=25, lon_div=50)

        glPopMatrix()
