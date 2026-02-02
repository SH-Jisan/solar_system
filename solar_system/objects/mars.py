import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere

class Mars:
    def __init__(self, sun, radius=0.6):
        self.sun = sun   # parent object (Sun)

        # -------- Geometry --------
        self.radius = radius

        # -------- Elliptical Orbit (scaled realistic) --------
        self.a = 12.0   # semi-major axis
        self.b = 11.5   # semi-minor axis

        self.orbit_angle = 0
        self.orbit_speed = 0.012   # slower than Earth

        # -------- Self Rotation (spin) --------
        self.spin_angle = 0
        self.spin_speed = 0.9

        # -------- Axis Tilt --------
        self.tilt_angle = 25.0   # Mars tilt ≈ 25°

        # -------- World Position --------
        self.x = 0
        self.y = 0
        self.z = 0

    def update(self):
        # ---- Mars revolution ----
        self.x = self.a * math.cos(self.orbit_angle)
        self.z = self.b * math.sin(self.orbit_angle)
        self.y = 0

        self.orbit_angle += self.orbit_speed

        # ---- Mars self spin ----
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        glColor3f(1.0, 0.5, 0.5)  # reddish orbit line
        glBegin(GL_LINE_LOOP)

        for i in range(200):
            t = 2 * math.pi * i / 200
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

        # ---- move to Mars orbit position ----
        glTranslatef(self.x, self.y, self.z)

        # ---- axis tilt ----
        glRotatef(self.tilt_angle, 1, 0, 0)

        # ---- self spin ----
        glRotatef(self.spin_angle, 0, 1, 0)

        # ---- draw Mars ----
        glColor3f(0.8, 0.3, 0.2)   # red/orange Mars color
        draw_sphere(radius=self.radius, lat_div=20, lon_div=40)

        glPopMatrix()
