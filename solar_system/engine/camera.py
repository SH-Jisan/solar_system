import glfw
from OpenGL.GL import *

class Camera:
    def __init__(self):
        self.angle_x = 30     # vertical rotation
        self.angle_y = 30     # horizontal rotation
        self.distance = 10    # zoom (camera distance)

        self.last_x = 0
        self.last_y = 0
        self.dragging = False

    # Mouse button (left click)
    def mouse_button_callback(self, window, button, action, mods):
        if button == glfw.MOUSE_BUTTON_LEFT:
            if action == glfw.PRESS:
                self.dragging = True
                self.last_x, self.last_y = glfw.get_cursor_pos(window)
            elif action == glfw.RELEASE:
                self.dragging = False

    # Mouse move (drag)
    def cursor_position_callback(self, window, xpos, ypos):
        if self.dragging:
            dx = xpos - self.last_x
            dy = ypos - self.last_y

            self.angle_y += dx * 0.3
            self.angle_x += dy * 0.3

            self.last_x = xpos
            self.last_y = ypos

    # Mouse scroll (zoom)
    def scroll_callback(self, window, xoffset, yoffset):
        # yoffset: +ve scroll up, -ve scroll down
        self.distance -= yoffset
        if self.distance < 2:
            self.distance = 2
        if self.distance > 50:
            self.distance = 50

    # Apply camera transform
    def apply(self):
        glTranslatef(0, 0, -self.distance)
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)
