from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 500, 400  
rect_x = 10
rect_y = 10 
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
    draw_rect(rect_x, rect_y, 200, 200)
    glColor3f(1.0, 0.0, 9.0)
    draw_line()
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
    #left 
	if key == GLUT_KEY_LEFT:
		rect_x -= 5
    # right
	if key == GLUT_KEY_RIGHT:
		rect_x += 5



# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("noobtuts.com")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
#glutKeyboardFunc(press)
glutSpecialFunc(press)
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop() 