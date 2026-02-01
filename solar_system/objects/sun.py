from OpenGL.GL import *
from geometry.sphere import draw_sphere

class Sun:
    def __init__(self, radius=2):
        self.radius = radius

        # Sun stays at origin
        self.x = 0
        self.y = 0
        self.z = 0

        # only self rotation
        self.spin_angle = 0
        self.spin_speed = 0.5

    def update(self):
        # only spin
        self.spin_angle += self.spin_speed
        if self.spin_angle >= 360:
            self.spin_angle -= 360

    def draw(self):
        glPushMatrix()

        glTranslatef(self.x, self.y, self.z)
        glRotatef(self.spin_angle, 0, 1, 0)

        # draw Sun geometry
        glColor3f(1.0, 0.7, 0.0)  # Sun color
        draw_sphere(radius=self.radius, lat_div=30, lon_div=60)

        glPopMatrix()
