from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number

# initial position of the quard
rect_x = 0
rect_y = 200

# constants
RECT_WIDTH = 50
RECT_HEIGHT = 50
RECT_DELAY = 20
width, height = 400, 400                               # width and height of the window

# vector of direction
dy = -10
dx = 15

# window size
def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd() 

def draw_line():
    glBegin(GL_LINES)
    glVertex2i(10,10)
    glVertex2i(100,600)
    glEnd()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
   
    # ToDo draw rectangle
    refresh2d(width, height)   
    glColor3f(0.0, 0.0, 2.0)
    draw_rect(rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)
    glutSwapBuffers()                                  # important for double buffering

def press(key, x, y):
    global rect_y
    global rect_x

    # up
    if key == GLUT_KEY_UP:
        rect_y += 5
    # down
    if key == GLUT_KEY_DOWN:
        rect_y -= 5
    # left 
    if key == GLUT_KEY_LEFT:
        rect_x -= 5
    # right
    if key == GLUT_KEY_RIGHT:
        rect_x += 5


def rect_fall(value):
    global rect_y, rect_x, dy, dx

    rect_y += dy
    rect_x += dx

    # collision with the bottom wall
    if rect_y >= 0:
        dy = -1 * dy

    # collision with the up wall
    if rect_y <= height - RECT_HEIGHT:
        dy = -1 * dy

    # collision with the right wall
    if rect_x <= width - RECT_WIDTH:
        dx = -1 * dx

    # collision with the left wall
    if rect_x >= 0:
        dx = -1 * dx

    # action all the time
    glutTimerFunc(RECT_DELAY, rect_fall, 0)


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Moving ball")             # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
# glutKeyboardFunc(press)
glutSpecialFunc(press)
glutIdleFunc(draw)                                     # draw all the time
glutTimerFunc(RECT_DELAY, rect_fall, 0)
glutMainLoop() 