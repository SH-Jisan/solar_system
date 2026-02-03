import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere


class Uranus:
    def __init__(self, sun, radius=0.9):
        self.sun = sun   # parent (Sun)

        # -------- Geometry --------
        self.radius = radius
        self.inclination = 0.8

        # -------- Elliptical Orbit --------
        self.a = 24.0   # semi-major axis
        self.b = 23.5   # semi-minor axis

        self.orbit_angle = 0
        self.orbit_speed = 0.004   # slower than Saturn

        # -------- Self Rotation --------
        self.spin_angle = 0
        self.spin_speed = 1.2

        # -------- Axis Tilt --------
        self.tilt_angle = 98.0   # Uranus extreme tilt

        # -------- World Position --------
        self.x = 0
        self.y = 0
        self.z = 0

    def update(self):
        # revolution around Sun
        i = math.radians(self.inclination)
        self.x = self.a * math.cos(self.orbit_angle)
        self.z = self.b * math.sin(self.orbit_angle) * math.cos(i)
        self.y = self.b * math.sin(self.orbit_angle) * math.sin(i)

        self.orbit_angle += self.orbit_speed

        # self spin
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        glColor3f(0.5, 0.7, 1.0)  # bluish orbit line
        glBegin(GL_LINE_LOOP)

        for i in range(260):
            t = 2 * math.pi * i / 260
            x = self.a * math.cos(t)
            z = self.b * math.sin(t)

            glVertex3f(self.sun.x + x, self.sun.y, self.sun.z + z)

        glEnd()

    def draw(self):
        # draw orbit path
        self.draw_orbit_path()

        glPushMatrix()

        # move to Sun
        glTranslatef(self.sun.x, self.sun.y, self.sun.z)

        # move to Uranus orbit position
        glTranslatef(self.x, self.y, self.z)

        # tilt Uranus system
        glRotatef(self.tilt_angle, 1, 0, 0)

        # self spin
        glRotatef(self.spin_angle, 0, 1, 0)

        # draw Uranus
        glColor3f(0.5, 0.8, 1.0)   # cyan/blue Uranus
        draw_sphere(radius=self.radius, lat_div=25, lon_div=50)

        glPopMatrix()
