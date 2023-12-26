from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_width, window_height = 0, 0
window_position_x, window_position_y = 0, 0
triangle_translation = 0.0
triangle_speed = 0.005  # Adjust the speed as needed

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    render_Scene()
    glFlush()
    glutSwapBuffers()

def render_Scene():
    global triangle_translation

    # Draw a green triangle
    glColor3f(0, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.8 + triangle_translation, -0.3, -0.1)
    glVertex3f(-0.3 + triangle_translation, 0.5, 0.0)
    glVertex3f(0.2 + triangle_translation, 0.3, 0.2)
    glEnd()

    # Update the translation for continuous movement
    triangle_translation += triangle_speed

    # Reset the translation when the triangle reaches the right end
    if triangle_translation > 1.8:
        triangle_translation = -0.6

def reshape(width, height):
    global window_width, window_height
    window_width, window_height = width, height
    update_window_info()

def update_window_info():
    print("Window Size:", window_width, "x", window_height)
    print("Window Position:", window_position_x, ",", window_position_y)
    print()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"My OpenGL Window")

gluOrtho2D(-1, 1, -1, 1)

glutDisplayFunc(display)
glutReshapeFunc(reshape)

glutIdleFunc(display)  # Register the idle function for continuous rendering

glutMainLoop()
