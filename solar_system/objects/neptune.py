import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere


class Neptune:
    def __init__(self, sun, radius=0.85):
        self.sun = sun   # parent (Sun)

        # -------- Geometry --------
        self.radius = radius

        # -------- Elliptical Orbit --------
        self.a = 28.0   # semi-major axis (farthest)
        self.b = 27.5   # semi-minor axis

        self.orbit_angle = 0
        self.orbit_speed = 0.003   # very slow (outer planet)

        # -------- Self Rotation --------
        self.spin_angle = 0
        self.spin_speed = 1.1

        # -------- Axis Tilt --------
        self.tilt_angle = 28.0   # Neptune tilt ≈ 28°

        # -------- World Position --------
        self.x = 0
        self.y = 0
        self.z = 0

    def update(self):
        # revolution around Sun (ellipse)
        self.x = self.a * math.cos(self.orbit_angle)
        self.z = self.b * math.sin(self.orbit_angle)
        self.y = 0

        self.orbit_angle += self.orbit_speed

        # self spin
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        glColor3f(0.3, 0.4, 1.0)  # blue orbit line
        glBegin(GL_LINE_LOOP)

        for i in range(300):
            t = 2 * math.pi * i / 300
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

        # move to Neptune orbit position
        glTranslatef(self.x, self.y, self.z)

        # axis tilt
        glRotatef(self.tilt_angle, 1, 0, 0)

        # self spin
        glRotatef(self.spin_angle, 0, 1, 0)

        # draw Neptune
        glColor3f(0.2, 0.3, 1.0)   # deep blue Neptune
        draw_sphere(radius=self.radius, lat_div=25, lon_div=50)

        glPopMatrix()
