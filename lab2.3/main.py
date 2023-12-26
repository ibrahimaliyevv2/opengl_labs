from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Global variable for the number of sides
n = 8

# Scene render function
def render_Scene():
    # Radius of the regular polygon
    radius = 0.5

    # Function to calculate vertex position for regular polygon
    def calculate_vertex(i):
        angle = 2 * math.pi * i / n
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        return x, y

    # Render regular polygon using GL_TRIANGLES
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    for i in range(n):
        glVertex2f(0, 0)
        glVertex2f(*calculate_vertex(i))
        glVertex2f(*calculate_vertex((i + 1) % n))
    glEnd()

    # Render regular polygon using GL_TRIANGLE_STRIP
    glColor3f(0, 1, 0)
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(n + 1):
        glVertex2f(*calculate_vertex(i % n))
        glVertex2f(*calculate_vertex((i + 1) % n))
    glEnd()

    # Render regular polygon using GL_TRIANGLE_FAN
    glColor3f(0, 0, 1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for i in range(n + 1):
        glVertex2f(*calculate_vertex(i % n))
    glEnd()

# Display callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    # Render scene
    render_Scene()

    # Swap buffers
    glutSwapBuffers()  

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow(b"Drawing a polygon using different directives")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define callbacks
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()
