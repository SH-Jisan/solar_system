import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere

class Venus:
    def __init__(self, sun, radius=0.7):
        self.sun = sun   # parent object (Sun)

        # -------- Geometry --------
        self.radius = radius

        # -------- Elliptical Orbit (realistic proportion) --------
        # Venus semi-major & semi-minor (scaled)
        self.a = 6.5   # X direction (orbit size)
        self.b = 6.3   # Z direction (almost circle)

        self.orbit_angle = 0
        self.orbit_speed = 0.02   # slower than Mercury

        # -------- Self Rotation (spin) --------
        self.spin_angle = 0
        self.spin_speed = 0.3     # Venus rotates slower

        # -------- Axis Tilt --------
        self.tilt_angle = 177     # Venus has extreme tilt (retrograde)

    def update(self):
        # update orbital motion (revolution)
        self.orbit_angle += self.orbit_speed

        # update self rotation (spin)
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        """Draw Venus orbit as an ellipse around Sun"""
        glColor3f(1, 1, 1)
        glBegin(GL_LINE_LOOP)

        for i in range(200):
            t = 2 * math.pi * i / 200
            x = self.a * math.cos(t)
            z = self.b * math.sin(t)

            # relative to Sun position
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

        # ---- Axis tilt (arbitrary axis rotation) ----
        glRotatef(self.tilt_angle, 1, 0, 0)

        # ---- Self spin ----
        glRotatef(self.spin_angle, 0, 1, 0)

        # ---- Draw Venus geometry ----
        glColor3f(0.9, 0.7, 0.3)   # yellowish Venus color
        draw_sphere(radius=self.radius, lat_div=20, lon_div=40)

        glPopMatrix()
