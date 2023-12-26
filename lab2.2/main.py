from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin
import random

window_width, window_height = 0, 0
window_position_x, window_position_y = 0, 0

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    render_Scene()
    glFlush()
    glutSwapBuffers()


def draw_axes():
    glColor3f(1.0, 0.0, 0.0)  # Set color to red
    # Draw X-axis
    glBegin(GL_LINES)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glEnd()
    # Draw Y-axis
    glBegin(GL_LINES)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)
    glEnd()

def draw_triangle(x1,x2,x3,y1,y2,y3):
    glColor3f(1.0, 1.0, 0.0)  # Set color to yellow
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()


def render_Scene():
    draw_axes()
    # the triangle vertices
    draw_triangle(0.3,0.7,0.5,0.2,0.5,0.7)
    draw_triangle(-0.3,-0.7,-0.5,0.2,0.5,0.7)
    draw_triangle(0.3,0.7,0.5,-0.2,-0.5,-0.7)
    draw_triangle(-0.3,-0.7,-0.5,-0.2,-0.5,-0.7)


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

glutMainLoop()