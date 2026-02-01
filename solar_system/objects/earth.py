import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere

class Earth:
    def __init__(self, sun, radius=0.75):
        self.sun = sun   # parent object (Sun)

        # -------- Geometry --------
        self.radius = radius

        # -------- Elliptical Orbit (scaled real proportion) --------
        self.a = 9.0    # semi-major axis (X direction)
        self.b = 8.8    # semi-minor axis (Z direction)

        self.orbit_angle = 0
        self.orbit_speed = 0.015   # slower than Venus

        # -------- Self Rotation (spin) --------
        self.spin_angle = 0
        self.spin_speed = 1.0      # Earth spins faster than Venus

        # -------- Axis Tilt --------
        self.tilt_angle = 23.5     # Earth axial tilt (realistic)

    def update(self):
        # update orbital motion (revolution)
        self.orbit_angle += self.orbit_speed

        # update self rotation (spin)
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        """Draw Earth's orbit (ellipse) around Sun"""
        glColor3f(0.8, 0.8, 0.8)
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

        # ---- Parent transform (Sun position) ----
        glTranslatef(self.sun.x, self.sun.y, self.sun.z)

        # ---- Elliptical revolution ----
        x = self.a * math.cos(self.orbit_angle)
        z = self.b * math.sin(self.orbit_angle)
        glTranslatef(x, 0, z)

        # ---- Axis tilt ----
        glRotatef(self.tilt_angle, 1, 0, 0)

        # ---- Self spin ----
        glRotatef(self.spin_angle, 0, 1, 0)

        # ---- Draw Earth geometry ----
        glColor3f(0.2, 0.4, 1.0)   # bluish Earth
        draw_sphere(radius=self.radius, lat_div=20, lon_div=40)

        glPopMatrix()
