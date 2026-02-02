import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.1, 0.1, 0.1, 1))

def create_window():
    if not glfw.init():
        raise Exception("GLFW init failed")

    window = glfw.create_window(1200, 800, "Solar System, red-x, green-y, blue-z ", None, None)
    glfw.make_context_current(window)

    glEnable(GL_DEPTH_TEST)
    setup_lighting()
    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 0.1, 50)
    glMatrixMode(GL_MODELVIEW)


    return window
