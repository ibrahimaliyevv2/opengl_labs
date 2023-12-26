# Template code to run OpenGL with Python

# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Global variables to store window size and position
window_width, window_height = 500, 500
window_x, window_y = 0, 0

# Display callback function
def display():
    # Set the background color to yellow (RGBA values)
    glClearColor(1.0, 1.0, 0.0, 1.0)
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    # Render scene
    render_Scene()

    # Swap buffers
    glutSwapBuffers()

# Reshape callback function
def reshape(width, height):
    global window_width, window_height, window_x, window_y
    window_width, window_height = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
    window_x, window_y = glutGet(GLUT_WINDOW_X), glutGet(GLUT_WINDOW_Y)

    # Request display update
    glutPostRedisplay()

# Scene render function
def render_Scene():
    # Set current color to red
    glColor3f(1.0, 0.0, 1.0)

    # Draw a red square
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

    # Display window size and position
    display_info()

# Function to display window size and position
def display_info():
    glColor3f(1.0, 0.0, 1.0)  # Set text color to white
    glWindowPos2i(10, 10)    # Set text position
    glutBitmapString(GLUT_BITMAP_HELVETICA_12, f"Window Size: {window_width} x {window_height}".encode('utf-8'))

    glWindowPos2i(10, 25)    # Set text position
    glutBitmapString(GLUT_BITMAP_HELVETICA_12, f"Window Position: {window_x} x {window_y}".encode('utf-8'))

# Initialize GLUT
glutInit()

# Get the screen width and height
screen_width = glutGet(GLUT_SCREEN_WIDTH)
screen_height = glutGet(GLUT_SCREEN_HEIGHT)

# Calculate the window position to center it
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(window_width, window_height)

# Create the window and give it a title
glutCreateWindow(b"My First OpenGL Window")

# Set the window position to center it on the screen
glutPositionWindow(window_x, window_y)

# Define callbacks
glutDisplayFunc(display)
glutReshapeFunc(reshape)

# Begin event loop
glutMainLoop()
