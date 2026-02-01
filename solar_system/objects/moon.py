import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere

class Moon:
    def __init__(self, earth, radius=0.25):
        self.earth = earth   # parent object (Earth)

        # geometry
        self.radius = radius

        # -------- Orbit around Earth --------
        self.orbit_radius = 1.5
        self.orbit_angle = 0
        self.orbit_speed = 0.05   # faster than Earth

        # -------- Self rotation (spin) --------
        self.spin_angle = 0
        self.spin_speed = 0.5

        # -------- Axis tilt --------
        self.tilt_angle = 6.5   # Moon tilt ~6.5°

    def update(self):
        # revolution around Earth
        self.orbit_angle += self.orbit_speed

        # self rotation
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        """Draw Moon orbit around Earth"""
        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_LINE_LOOP)

        for i in range(150):
            t = 2 * math.pi * i / 150
            x = self.orbit_radius * math.cos(t)
            z = self.orbit_radius * math.sin(t)

            # relative to Earth
            glVertex3f(self.earth.x + x, self.earth.y, self.earth.z + z)

        glEnd()

    def draw(self):
        # draw orbit path
        self.draw_orbit_path()

        glPushMatrix()

        # ---- move to Earth (parent transform) ----
        glTranslatef(self.earth.x, self.earth.y, self.earth.z)

        # ---- Moon revolution ----
        x = self.orbit_radius * math.cos(self.orbit_angle)
        z = self.orbit_radius * math.sin(self.orbit_angle)
        glTranslatef(x, 0, z)

        # ---- Axis tilt ----
        glRotatef(self.tilt_angle, 1, 0, 0)

        # ---- Self spin ----
        glRotatef(self.spin_angle, 0, 1, 0)

        # draw Moon geometry
        glColor3f(0.8, 0.8, 0.8)  # light gray
        draw_sphere(radius=self.radius, lat_div=15, lon_div=30)

        glPopMatrix()
