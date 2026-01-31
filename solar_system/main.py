import glfw
from OpenGL.GL import *

from engine.window import create_window
from engine.camera import Camera
from geometry.axes import draw_axes
from objects.sun import Sun

window = create_window()
camera = Camera()

glfw.set_mouse_button_callback(window, camera.mouse_button_callback)
glfw.set_cursor_pos_callback(window, camera.cursor_position_callback)
glfw.set_scroll_callback(window, camera.scroll_callback)

sun = Sun(radius = 2, orbit_radius = 5)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    camera.apply()
    draw_axes()              # draw x,y,z

    sun.update()
    sun.draw()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
