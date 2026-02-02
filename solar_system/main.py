import glfw
from OpenGL.GL import *

from engine.window import create_window
from engine.camera import Camera
from geometry.axes import draw_axes
from objects.earth import Earth
from objects.sun import Sun
from objects.mercury import Mercury
from objects.venus import Venus
from objects.moon import Moon
from objects.mars import Mars

window = create_window()
camera = Camera()

glfw.set_mouse_button_callback(window, camera.mouse_button_callback)
glfw.set_cursor_pos_callback(window, camera.cursor_position_callback)
glfw.set_scroll_callback(window, camera.scroll_callback)

sun = Sun(radius = 2)
mercury = Mercury(sun, radius=0.5)
venus = Venus(sun, radius=0.7)
earth = Earth(sun, radius=0.5)
moon = Moon(earth, radius=0.5)
mars = Mars(sun, radius=0.6)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    camera.apply()
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 0, 1))
    draw_axes()              # draw x,y,z

    sun.update()
    glDisable(GL_LIGHTING)
    sun.draw()
    glEnable(GL_LIGHTING)

    mercury.update()
    mercury.draw()

    venus.update()
    venus.draw()

    earth.update()
    earth.draw()

    moon.update()
    moon.draw()

    mars.update()
    mars.draw()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
