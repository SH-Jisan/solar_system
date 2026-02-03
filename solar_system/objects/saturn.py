import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere


class Saturn:
    def __init__(self, sun, radius=1.0):
        self.sun = sun   # parent (Sun)

        # -------- Geometry --------
        self.radius = radius
        self.inclination =2.5

        # -------- Elliptical Orbit --------
        self.a = 20.0   # semi-major axis
        self.b = 19.5   # semi-minor axis

        self.orbit_angle = 0
        self.orbit_speed = 0.006   # slower than Jupiter

        # -------- Self Rotation --------
        self.spin_angle = 0
        self.spin_speed = 1.5

        # -------- Axis Tilt --------
        self.tilt_angle = 26.7   # Saturn axial tilt ≈ 26.7°

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
        glColor3f(0.7, 0.6, 0.4)
        glBegin(GL_LINE_LOOP)

        for i in range(240):
            t = 2 * math.pi * i / 240
            x = self.a * math.cos(t)
            z = self.b * math.sin(t)

            glVertex3f(self.sun.x + x, self.sun.y, self.sun.z + z)

        glEnd()

    def draw_rings(self):
        """Draw Saturn rings (flat disk)"""
        glColor3f(0.8, 0.8, 0.6)

        inner_radius = self.radius * 1.3
        outer_radius = self.radius * 2.0

        slices = 100

        glBegin(GL_TRIANGLE_STRIP)
        for i in range(slices + 1):
            angle = 2 * math.pi * i / slices
            x_outer = outer_radius * math.cos(angle)
            z_outer = outer_radius * math.sin(angle)

            x_inner = inner_radius * math.cos(angle)
            z_inner = inner_radius * math.sin(angle)

            glVertex3f(x_outer, 0, z_outer)
            glVertex3f(x_inner, 0, z_inner)
        glEnd()

    def draw(self):
        # draw orbit path
        self.draw_orbit_path()

        glPushMatrix()

        # move to Sun
        glTranslatef(self.sun.x, self.sun.y, self.sun.z)

        # move to Saturn orbit position
        glTranslatef(self.x, self.y, self.z)

        # tilt the whole Saturn system (planet + rings)
        glRotatef(self.tilt_angle, 1, 0, 0)

        # draw rings first
        self.draw_rings()

        # spin planet
        glRotatef(self.spin_angle, 0, 1, 0)

        # draw Saturn sphere
        glColor3f(0.9, 0.8, 0.5)
        draw_sphere(radius=self.radius, lat_div=25, lon_div=50)

        glPopMatrix()
