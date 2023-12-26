from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

length = 0.2
arrow_dim = 0.05

# Define global rotation angles
rotate_x = 0.0
rotate_y = 0.0

# Display callback function
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Apply rotations
    glRotatef(rotate_x, 1, 0, 0)
    glRotatef(rotate_y, 0, 1, 0)

    # Render scene
    render_Scene()

    glutSwapBuffers()

# Scene render function
def render_Scene():
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(2.0)
    
    ###################
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(length, 0, 0)
    glEnd()

    ###################    
    glBegin(GL_LINES)
    glVertex3f(length, 0, 0)
    glVertex3f(length - arrow_dim, arrow_dim / 2, 0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(length, 0, 0)
    glVertex3f(length - arrow_dim, -arrow_dim / 2, 0)
    glEnd()    
    
    glBegin(GL_LINES)
    glVertex3f(length, 0, 0)
    glVertex3f(length - arrow_dim, 0, arrow_dim / 2)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(length, 0, 0)
    glVertex3f(length - arrow_dim, 0, -arrow_dim / 2)
    glEnd()    
    
    glColor3f(0.0, 1.0, 0.0)
    ###################
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, length, 0)
    glEnd()

    ###################
    glBegin(GL_LINES)
    glVertex3f(0, length, 0)
    glVertex3f(arrow_dim / 2, length - arrow_dim, 0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, length, 0)
    glVertex3f(-arrow_dim / 2, length - arrow_dim, 0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, length, 0)
    glVertex3f(0, length - arrow_dim, arrow_dim / 2)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, length, 0)
    glVertex3f(0, length - arrow_dim, -arrow_dim / 2)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)    
    ###################
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, length)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, 0, length)
    glVertex3f(arrow_dim / 2, 0, length - arrow_dim)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, 0, length)
    glVertex3f(-arrow_dim / 2, 0, length - arrow_dim)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, 0, length)
    glVertex3f(0, arrow_dim / 2, length - arrow_dim)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, 0, length)
    glVertex3f(0, -arrow_dim / 2, length - arrow_dim)
    glEnd()

def reshape(x, y):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(5.0, x / y, 4.5, 20.0)
    gluLookAt(2, -4, -2, 0, 0, 0, 0, 1, 0)
    glViewport(0, 0, x, y)

# Keyboard callback function
def keyboard(key, x, y):
    global rotate_x, rotate_y

    # Handle arrow key presses
    if key == GLUT_KEY_UP:
        rotate_x += 5.0
    elif key == GLUT_KEY_DOWN:
        rotate_x -= 5.0
    elif key == GLUT_KEY_RIGHT:
        rotate_y += 5.0
    elif key == GLUT_KEY_LEFT:
        rotate_y -= 5.0

    # Redraw the scene
    glutPostRedisplay()

# Initialize GLUT
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Enable depth testing
glutInitWindowSize(500, 500)
glutCreateWindow(b"Rotating Cube with Arrows")
glutInitWindowPosition(50, 50)

# Enable depth testing
glEnable(GL_DEPTH_TEST)

# Define callbacks
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutSpecialFunc(keyboard)  # Register the keyboard callback for special keys

# Begin event loop
glutMainLoop()
