from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, radians
import random

window_width, window_height = 0, 0
window_position_x, window_position_y = 0, 0
rotation_angle = 0

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    render_Scene()
    glFlush()
    glutSwapBuffers()

def render_Scene():
    pointSize = 0
    index = 1

    global rotation_angle
    rotation_angle += 1  # Increment the rotation angle

    for i in range(150):
        pointSize += 0.05
        index += 3
        colorG = random.random()
        colorR = random.random()
        colorB = random.random()
        glColor3f(colorR, colorB, colorG)
        glPointSize(pointSize)
        glBegin(GL_POINTS)
        angle = (index + rotation_angle) * (3.14159265 / 180.0)
        x = 0 + 0.7 * cos(angle)
        y = 0 + 0.7 * sin(angle)
        glVertex2f(x, y)
        glEnd()

def update_rotation_angle(value):
    global rotation_angle
    rotation_angle += 1
    glutPostRedisplay()
    glutTimerFunc(16, update_rotation_angle, 0)  # 60 frames per second

# GLUT callback function for window resize
def reshape(width, height):
    global window_width, window_height
    window_width, window_height = width, height


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Lab task")

gluOrtho2D(-1, 1, -1, 1)

# Register GLUT callback functions
glutDisplayFunc(display)
glutReshapeFunc(reshape)

# Set up the timer for continuous rotation
glutTimerFunc(0, update_rotation_angle, 0)

glutMainLoop()
