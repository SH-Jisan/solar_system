import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

def create_window():
    if not glfw.init():
        raise Exception("GLFW init failed")

    window = glfw.create_window(800, 600, "Solar System, red-x, green-y, blue-z ", None, None)
    glfw.make_context_current(window)

    glEnable(GL_DEPTH_TEST)
    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 0.1, 50)
    glMatrixMode(GL_MODELVIEW)

    return window
