from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Display callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Render scene
    render_Scene()

    # Swap buffers
    glutSwapBuffers()

# Scene render function
def render_Scene():
    # Perform a translation for the first/red triangle
    glPushMatrix()
    glTranslated(0.0, -0.4, 0.0)

    # Draw first/red triangle in Red at the bottom
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3, -0.1, -0.8)
    glVertex3f(0.3, -0.1, -1)
    glVertex3f(0, 0.3, -0.9)
    glEnd()

    # Pop the translation transformation
    glPopMatrix()

    # Perform a translation for the second/yellow triangle
    glPushMatrix()
    glTranslated(0.0, 0.4, 0.0)

    # Draw second/yellow triangle in Yellow at the top
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3, 0.2, 0.0)
    glVertex3f(-0.7, 0.5, 0.0)
    glVertex3f(-0.5, 0.7, 0.0)
    glEnd()

    # Pop the translation transformation
    glPopMatrix()

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow(b"Translation Example")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Enable depth testing for 3D rendering
glEnable(GL_DEPTH_TEST)

# Define callbacks
glutDisplayFunc(display)

# Set the perspective projection matrix
glMatrixMode(GL_PROJECTION)
gluPerspective(45, 1, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

# Begin event loop
glutMainLoop()
