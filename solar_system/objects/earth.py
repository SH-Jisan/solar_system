import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere

class Earth:
    def __init__(self, sun, radius=0.75):
        self.sun = sun   # parent object (Sun)

        # -------- Geometry --------
        self.radius = radius

        self.inclination = 0.0
        # -------- Elliptical Orbit --------
        self.a = 9.0    # semi-major axis
        self.b = 8.8    # semi-minor axis

        self.orbit_angle = 0
        self.orbit_speed = 0.015

        # -------- Self Rotation --------
        self.spin_angle = 0
        self.spin_speed = 1.0

        # -------- Axis Tilt --------
        self.tilt_angle = 23.5

        # -------- World Position (IMPORTANT for Moon) --------
        self.x = 0
        self.y = 0
        self.z = 0

    def update(self):
        i = math.radians(self.inclination)
        # ---- Earth revolution (ellipse around Sun) ----
        self.x = self.a * math.cos(self.orbit_angle)
        self.z = self.b * math.sin(self.orbit_angle) * math.cos(i)
        self.y = self.b * math.sin(self.orbit_angle) * math.sin(i)

        self.orbit_angle += self.orbit_speed

        # ---- Earth self spin ----
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        glColor3f(0.8, 0.8, 0.8)
        glBegin(GL_LINE_LOOP)

        for i in range(200):
            t = 2 * math.pi * i / 200
            x = self.a * math.cos(t)
            z = self.b * math.sin(t)

            glVertex3f(self.sun.x + x, self.sun.y, self.sun.z + z)

        glEnd()

    def draw(self):
        # draw Earth orbit
        self.draw_orbit_path()

        glPushMatrix()

        # ---- move to Sun (parent) ----
        glTranslatef(self.sun.x, self.sun.y, self.sun.z)

        # ---- move to Earth's orbit position ----
        glTranslatef(self.x, self.y, self.z)

        # ---- tilt ----
        glRotatef(self.tilt_angle, 1, 0, 0)

        # ---- spin ----
        glRotatef(self.spin_angle, 0, 1, 0)

        # ---- draw Earth ----
        glColor3f(0.2, 0.4, 1.0)
        draw_sphere(radius=self.radius, lat_div=20, lon_div=40)

        glPopMatrix()
