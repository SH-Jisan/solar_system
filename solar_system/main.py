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
from objects.mars_moon import MarsMoon
from objects.mars_moon2 import MarsMoon2
from objects.jupiter import Jupiter
from objects.jupiter_moons import JupiterMoons
from objects.saturn import Saturn
from objects.uranus import Uranus

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
mars_moon = MarsMoon(mars, radius=0.2)
mars_moon2 = MarsMoon2(mars, radius=0.15)
jupiter = Jupiter(sun, radius=1.2)
jupiter_moons = JupiterMoons(jupiter)
saturn = Saturn(sun, radius=1.0)
uranus = Uranus(sun, radius=0.9)

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
    mars_moon.update()
    mars_moon.draw()
    mars_moon2.update()
    mars_moon2.draw()

    jupiter.update()
    jupiter.draw()
    jupiter_moons.update()
    jupiter_moons.draw()

    saturn.update()
    saturn.draw()

    uranus.update()
    uranus.draw()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
