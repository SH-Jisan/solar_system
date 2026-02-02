import math
from OpenGL.GL import *
from geometry.sphere import draw_sphere


class JupiterMoon:
    def __init__(self, jupiter, orbit_radius, orbit_speed, radius, color):
        self.jupiter = jupiter   # parent (Jupiter)

        self.orbit_radius = orbit_radius
        self.orbit_angle = 0
        self.orbit_speed = orbit_speed

        self.radius = radius
        self.color = color

        self.spin_angle = 0
        self.spin_speed = 0.5

    def update(self):
        self.orbit_angle += self.orbit_speed
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw_orbit_path(self):
        glColor3f(0.5, 0.5, 0.5)
        glBegin(GL_LINE_LOOP)

        for i in range(100):
            t = 2 * math.pi * i / 100
            x = self.orbit_radius * math.cos(t)
            z = self.orbit_radius * math.sin(t)

            glVertex3f(self.jupiter.x + x,
                       self.jupiter.y,
                       self.jupiter.z + z)

        glEnd()

    def draw(self):
        self.draw_orbit_path()

        glPushMatrix()

        # move to Jupiter (parent)
        glTranslatef(self.jupiter.x, self.jupiter.y, self.jupiter.z)

        # moon revolution
        x = self.orbit_radius * math.cos(self.orbit_angle)
        z = self.orbit_radius * math.sin(self.orbit_angle)
        glTranslatef(x, 0, z)

        # self spin
        glRotatef(self.spin_angle, 0, 1, 0)

        glColor3f(*self.color)
        draw_sphere(radius=self.radius, lat_div=12, lon_div=24)

        glPopMatrix()


# --------- Container class for all Jupiter moons ----------
class JupiterMoons:
    def __init__(self, jupiter):
        self.moons = [
            # Io
            JupiterMoon(jupiter, orbit_radius=1.8, orbit_speed=0.08,
                        radius=0.15, color=(1.0, 0.9, 0.3)),
            # Europa
            JupiterMoon(jupiter, orbit_radius=2.4, orbit_speed=0.06,
                        radius=0.14, color=(0.8, 0.8, 0.9)),
            # Ganymede
            JupiterMoon(jupiter, orbit_radius=3.0, orbit_speed=0.04,
                        radius=0.18, color=(0.7, 0.7, 0.7)),
            # Callisto
            JupiterMoon(jupiter, orbit_radius=3.8, orbit_speed=0.03,
                        radius=0.17, color=(0.5, 0.5, 0.5)),
        ]

    def update(self):
        for moon in self.moons:
            moon.update()

    def draw(self):
        for moon in self.moons:
            moon.draw()
