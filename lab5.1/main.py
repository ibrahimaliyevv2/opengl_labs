from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def background():
    glClearColor(0.5, 0.5, 0.5, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def perspective():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    _, _, width, height = glGetDoublev(GL_VIEWPORT)
    gluPerspective(45, width / height, 0.25, 200)

def lookat():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 4, 0, 0, 0, 0, 1, 0)

def light():
    glLightfv(GL_LIGHT0, GL_AMBIENT, GLfloat_4(0.0, 1.0, 0.0, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, GLfloat_4(1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, GLfloat_4(1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(1.0, 1.0, 1.0, 0.0))
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

def depth():
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

def coneMaterial():
    glMaterialfv(GL_FRONT, GL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, GLfloat_4(0.8, 0.8, 0.8, 1.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, GLfloat_4(1.0, 0.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT, GL_SHININESS, GLfloat(50.0))

def transformationsCone():
    glRotatef(90, -1, 0, 0)
    glTranslatef(0.5, 1, -0.5)  # Smaller translation

def transformationsSphere():
    glTranslatef(0, 1, -0.5)

def drawCone(radius, height, slices, stacks):
    glPushMatrix()
    glutSolidCone(radius, height, slices, stacks)
    glPopMatrix()

def drawSphere(radius, slices, stacks):
    glPushMatrix()
    glutSolidSphere(radius, slices, stacks)
    glPopMatrix()

def display():
    background()
    perspective()
    lookat()
    light()
    depth()
    coneMaterial()
    transformationsCone()
    drawCone(1, 2, 50, 10)
    transformationsSphere()
    drawSphere(1, 50, 100)
    glutSwapBuffers()

# Initialize GLUT
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Moving Cone to the Right")

glClearColor(0.0, 0.0, 0.0, 0.0)
glutInitWindowPosition(50, 50)

# Define display callback
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()
