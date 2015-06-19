from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import randint

width, height = 400, 400                                # width and height of the window
field_width, field_height = 300, 300                    # size of window where food appear


RECT_DELAY = 0
RECT_DELAY1 = 50

# initial position of the frame 
rect_x = 7
rect_y = 7

# speed of movement
v = 15

#initial position of the rectangle_monster
pol_x = 60
pol_y = 60

# size of the rectangle_moster
width_moster = 40
height_monster = 40

# size of the frame
RECT_WIDTH = 380
RECT_HEIGHT = 380
food_list = []


def draw_rect(x, y, width, height):
    glBegin(GL_LINE_LOOP)                              # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd() 


def draw_rect_monster(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd() 


def draw_rect_food(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd() 


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


#spreading food in the frame
def random_food(value):
    delay = randint(1000, 8000)

    x, y = randint(40, field_width), randint(40, field_height)
    food_list.append({"X":x, "Y":y})

    glutTimerFunc(delay, random_food,0)


def draw_food():
    for i in food_list:
        draw_rect_food(i["X"], i["Y"],10, 10)


def draw_monster():
    glColor3f(1.0, 0.0, 1.0)
    draw_rect_monster(pol_x, pol_y, width_moster, height_monster)


# control the rectangle monster with keyboard
def press(key, cx, cy):
    global pol_x
    global pol_y, v

    # up
    if key == GLUT_KEY_UP:
        pol_y += v
    # down
    if key == GLUT_KEY_DOWN:
        pol_y -= v
    # left 
    if key == GLUT_KEY_LEFT:
        pol_x -= v
    # right
    if key == GLUT_KEY_RIGHT:
        pol_x += v


# disappearing food after "eating" of the rectangle_monster
def eat_food():
    for i in food_list:
        x_condition = i["X"] > pol_x and i["X"] < (pol_x + width_moster)
        y_condition = i["Y"] > pol_y and  i["Y"] < (pol_y + height_monster)

        if x_condition and y_condition:
            food_list.remove(i)


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)     # clear the screen
    glLoadIdentity()                                       # reset position
    # ToDo draw rectangle
    refresh2d(width, height)   
    glColor3f(1.0, 1.0, 1.0)
    draw_rect(rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)
    glColor3f(0.0, 1.0, 0.0)
    draw_food()
    draw_monster()
    eat_food()
    glutSwapBuffers()                                  # important for double buffering


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Rectangle_monster")             # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
#glutKeyboardFunc(press)
glutSpecialFunc(press)
glutIdleFunc(draw)                                     # draw all the time
glutTimerFunc(RECT_DELAY1, random_food, 0)
glutMainLoop() 