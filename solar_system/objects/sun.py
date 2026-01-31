import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere

class Sun:
    def __init__(self, radius=2, orbit_radius=5):
        # geometry
        self.radius = radius

        # orbit (revolution)
        self.orbit_radius = orbit_radius
        self.orbit_angle = 0
        self.orbit_speed = 0.01   # revolution speed

        # vertical oscillation
        self.osc_amplitude = 2.0   # A
        self.osc_speed = 0.5       # ω (relative to orbit angle)

        # self rotation (spin)
        self.spin_angle = 0
        self.spin_speed = 0.5

        # world position
        self.x = 0
        self.y = 0
        self.z = 0

    def update(self):
        # ---- Revolution (XZ plane) ----
        self.x = self.orbit_radius * math.cos(self.orbit_angle)
        self.z = self.orbit_radius * math.sin(self.orbit_angle)

        # ---- Vertical Oscillation (Y axis) ----
        self.y = self.osc_amplitude * math.sin(self.osc_speed * self.orbit_angle)

        # update orbit parameter (time)
        self.orbit_angle += self.orbit_speed

        # ---- Spin (self rotation) ----
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw(self):
        glPushMatrix()

        # Translation due to revolution + oscillation
        glTranslatef(self.x, self.y, self.z)

        # Self rotation (spin)
        glRotatef(self.spin_angle, 0, 1, 0)

        # Geometry
        draw_sphere(radius=self.radius, lat_div=30, lon_div=60)

        glPopMatrix()
